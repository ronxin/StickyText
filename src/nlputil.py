import re
import nltk
from nltk.corpus import stopwords
def remove_punctuation_from_words(words):
    # retain only those tokens that have at least a letter or number
    nonPunct = re.compile('.*[A-Za-z0-9].*')
    return [w for w in words if nonPunct.match(w.text)]

def remove_stopwords(words):
    return [w for w in words if not w.text.lower() in stopwords.words("english")]

# Note: plain word texts are returned instead of Word objects
_stemmer = nltk.PorterStemmer()
def stem_lower_words(words):
    return [_stemmer.stem(w.text.lower()) for w in words]
