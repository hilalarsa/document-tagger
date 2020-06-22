
# importing required modules 
from PyPDF2 import PdfFileReader
import nltk


def pdf_to_text(filePath, filename):
    # creating a pdf file object 
    # print(result)
    pdfFileObj = open(filePath, 'rb') 
    # creating a pdf reader object 
    pdfReader = PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file 

    # creating a page object 
    pageObj = pdfReader.getPage(1) 

    # extracting text from page 
    # print(pageObj.extractText()) 
    # sentences = nltk.sent_tokenize(pageObj.extractText())
    # for sentence in sentences:
        # print(sentence)
        # words = nltk.word_tokenize(sentence)
        # print words
        # for word in words:
            # print(word)

    # closing the pdf file object 
    # print(pageObj.extractText())
    result = pageObj.extractText()

    # return function value
    return result
    pdfFileObj.close()


