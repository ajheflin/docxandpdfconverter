import PyPDF2

class PDF:
	def __init__(self, filename):
		self.filename = filename
	def getText(self):
    		pdfFileObj = open(self.filename, 'rb')
    		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    		fulltext = ""
    		for page in range(pdfReader.numPages):
        		pageObj = pdfReader.getPage(page)
        		fulltext += pageObj.extractText() + '\n'
    		pdfFileObj.close()
    		return fulltext
