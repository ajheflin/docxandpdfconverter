import docx

class DocxObj:
	def __init__(self, filename):
		self.filename = filename
	def getText(self):
    		doc = docx.Document(self.filename)
    		fullText = []
    		for para in doc.paragraphs:
        		fullText.append(para.text)
    		return '\n'.join(fullText)
