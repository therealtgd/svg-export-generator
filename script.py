import os
import sys
import re
import textwrap
from collections import defaultdict

def find_svg_filenames(svg_folder):
    svg_filenames = []
    for root, _, files in os.walk(svg_folder):
        for file in files:
            if file.endswith('.svg'):
                svg_filenames.append(os.path.splitext(file)[0])
    return svg_filenames

def find_import_statements(target_folder, svg_filenames):
    file_types = ('.js', '.jsx', '.ts', '.tsx')
    import_statements = defaultdict(set)

    for root, _, files in os.walk(target_folder):
        for file in files:
            if file.endswith(file_types):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    for svg_filename in svg_filenames:
                        pattern = re.compile(fr"import\s+(\w+)\s+from\s+['\"].*/{svg_filename}\.svg['\"]")
                        matches = pattern.finditer(content)
                        for match in matches:
                            import_name = match.group(1)
                            import_statements[import_name].add(svg_filename)
    return import_statements

def generate_export_statements(svg_folder, import_statements):
    export_file = os.path.join(svg_folder, 'index.js')
    with open(export_file, 'w') as f:
        for import_name, svg_filenames in import_statements.items():
            for svg_filename in svg_filenames:
                f.write(f"export {{ default as {import_name} }} from './{svg_filename}.svg';\n")

def refactor_imports(js_ts_folder, svg_export_path):
    for root, _, files in os.walk(js_ts_folder):
        for file in files:
            if file.endswith(('.js', '.jsx', '.ts', '.tsx')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                matches = re.findall(r"import\s+(\w+)\s+from\s+['\"](\S+\.svg)['\"];", content)
                if not matches:
                    continue

                svg_imports = [f"{match[0]}" for match in matches]
                if len(svg_imports) > 3 or len(', '.join(svg_imports)) + len(svg_export_path) + 26 > 120:
                    import_statement = "import {{\n{0},\n}} from '{1}';\n".format(
                        textwrap.indent(',\n'.join(svg_imports), '    '),
                        svg_export_path
                    )
                else:
                    import_statement = "import {{ {0} }} from '{1}';\n".format(
                        ', '.join(svg_imports),
                        svg_export_path
                    )

                first_import_match = re.search(r"import\s+(\w+)\s+from\s+['\"](\S+\.svg)['\"];", content)
                before_first_import = content[:first_import_match.start()]
                after_first_import = re.sub(
                    r"import\s+(\w+)\s+from\s+['\"](\S+\.svg)['\"];\n?",
                    "",
                    content[first_import_match.start():]
                )
                modified_content = before_first_import + import_statement + after_first_import

                with open(file_path, 'w') as f:
                    f.write(modified_content)

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: python {script_name} <SVG_folder> <JS_TS_folder> [optional:svg_export_path]")
        sys.exit(1)

    svg_folder = sys.argv[1]
    target_folder = sys.argv[2]

    svg_filenames = find_svg_filenames(svg_folder)
    import_statements = find_import_statements(target_folder, svg_filenames)
    generate_export_statements(svg_folder, import_statements)

    if len(sys.argv) > 3:
        svg_export_path = sys.argv[3]
        refactor_imports(target_folder, svg_export_path)

if __name__ == "__main__":
    main()