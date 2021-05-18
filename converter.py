import docxobj
import pdf

class Converter:
	def __init__(self, filename):
		fileExtension = list(filename.split('.'))[1]
		if fileExtension == "docx":
			self.fileObj = docxobj.DocxObj(filename)
		elif fileExtension == "pdf":
			self.fileObj = pdf.PDF(filename)
	def getText(self):
		return self.fileObj.getText()
