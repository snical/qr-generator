# QR Generator

A minimal Python script that generates QR codes from a URL and saves them as PNG files.

## Features

- Generates a QR code from a URL
- Lets you choose the file name
- Automatically replaces spaces with `_`
- Saves all QR codes into the `codes/` folder
- Automatically creates the folder if it doesn’t exist

## Project Structure

```
QR-GENERATOR/
├── codes/
├── main.py
├── requirements.txt
├── .gitignore
```

## Requirements

- Python 3.8 or newer
- `qrcode` library

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

You will be prompted to enter:

- A URL
- A name for the QR code file

Example:

```
URL: https://example.com
QR name: my website
```

This will generate:

```
codes/my_website.png
```

## Notes

- Spaces in file names are automatically replaced with `_`
- Existing files with the same name will be overwritten
- Output format is always PNG

## License

Do whatever you want with this project.
