import pytesseract
import nltk
import difflib

import re

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stopper
factoryRemover = StopWordRemoverFactory()
stopword = factoryRemover.create_stop_word_remover()

# create stemmer
factoryStemmer = StemmerFactory()
stemmer = factoryStemmer.create_stemmer()

# tesseract run on subject
text = pytesseract.image_to_string('./contoh 2 surat tugas.jpeg', lang='ind')
# print(text)

sentences = nltk.sent_tokenize(text)
# print(sentences)
arrayFull = []
for i, sentence in enumerate(sentences):
    # stopResult = stopword.remove(sentence).split();
    result = re.sub('\n', ' ', sentence)
    result2 = re.sub(' +', ' ', result)
    result3 = result2.encode("utf-8")
    # print(result2)
    # text = "Here is the text we are trying to match across to find the three word sequence n0 inf0rmation available I wonder if we will find it?"    
    words = result3.split()
    arrayFull = arrayFull + words
    
    # three = [' '.join([i,j,k]) for i,j,k in zip(words, words[1:], words[2:])]
    # print difflib.get_close_matches('no information available', three, cutoff=0.9)
print(arrayFull)