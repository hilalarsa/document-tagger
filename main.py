import pytesseract
import nltk
import difflib
import json

import re
import os

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# from external file
from tesseract_ocr import image_to_text
from pypdf_test import pdf_to_text
from difflib_checker import text_matcher
from api_test import get_data

# receive filepath, filter to either pdf or image
def textTransform(filePath):
    filename, file_extension = os.path.splitext(filePath)
    if(file_extension == ".jpeg" or file_extension == ".jpg" or file_extension == ".png" or file_extension == ".pbm" or file_extension == ".bmp" ):
        # Format Image
        transformed_text = image_to_text(filePath)
        return(transformed_text)
    elif (file_extension == ".pdf" ):
        # Format PDF
        transformed_text = pdf_to_text(filePath)
        return(transformed_text)
    else:
        print("Format Unrecognized. Aborting ...")

# create stopper
# factoryRemover = StopWordRemoverFactory()
# stopword = factoryRemover.create_stop_word_remover()

# create stemmer (disabled, not necessary)
# factoryStemmer = StemmerFactory()
# stemmer = factoryStemmer.create_stemmer()

# tesseract run on subject to raw text
# rawText = pytesseract.image_to_string('./contoh 2 surat tugas.jpeg', lang='ind')
# raw_text = pytesseract.image_to_string('../sample/lembarpengesahan1.jpeg', lang='ind')
raw_text = textTransform("../sample/lembarpengesahan1.jpeg")
raw_text = textTransform("../sample_pdf3.pdf")
raw_text = textTransform("../server/dosen.js")

# tokenize text into sentences
sentences = nltk.sent_tokenize(raw_text)

print(sentences)


# split sentence into individual word
full_words = []
for i, sentence in enumerate(sentences):
    # change all text to lowercase
    resultLowerCase = sentence.lower()
    # replace enter (\n) with space
    resultNoEnter = re.sub('\n', ' ', resultLowerCase)
    # replace tabs and multiple spaces with single space
    resultNoTab = re.sub(' +', ' ', resultNoEnter)
    # change text encoding to utf8
    encodedText = resultNoTab
    # encodedText = resultNoTab.encode("utf-8")
    # # apply Sastrawi stopper removal
    # endText = stopword.remove(encodedText)

    word = encodedText.split()
    full_words = full_words + word
    # print words

# print(full_words)







# dataDosen = get_data('dosen')
dataJudul = get_data('judul')
# print(dataDosen)
# print(dataJudul)
dataFromApi = ['putra prima arhandi', 'luqman affandi', 'dimas wahyu wibowo']
for item in dataJudul:
    triggerWord = item['trigger_word']
    # print(triggerWord)
    # print(text_matcher(full_words, item['trigger_word'])) # text_matcher(sourceWord, testedWord):


# check document extension
# check dosen name, and name occurance
# check document type
# check rest info