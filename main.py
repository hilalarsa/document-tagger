import pytesseract
import nltk
import difflib

import re

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stopper
factoryRemover = StopWordRemoverFactory()
stopword = factoryRemover.create_stop_word_remover()

# create stemmer (disabled, not necessary)
# factoryStemmer = StemmerFactory()
# stemmer = factoryStemmer.create_stemmer()

# tesseract run on subject
rawText = pytesseract.image_to_string('./contoh 2 surat tugas.jpeg', lang='ind')

# tokenize text into sentences
sentences = nltk.sent_tokenize(rawText)

# GRAVEYARD
# split sentence into individual word
fullWords = []
for i, sentence in enumerate(sentences):
    # change all text to lowercase
    resultLowerCase = sentence.lower()
    # replace enter (\n) with space
    resultNoEnter = re.sub('\n', ' ', resultLowerCase)
    # replace tabs and multiple spaces with single space
    resultNoTab = re.sub(' +', ' ', resultNoEnter)
    # change text encoding to utf8
    encodedText = resultNoTab.encode("utf-8")
    # # apply Sastrawi stopper removal
    # endText = stopword.remove(encodedText)

    word = encodedText.split()
    fullWords = fullWords + word
    # print words
    # three = [' '.join([i,j,k]) for i,j,k in zip(words, words[1:], words[2:])]

# print fullWords
# print difflib.get_close_matches('putra', 'putra', cutoff=0.9)
# print difflib.SequenceMatcher(a='putra', b='putr').ratio()
dictFromApi = ['putra prima arhandi', 'luqman affandi', 'dimas wahyu wibowo']


for word in fullWords:
    matches = difflib.get_close_matches(word, dictFromApi, n=3, cutoff=0.1)
    print(matches)
    # if(item)
    # print item +"\n"
# for 