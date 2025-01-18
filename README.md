# CBZ WebP Corruption Checker

This Python script scans through CBZ files in a directory (and its subdirectories) to identify corrupted WebP images without extracting the archives.

## Features

- Recursively scans all .cbz files in the specified directory
- Checks WebP files for corruption without extracting them to disk
- Generates a report of corrupted files
- Memory-efficient processing

## Requirements

- Python 3.6+
- Pillow library

## Installation

1. Clone or download this repository

2. Create and activate a virtual environment:

   **Windows:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

   **Linux/MacOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script by providing the path to scan:
```bash
python check_corrupted_webp.py "path/to/scan"
```

The script will:
1. Scan all .cbz files in the specified directory and its subdirectories
2. Check each WebP file within the CBZ archives for corruption
3. Generate a `corrupted_webp_files.txt` report in the current directory

## Output

The script creates a `corrupted_webp_files.txt` file containing:
- List of corrupted WebP files (format: `cbz_path:webp_file_path`)
- Any errors encountered during processing
- "No corrupted WebP files found" message if all files are valid

## Error Handling

- Invalid paths will generate an error message
- Corrupted CBZ files will be noted in the report
- Individual corrupted WebP files will be listed with their specific errors

## License

This project is open source and available under the MIT License.