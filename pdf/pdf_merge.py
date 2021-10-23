import PyPDF2 as PDFManger
import  os

merger = PDFManger.PdfFileMerger()

docuList = []
for x in os.listdir():
    if x.endswith(".pdf"):
        docuList.append(x)

for pdf in docuList:
    merger.append(open(pdf,'rb'))

with open("mergedFiles.pdf","wb") as out:
    merger.write(out)


