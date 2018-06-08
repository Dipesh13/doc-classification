# encoding=utf8
import PyPDF2
import os

# filename = 'Frankenstein.pdf'
def text_ext(filename):
    """
    Function to extract text from pdf and save it in txt format
    :param filename:
    :return:
    """
    dump = ''
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        # print(pageObj.extractText())
        dump += pageObj.extractText()
    with open(filename[0:-4]+'.txt','wb') as fo:
        fo.write(dump.encode('utf-8'))

for (dirname, dirs, files) in os.walk('.'):
    # walk the finance directory or the parent dir to convert pdfs to txts
    for filename in files:
        if filename.endswith('.pdf') :
            thefile = os.path.join(dirname,filename)
            text_ext(thefile)
            print("Finished processing {}".format(thefile))