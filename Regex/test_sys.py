import sys
import re
string_query = sys.argv[1]


#clean word with regex
def clean_word(word):
    cleaned_word = re.sub('[^A-Za-z]+', '', word)
    return cleaned_word

print(clean_word(string_query))