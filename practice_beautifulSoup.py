# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sentencepiece as spm
import pandas as pd

# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/John_D._Hunter').read()
# Make a soup 
soup = BeautifulSoup(source,'lxml')
# Print
# print(soup)

# Find out what set of elements there are in the soup
# print(set([text.parent.name for text in soup.find_all(text=True)]))

# Extract the plain text content from paragraphs
text = ''
for paragraph in soup.find_all('p'):
    text += paragraph.text
    
# Import package
import re
# Clean text
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')
print(text)



# Final code 📃
# This final code is a slightly different version where script was adjusted to keep paragraph headers as well
# so that there are two available examples to reference for both approaches.
# This may be more useful instead of collating the codes already shown in sections above.

# # ========== 1. Using wikipedia ==========
# # Import packages
# import wikipedia

# # Specify the title of the Wikipedia page
# wiki = wikipedia.page('John D. Hunter')

# # Extract the plain text content of the page, excluding images, tables, and other data.
# text = wiki.content

# # Replace '==' with '' (an empty string)
# text = text.replace('==', '')

# # Replace '\n' (a new line) with '' & end the string at $1000.
# text = text.replace('\n', '')[:-12]
# print(text)

# # ========== 2. Using urllib & BeatifulSoup ==========
# # Import packages
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

# # Specify url of the web page
# source = urlopen('https://en.wikipedia.org/wiki/John_D._Hunter').read()

# # Make a soup 
# soup = BeautifulSoup(source,'lxml')
# soup

# # Extract the plain text content from paragraphs
# paras = []
# for paragraph in soup.find_all('p'):
#     paras.append(str(paragraph.text))

# # Extract text from paragraph headers
# heads = []
# for head in soup.find_all('span', attrs={'mw-headline'}):
#     heads.append(str(head.text))

# # Interleave paragraphs & headers
# text = [val for pair in zip(paras, heads) for val in pair]
# text = ' '.join(text)

# # Drop footnote superscripts in brackets
# text = re.sub(r"\[.*?\]+", '', text)

# # Replace '\n' (a new line) with '' and end the string at $1000.
# text = text.replace('\n', '')[:-11]
# print(text)