
import os
def fullstr(pdf_content):
    with open("Result/newfile.txt","w", encoding='utf-8') as fill_pmt:
        fill_pmt.write(str(pdf_content))
    b=[]
    with open("Result/newfile.txt","r", encoding='utf-8') as r_txt:
        whole=r_txt.read()
        r_txt.seek(0)
        if len(whole) > 3000:
            for i in range(len(whole)//3000):
                a=r_txt.read(3000)
                if len(a)>100:
                    b.append(a)
        else:
            b.append(whole)
    return b





