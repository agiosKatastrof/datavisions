import PyPDF2
f = open('../../data/covid19/03-07-2020.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(f) 
pageObj = pdfReader.getPage(2) 
print(pageObj.extractText()) 
f.close()


