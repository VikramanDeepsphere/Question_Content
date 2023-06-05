import os
import time
import comtypes.client


def convertFiletoPDF(file):
    wdFormatPDF = 17
    in_file = os.path.abspath(file)
    out_file = os.path.abspath(file.replace(".docx", ".pdf"))
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = True
    time.sleep(3)
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()