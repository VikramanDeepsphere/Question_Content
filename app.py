import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
import math
from PIL import Image
import source.title_1 as head
import QuestionGeneration.question_gen as ques
import ContentGeneration.content_generation as cont_gen
import os
import openai

openai.api_key = os.environ["API_KEY"]

with open('style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((2,5,3))
with imcol1:
    st.write("")
with imcol2:
    st.image('image/Logo_final.png')
    st.markdown("")
with imcol3:
    st.write("")
#---------Side bar-------#

with st.sidebar:
    selected = st.selectbox("",
                     ['Select Application',"Question Generation","Content Generation"],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Image","Pandas","Openai"],key='text1')
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    GPT_TOOL =  st.selectbox(" ",('Models Used','GPT3 - Davinci','GPT-3.5 Turbo Model'),key='text3')
    st.markdown("## ")
    href = """<form action="#">
            <input type="submit" value="Clear/Reset" />
            </form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    st.markdown("# ")
    st.markdown("<p style='text-align: center; color: White; font-size:18px;'>Powered By<span style='font-weight: bold'></span></p>", unsafe_allow_html=True)
    s1,s2,s3=st.columns((2,3,2))
    with s2:    
        #st.write("")
        st.image("image/Openai.png")
#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == "Select Application":
            head.title()
            st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
        if selected == "Question Generation":
            ques.quens_gen()
        if selected == "Content Generation":
            cont_gen.content_gen()
    except BaseException as error:
        st.error(error)