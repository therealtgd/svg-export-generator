import os
import re
import sys
import pathlib

def replace_imports(root_folder, root_alias):
    # Check if root_alias ends with '/' and remove it if it does
    if root_alias.endswith('/'):
        root_alias = root_alias[:-1]
    
    # Regex to match import statements
    import_re = re.compile(r'import (.+?) from \'(.+?)\';')

    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(('.js', '.jsx', '.ts', '.tsx')):
                filepath = os.path.join(foldername, filename)
                # Open the file in binary mode
                with open(filepath, 'rb') as file:
                    # Read the file content and decode it with UTF-8, ignoring errors
                    content = file.read().decode('utf-8', errors='ignore')

                    matches = import_re.findall(content)
                    for match in matches:
                        import_path = match[1]
                        if import_path.startswith('..'):
                            # Calculate the absolute path of the imported module
                            absolute_path = (pathlib.Path(foldername) / import_path).resolve()
                            # Calculate the new import path relative to the root folder
                            new_path = str(absolute_path.relative_to(root_folder))
                            # Ensure the new path doesn't start with a '/'
                            if new_path.startswith('/'):
                                new_path = new_path[1:]
                            # Remove root folder from new path
                            new_path = new_path.replace(root_folder, "")

                            # Replace the old import path with the new one
                            content = content.replace(import_path, f'{root_alias}/{new_path}')
                    
                    # Write the modified content back to the file
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(content)

if __name__ == "__main__":
    root_folder = sys.argv[1]
    root_alias = sys.argv[2]
    replace_imports(root_folder, root_alias)