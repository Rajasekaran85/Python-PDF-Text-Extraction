import sys
import os
import PyPDF2


print("\n PDF Text Extraction \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 28 May 2022 \n\n")


filepath1 = input(" Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath) # specified path is an existing directory or not

for fname in os.listdir(filepath):
    if not fname.endswith(".pdf"):
        continue
    path = os.path.join(filepath, fname) 
    pdfobj = open(path, 'rb')
    pdfread = PyPDF2.PdfFileReader(pdfobj)
    test = os.path.splitext(fname)[0]
    print(fname)
    txtname = filepath + test + ".txt"
    if os.path.exists(txtname):
        os.remove(txtname)
    x = pdfread.numPages
    for i in range(x):
        pageObj = pdfread.getPage(i) 
        with open(txtname, 'a+', encoding="utf-8") as f: 
            f.write((pageObj.extractText()))
    pdfobj.close()
print("Process Completed")
