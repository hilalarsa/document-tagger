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
from api import get_data

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
raw_text = textTransform("../sample/s_tugas1.jpeg")
# raw_text = textTransform("../sample_pdf3.pdf")
# raw_text = textTransform("../server/dosen.js")

# tokenize text into sentences
sentences = nltk.sent_tokenize(raw_text)

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

# text ready to be compared with database
# print(full_words)

# dataDosen = get_data('dosen')
# dataJudul = get_data('judul')

# sample
dataDosen = ['ahmadi yuli ananta','ariadi retno tri hayati ririd','arief prasetyo','banni satria andoko','budi harijanto','cahya rahmad','deddy kusbianto purwoko aji','dimas wahyu wibowo''dwi puspitasari','dyah ayu irawati','ekojono','ely setyo astuti','erfan rohadi','faisal rahutomo','gunawan budiprasetyo','hendra pradibta','imam fahrur rozi','indra dharma wijaya','luqman affandi', 'nurudin santoso','putra prima arhandi','rawansyah','ridwan rismanto','rosa andrie asmara','siti romlah','ulla defana rosiani','yan watequlis syaifudin']
dataJudul = ['surat tugas', 'lembar pengesahan']

# print dataDosen

nama_dosen = []
document_type = ''
occuranceCounter = 0
for item in dataDosen:
    a = text_matcher(full_words, item)
    if a is not None:
        nama_dosen.append(a)
        occuranceCounter = occuranceCounter + 1

for item in dataJudul:
    a = text_matcher(full_words, item)
    if a is not None:
        document_type = a['text']

# Start of Rule base method
if(occuranceCounter <= 1):
    document_type = "surat tugas individu"
elif(occuranceCounter > 1):
    document_type = "surat tugas kelompok"

print(nama_dosen)
print(document_type)

# JUDUL
# for item in dataJudul:
    # triggerWord = item['trigger_word']
    # print(triggerWord)
    # print(text_matcher(full_words, item['trigger_word'])) # text_matcher(sourceWord, testedWord):


# check document extension (V)
# check dosen name, and name occurance
# check document type
# check rest info