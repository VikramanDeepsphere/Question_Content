
def txt_file(txt_content,vAR_input_quetype,serial_no):
    if vAR_input_quetype == "Fill in the blanks":
        fillup_f = open("QuestionGeneration/prompt_fillup.txt", "r")
        fill=fillup_f.read()
        return fill+"\n Generate 5 fill in the blanks questions with answers as blank space for below content with Question Numbers"+str(serial_no)+":"+'"'+txt_content+'"'
    if vAR_input_quetype == "Multiple choices":
        multi_f = open("QuestionGeneration/prompt_mcq.txt", "r")
        multi=multi_f.read()
        return multi+"\n Generate 5 multiple choice questions with answers for below content with Question Numbers"+str(serial_no)+":" +'"'+txt_content+'"'
    if vAR_input_quetype == "True or False":
        torf_f = open("QuestionGeneration/prompt_trf.txt", "r")
        trfa=torf_f.read()
        return trfa+"\n Generate 5 True or False questions with answers for below content with Question Numbers"+str(serial_no)+":" +'"'+txt_content+'"'
    if vAR_input_quetype == "Match the following":
        mtf_f = open("QuestionGeneration/prompt_match.txt", "r")
        mtf=mtf_f.read()
        return mtf+"\n Generate 5 Match the follwing question with answers list for below content :" +"'"+txt_content+"'"
