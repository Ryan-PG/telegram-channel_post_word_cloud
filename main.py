import os
from bs4 import BeautifulSoup
import re
import arabic_reshaper
from bidi.algorithm import get_display
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Paths
# html_files_directory_path = "./html_files"
# html_files_directory_path = "./ali"
# html_files_directory_path = "./mmd"
html_files_directory_path = "./mahdi"
stopwords_file_path = "persianST.txt"
font_path = "IRANSans_Bold.ttf"

# Check if necessary files exist
if not os.path.exists(stopwords_file_path):
    raise FileNotFoundError(f"Stopwords file not found: {stopwords_file_path}")
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found: {font_path}")

# Load stopwords
with open(stopwords_file_path, "r", encoding="utf-8") as file:
    stop_words = set(file.read().splitlines())

# Get list of HTML files
files = sorted(os.listdir(html_files_directory_path))
html_files = [
    file for file in files if os.path.isfile(os.path.join(html_files_directory_path, file))
]

# Initialize a variable to hold all combined text
all_combined_text = ""

# Process each HTML file
for html_file in html_files:
    file_path = os.path.join(html_files_directory_path, html_file)
    
    # Read and parse HTML
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    # Extract and clean text
    texts = [div.get_text(strip=True) for div in soup.find_all("div", class_="text")]
    combined_text = " ".join(texts)
    cleaned_text = re.sub(r"[^آ-ی۰-۹a-zA-Z ]", " ", combined_text)
    
    # Append to all_combined_text
    all_combined_text += " " + cleaned_text

# Persian text reshaping and bidirectional handling
reshaped_text = arabic_reshaper.reshape(all_combined_text)
bidi_text = get_display(reshaped_text)

# Ensure bidi_text is explicitly a string and remove stopwords
filtered_text = " ".join(
    word for word in str(bidi_text).split() if word not in stop_words and len(word) >= 4
)

# Generate word cloud for all pages
wordcloud = WordCloud(
    font_path=font_path,
    width=800,
    height=400,
    background_color="white",
    max_words=150,
).generate(filtered_text)

# Plot the combined word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud for All Pages")
plt.show()
