# Media Library Optimizer

Media Library Optimizer is a Python script designed to analyze and optimize your media library.

## Features

- **Library Analysis:** Gain insights into your media library with file format breakdowns and overall file counts.
- **Remove Orphaned Files:** Automatically remove orphaned NFO files that clutter your library.
- **Rename Folders:** Streamline your library by removing unnecessary URL prefixes from folder names.

## Requirements

- Python 3.x

## Usage

```bash
python media-library-optimizer.py -l /path/to/media/library
```
```
options:
  -h, --help            show this help message and exit
  -l LOCATION, --location LOCATION
                        Path to the media location
  -a, --analyze         Perform library analysis
  -r, --remove-orphaned
                        Remove orphaned files
  -re, --rename-folders
                        Remove URL prefix folders
  -y, --yes             Automatic yes to prompts
```

## Contribute

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.