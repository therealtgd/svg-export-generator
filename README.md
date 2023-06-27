# SVG Export Generator

This script generates an `index.js` file in your SVG folder containing export statements for all your SVG icons. It scans your JavaScript or TypeScript files for import statements, extracts the icon names, and creates corresponding export statements in the `index.js` file.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.9 or newer

## Installation

1. Clone this repository or download the `svg_export_generator.py` file.
2. Ensure you have Python 3.9 or newer installed on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder containing the `svg_export_generator.py` file.
3. Run the following command:

```bash
python svg_export_generator.py /path/to/svg/folder /path/to/js/ts/folder
```
Replace `/path/to/svg/folder` with the path to your SVG folder and `/path/to/js/ts/folder` with the path to your JavaScript or TypeScript folder.

The script will generate an `index.js` file in your SVG folder with export statements for all your SVG icons.

## New Function: refactor_imports
The `refactor_imports` function was added to the script. This function allows you to refactor your import statements in JavaScript or TypeScript files to use a single import statement for all SVG files.

Here's how the `refactor_imports` function works:

1. It traverses the target folder recursively to find JavaScript or TypeScript files.
2. For each file, it reads the content and searches for import statements that import SVG files.
3. If import statements are found, it refactors them to use a single import statement for all SVG files.
4. The refactored import statement is inserted before the first import statement in the file.
5. The modified content is then written back to the file.
6. The `refactor_imports` function improves code readability by consolidating multiple import statements for SVG files into a single import statement.

To use the `refactor_imports` function run the script with a third argument which is the folder from where to import the svg files.
Example:
```bash
python svg_export_generator.py /path/to/svg/folder /path/to/js/ts/folder /icons
```

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.