# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.
# It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.


from pypdf import PdfWriter

path = PdfWriter()
# noofpages = len(path.pages)
# print(noofpages)
# page = path.pages[0]
# text = page.extract_text()
for pdf in [
    "/home/priyam/Downloads/RESUME.pdf",
    "/home/priyam/Downloads/Mozilla-Recovery-Key_2025-09-11_priyamsaini241178@gmail.com.pdf",
]:
    path.append(pdf)
path.write("/home/priyam/Downloads/result.pdf")
