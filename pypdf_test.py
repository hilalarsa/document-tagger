
# importing required modules 
import PyPDF2 
import nltk

  
# creating a pdf file object 
pdfFileObj = open('sample_pdf3.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
# print(pageObj.extractText()) 

sentences = nltk.sent_tokenize(pageObj.extractText())
for sentence in sentences:
    # print(sentence)
    words = nltk.word_tokenize(sentence)
    print words
    # for word in words:
        # print(word)
  
# closing the pdf file object 
pdfFileObj.close() 
