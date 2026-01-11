# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
import pypdf 
# to list all classes in pypdf module
# print(dir(pypdf))

import os

# Creating an object of PdfWriter class
merger = pypdf.PdfWriter()

# listing files that ends with .pdf and converting filter object into list
files = list(filter(lambda file: True if file.endswith(".pdf") else False, os.listdir()))
# OR listing file using list comprehension
# files = [file for file in os.listdir() if file.endswith(".pdf")]
# print(files)

# merging 
for pdf in files:
    merger.append(pdf)
    
# Naming the merged pdf files
merger.write("merged-file.pdf")

# Closing the merger object
merger.close()

# To merge in a specific order, sort the files name list accordingly