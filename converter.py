import docxobj
import pdf

filename = input("Enter a filename: ")

fileExtension = list(filename.split("."))[1]

fileObj = None

if fileExtension == "docx":
    fileObj = docxobj.DocxObj(filename)
elif fileExtension == "pdf":
    fileObj = pdf.PDF(filename)

print(fileObj.getText())
