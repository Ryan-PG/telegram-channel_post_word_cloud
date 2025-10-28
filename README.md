# Telegram Channel Post Word Cloud

Generate a Persian word cloud from a folder of HTML files (e.g., Telegram exports). Text is extracted from `div.text` elements, Persian shaping/bidi is handled, stopwords are removed, and the result is shown via Matplotlib.

## Overview
- Parses all HTML files in a target directory.
- Extracts text from `<div class="text">` blocks.
- Applies Persian reshaping and bidi fix.
- Removes custom stopwords (one per line).
- Builds and displays a word cloud.

## Export From Telegram
- Use Telegram Desktop for exporting chat/channel history.
- Open the target chat/channel, then:
  - Option A: Chat menu (three dots) > "Export chat history…"
  - Option B: Settings > Advanced > Export Telegram Data > "Export chat history"
- Choose the chat/channel, set Format to "HTML". Media is optional (this script only needs HTML).
- Pick an export location and start the export. When finished, click "Show Data".
- Telegram creates a folder (e.g., `ChatName/`) containing `messages.html` and, for large chats, `messages2.html`, `messages3.html`, etc. Only the `.html` files are needed.

## Requirements
- Python 3.9+
- Packages: see `requirements.txt` (`beautifulsoup4`, `arabic-reshaper`, `python-bidi`, `wordcloud`, `matplotlib`)
- Font file for Persian characters: `IRANSans_Bold.ttf` (included)
- Stopwords file: `persianST.txt` (you provide)

## Install
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

## Prepare Inputs
1) Copy the exported Telegram folder (e.g., `ChatName/`) into this repository.
- It should contain `messages.html` and possibly `messages2.html`, etc.

2) Point the script to this folder:
- Option A: Rename the exported folder to `mahdi` (matches the default `html_files_directory_path = "./mahdi"`).
- Option B: Edit `html_files_directory_path` in `main.py` to your exported folder name, e.g., `"./ChatName"`.

3) Create a stopwords file at the repo root named `persianST.txt`.
- One word per line (UTF-8). Example:
  ```
  اینکه
  برای
  باشد
  ```

4) Ensure the font file exists at the repo root as `IRANSans_Bold.ttf`.
- The repo already includes this file. If you replace it, update the path accordingly.

## Configure (optional)
- Target HTML folder: edit `html_files_directory_path` in `main.py:13` to match your folder name, e.g. `"./mahdi"`.
- Stopwords path: edit `stopwords_file_path` in `main.py:14` if you use a different filename or location.
- Font path: edit `font_path` in `main.py:15` if you change the font file.

## Run
```bash
python main.py
```
- A window with the word cloud appears (`plt.show()`).
- The script scans all `.html` files in the target folder and extracts text from `<div class="text">` blocks.

## Save Image (optional)
If you prefer saving instead of displaying, add a save call after plotting in `main.py` (around `main.py:70-75`):
```python
plt.savefig("wordcloud.png", dpi=300, bbox_inches="tight")
```

## Expected Layout
```
.
├─ IRANSans_Bold.ttf
├─ persianST.txt              # you create
├─ main.py
└─ mahdi\                     # or any folder name you set
   ├─ page1.html
   └─ page2.html
```

## Notes & Troubleshooting
- File not found errors:
  - `persianST.txt` must exist at the path in `main.py:14`.
  - `IRANSans_Bold.ttf` must exist at the path in `main.py:15`.
- No words or small cloud: check that your HTML contains `<div class="text">` content and that stopwords aren’t overly aggressive.
- Headless environments: `plt.show()` may not work without a display. Use the save approach above and run without showing the plot.
