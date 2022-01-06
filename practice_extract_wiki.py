# https://levelup.gitconnected.com/two-simple-ways-to-scrape-text-from-wikipedia-in-python-9ce07426579b


# Use beautifulSoup



# Import package
import wikipedia
# Specify the title of the Wikipedia page
wiki = wikipedia.page('John D. Hunter')
# Extract the plain text content of the page
text = wiki.content
print(text)

##############################################

# Import package
import re
# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')
print(text)


# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup