# Import `requests`
import requests
from bs4 import BeautifulSoup
# Import nltk
import nltk
# Import RegexpTokenizer from nltk.tokenize
from nltk.tokenize import RegexpTokenizer
#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Figures inline and set visualization style
sns.set()


# Store url
url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'


# Make the request and check object type
r = requests.get(url)
type(r)

# Extract HTML from Response object and print
html = r.text
#print(html)

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html5lib")
print(soup.title.string)

# Get the text out of the soup 
text = soup.get_text()

# Create tokenizer
tokenizer = RegexpTokenizer('\w+')

# Create tokens
tokens = tokenizer.tokenize(text)

# Initialize new list
words = []

# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())

# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')


# Initialize new list
words_ns = []

# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

# Print several list items as sanity check
words_ns[:5]



# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)

