# Bulk Image Renamer

A tiny Python utility that renames every image in a folder with a custom prefix — useful when you need clean, link-friendly filenames in one pass instead of renaming files by hand.

## How it works

Point it at an `IMAGES/` folder, enter a prefix, and it walks the folder renaming each file to `<prefix><suffix>`. The string slice in `main.py` controls which part of the original name is kept — edit it to match your naming scheme.

## Usage

```bash
# Put your images in a folder named IMAGES/ next to main.py
python main.py
# Enter the prefix when prompted (no spaces if you'll use the names as links)
```

> **Note:** renaming happens in place. Run it on a copy first to confirm the output names are what you expect.

## Build a standalone executable (optional)

A [PyInstaller](https://pyinstaller.org/) spec is included:

```bash
pip install pyinstaller
pyinstaller main.spec
```

## License

[MIT](LICENSE)
