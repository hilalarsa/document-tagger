import pytesseract
# import nltk
# import difflib

import re

# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stopper
# factoryRemover = StopWordRemoverFactory()
# stopword = factoryRemover.create_stop_word_remover()

# create stemmer
# factoryStemmer = StemmerFactory()
# stemmer = factoryStemmer.create_stemmer()


def image_to_text(filePath):
    # tesseract run on subject
    text = pytesseract.image_to_string(filePath, lang='ind')
    return text


# tokenize text into sentences
# sentences = nltk.sent_tokenize(text)

# print sentences[0]
# GRAVEYARD
# split sentence into individual word
# arrayFull = []
# for i, sentence in enumerate(sentences):
#     # replace enter (\n) with space
#     resultNoEnter = re.sub('\n', ' ', sentence)
#     # replace tabs and multiple spaces with single space
#     resultNoTab = re.sub(' +', ' ', resultNoEnter)
#     # change text encoding to utf8
#     encodedText = resultNoTab.encode("utf-8")
#     print  str(i) + ". " + encodedText
    # words = encodedText.split()
    # arrayFull = arrayFull + encodedText
    # print words
    # three = [' '.join([i,j,k]) for i,j,k in zip(words, words[1:], words[2:])]
    # print difflib.get_close_matches('putra', words, cutoff=0.9)

# print arrayFull