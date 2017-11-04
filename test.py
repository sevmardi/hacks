import PyPDF2
pdf = open("ml/datasets/mmds_book.pdf", 'rb')


reader = PyPDF2.PdfFileReader(pdf)


print(reader.numPages)