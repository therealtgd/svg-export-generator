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

1. Clone this repository or download the `script.py` file.
2. Ensure you have Python 3.9 or newer installed on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder containing the `script.py` file.
3. Run the following command:

```bash
python script.py /path/to/svg/folder /path/to/js/ts/folder
```
Replace `/path/to/svg/folder` with the path to your SVG folder and `/path/to/js/ts/folder` with the path to your JavaScript or TypeScript folder.

The script will generate an `index.js` file in your SVG folder with export statements for all your SVG icons.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.