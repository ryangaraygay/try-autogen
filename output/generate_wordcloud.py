# filename: generate_wordcloud.py

import os
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Specify the URL
url = "https://ryangaraygay.com/describe-design-decide-develop-a-framework-for-building-things/"

# Send HTTP request to URL and save the response from server in a response object called r
r = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')

# Extract all text
text = soup.get_text()

# Filter out common words and words that are less than 4 characters long
filtered_words = [word for word in text.split() if word not in stopwords.words('english') and len(word) > 3]

# Create and generate a word cloud image
wordcloud = WordCloud().generate(' '.join(filtered_words))

# Display the generated image using matplotlib
plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# Save the image in the img folder
image_path = "dddd-wordcloud.png"
wordcloud.to_file(image_path)
print(f"Image saved as {image_path}")