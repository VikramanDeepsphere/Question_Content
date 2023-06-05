import openai
import streamlit as st
import os
openai.api_key = os.environ["API_KEY"]

def generate_response4(message_log):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=3000,
    messages=message_log,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']




