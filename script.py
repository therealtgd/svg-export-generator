import os
import sys
import re
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

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <SVG_folder> <JS_TS_folder>")
        sys.exit(1)

    svg_folder = sys.argv[1]
    target_folder = sys.argv[2]

    svg_filenames = find_svg_filenames(svg_folder)
    import_statements = find_import_statements(target_folder, svg_filenames)
    generate_export_statements(svg_folder, import_statements)

if __name__ == "__main__":
    main()
