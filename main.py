import pytesseract
import nltk
import difflib
import json

import sys
import re
import os

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# from external file
from tesseract_ocr import image_to_text
from pypdf_test import pdf_to_text
from difflib_checker import text_matcher, get_document_type
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
# raw_text = textTransform("../sample/s_tugas1.jpeg")
raw_text = textTransform("../sample/lembarpengesahan1.jpeg")
# raw_text = textTransform(sys.argv[1])
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

dataDosen = get_data('dosen')
dataJudul = get_data('judul')
# print(dataJudul)

# sample
# dataDosen = ['ahmadi yuli ananta','ariadi retno tri hayati ririd','arief prasetyo','banni satria andoko','budi harijanto','cahya rahmad','deddy kusbianto purwoko aji','dimas wahyu wibowo''dwi puspitasari','dyah ayu irawati','ekojono','ely setyo astuti','erfan rohadi','faisal rahutomo','gunawan budiprasetyo','hendra pradibta','imam fahrur rozi','indra dharma wijaya','luqman affandi', 'nurudin santoso','putra prima arhandi','rawansyah','ridwan rismanto','rosa andrie asmara','siti romlah','ulla defana rosiani','yan watequlis syaifudin']
# dataJudul = ['surat tugas', 'lembar pengesahan']

# print dataDosen

# check document type
document_type_matched_array = []
for item in dataJudul:
    trigger_word_array = item['trigger_word'].split(', ') # get trigger word, split by comma and space to get its array form
    for trigger_word in trigger_word_array: 
        a = text_matcher(full_words, trigger_word)
        if a is not None:
            # document_type_matched_array = get_document_type_matched_array(a['text'], item) # get da doc type by checking trigger word with outputted text from difflib checker
            # document_type_matched_array += a['text'] + ', '
            document_type_matched_array.append(item['tipe_judul']) # save tipe judul as doc type ONLY IF text matcher showing FIRST RESULT (FLAW)
            break
        else:
            continue
    # if(document_type_matched_array != ''): # check only on first match, next metch no matter (FLAW)
        # break

# NOTE : if on surat tugas / surat keputusan / surat pengangkatan => document_type_matched_array will have more than 1 content

# check dosen amount, cz sometime dosen amount matters
dosenAmount = 0
nama_dosen = []
for item in dataDosen:
    a = text_matcher(full_words, item["nama_dosen"])
    if a is not None:
        nama_dosen.append(a)
        dosenAmount = dosenAmount + 1

print(document_type_matched_array)
document_type = ''
for item in dataJudul:
    for doc_type in document_type_matched_array: # break document_type_matched_array array and check if inside got is_multiple = true (means dosen amount is matter, and bobot is applied differently)
        if(item['tipe_judul'] == doc_type and item['is_multiple'] == "true" and dosenAmount > 1): # tipe_judul in loop is same as breaked array of matched doc_type PLUS nama dosen in document is more than 1
            # do something here with pembobotan for doc that has dosen > 1
            print("HEY BOI")
            document_type = item['tipe_judul']

if(document_type == ''): # if no dosen or dosen only 1 name in doc, apply first array value
    document_type = document_type_matched_array[0] # if dosen amount doesnt matter, array will ALWAYS has 1 index, so just get the 1st value in the array as legit doc type
print(document_type)

# get real doc type
# for item in dataJudul:
    # document_type = get_document_type(a['text'], item)

# print(document_type)
print(nama_dosen)
print(dosenAmount)
# print(document_type)
# TODO
# if certain document type is selected, dosen amount will matter, other than that, it wont 
# Start of Rule base method
# if(dosenAmount <= 1):        
    # document_type = "surat tugas individu"
# elif(dosenAmount > 1):
    # document_type = "surat tugas kelompok"


# JUDUL
# for item in dataJudul:
    # triggerWord = item['trigger_word']
    # print(triggerWord)
    # print(text_matcher(full_words, item['trigger_word'])) # text_matcher(sourceWord, testedWord):


# check document extension (V)
# check dosen name, and name occurance
# check document type
# check rest info