# Allows for a list to be created of ebooks in a folder.
# Books need to be PDF.
# List will contain name and number of pages in the end.

from os import listdir
import PyPDF2


class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


myPath = "F:/Books/"
readFileList = listdir(myPath)
bookList = []
ignoreSuffix = [".py", ".bat", ".txt"]

# Remove all unwanted items
for suf in ignoreSuffix:
    for item in readFileList:
        if item.endswith(suf):
            readFileList.remove(item)

# Fix names of the files
for i in range(0, len(readFileList)):
    readFileList[i] = readFileList[i].removesuffix(".pdf")

# Create list of books
for name in readFileList:
    pdfFile = open(myPath + name + ".pdf", "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    nrOfPages = len(pdfReader.pages)
    bookList.append(Book(name, nrOfPages))

# Create list of books text file
try:
    with open(myPath + "list.txt", "w") as f:
        for book in bookList:
            bookStr = book.name + " " + str(book.pages) + "\n"
            f.write(bookStr)
except FileNotFoundError:
    print("The 'docs' directory does not exist")
