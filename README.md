# File Organizer

A simple Python script to automatically organize files on your Desktop and in your Downloads folder.

## Features

- Organizes files by type (documents, images, videos, etc.)
- Analyzes directories before organizing
- Provides a preview of changes before making them
- Handles duplicate files automatically

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/cbarnes0/desktop-organizer.git
   cd desktop-organizer
   ```

2. Set your file paths using environment variables:

   **Windows (Command Prompt):**
   ```
   set DESKTOP_PATH=C:\path\to\your\desktop
   set DOWNLOADS_PATH=C:\path\to\your\downloads
   ```

   **Windows (PowerShell):**
   ```
   $env:DESKTOP_PATH = "C:\path\to\your\desktop"
   $env:DOWNLOADS_PATH = "C:\path\to\your\downloads"
   ```

   **Mac/Linux:**
   ```
   export DESKTOP_PATH=/path/to/your/desktop
   export DOWNLOADS_PATH=/path/to/your/downloads
   ```

   Note: If you don't set these variables, the script will try to use the default paths (`~/Desktop` and `~/Downloads`).

## Usage

Run the script:

```
python file_organizer.py
```

The script will:
1. Analyze each directory
2. Show you a preview of changes
3. Ask for confirmation before organizing files
4. Move files into appropriate folders based on their type

## Customization

You can customize the file types and categories by editing the `file_types` dictionary in the script:

```python
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    # Add or modify categories and extensions as needed
}
```

## Contributing

If you have an idea or suggestion to improve feel free to make a PR.

