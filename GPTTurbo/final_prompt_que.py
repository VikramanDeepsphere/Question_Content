import openai
import streamlit as st
import os
import GPTTurbo.Turbo35 as GPT_35

def mcq(prompt,serial_no):
    message_log = [{"role": "system", "content": "You are a helpful assistant for Multiple choice question generater "},
    {"role": "user", "content": "Generate 2 multiple choice questions with answers for below content with Question Number [1,2]:" "Data Preparation can be a procedure for collecting data from a single source or different sources, filtering the unwanted fields and content, which can also be termed as cleaning the data and compiling them into a file for further processing. Data Preparation is the preliminary and essential step since it is the stepping stone for data to further analysis. It is used for proper business data analysis. This Data Preparation is a step that starts before processing and analyzing the data. Data exploration is known as data exploration, such as its structure, counts, values,relationships between variables and more. Moreover, it brings out various insights and information.This process is usually done by data analysts using various visualization tools and languages like Python or R Programming. Therefore, it can be seen as a skill to prepare data ideally using multiple methodologies and bring out perfect insights."},
    {"role": "assistant","content":'''1. What is the step that comes before Data Preparation?
        A. Data exploration
        B. Data processing
        C. Data analysis
        D. None of the above
    Answer: A. Data exploration
    2. What is a skill required to prepare data ideally?
        A. Data exploration
        B. Data processing
        C. Data analysis
        D. Multiple methodologies
    Answer: D. Multiple methodologies'''},
    {"role": "user", "content": " Generate 5 multiple choice questions with answers for below content with serial numbers"+str(serial_no)+":"+prompt}]
    return GPT_35.generate_response4(message_log)

def fillup(prompt,serial_no):
    message_log = [
    {"role": "system", "content": "You are a helpful assistant for fill in the blanks question generater"},
    {"role": "user", "content": """Generate 2 fill in the blanks questions with answer as blank space for below content with Question Number [1,2]:'Data comes in from various sources: SAP, Oracle, Microsoft, Excel, CSV, ERP, and CRM systems,and anything in the structured, unstructured, and semi-structured forms. These data fromvarious data sources have to be collected (Extraction), prepared (Transformation), and Loaded(Loading) into the target systems.Overall we are making the data available for the next level of processing.'"""},
    {"role": "assistant",
     "content":'''1: Data comes in from various sources such as SAP, Oracle, Microsoft, Excel, CSV, ERP, and CRM systems, and anything in the _________, unstructured, and semi-structured forms.
        Answer: Structured

                2: The data from various data sources have to be collected (Extraction), prepared (Transformation), and Loaded (Loading) into the ___________ systems.
        Answer: Target''' },

    {"role": "user", "content": " Generate 5 fill in the blanks questions with answers as blank space for below content with serial numbers"+str(serial_no)+" : "+prompt} ]
    return GPT_35.generate_response4(message_log)


def trf(prompt,serial_no):
    message_log = [{"role": "system", "content": "You are a helpful assistant for true or false question generater"},
    {"role": "user", "content": """Generate 5 True or False questions with answers for below content with Question Number [1,2,3,4,5]: 'Data science pipelines help in this regard by making it easy for the data engineers and data scientists to create and deploy the applications quickly. This helps the business to make informed decisions faster.In summary, a data science pipeline is a set of stages that convert raw data into meaningful insights that can be used to make data-driven decisions. It involves data collection, cleaning, representation, and analysis, and helps businesses to save time and resources while making informed decisions.'"""},
    {"role": "assistant", 
     "content":'''1. The data is utilized for machine learning modelling - True
                2. Data Science pipeline not helps businesses make data-driven decisions efficiently and quickly - False
                3. The models are trained, tested and validated before deployment - True
                4. Data Science pipeline enables Smooth management of data engineering tasks - False
                5. Data science pipelines save adequate time by mitigating the error-prone task of conventional data collection - True''' },
    {"role": "user", "content": " generate 5 True or False questions with answers for below content with serial numbers"+str(serial_no)+" : " +prompt}]
    return GPT_35.generate_response4(message_log)


def matc(prompt):
    message_log = [{"role": "system", "content": "You are a helpful assistant for generating Match the following below content "},
    {"role": "user", "content": """Generate set of Match the follwing questions with answers for below content :'Data science pipelines help in this regard by making it easy for the data engineers and data scientists to create and deploy the applications quickly. This helps the business to make informed decisions faster. In summary, a data science pipeline is a set of stages that convert raw data into meaningful insights that can be used to make data-driven decisions. It involves data collection, cleaning, representation, and analysis, and helps businesses to save time and resources while making informed decisions.'"""},
    {"role": "assistant", 
     "content":'''
                1. Data Science pipeline - a) Extracting insights from data
                2. Machine Learning modelling - b) Series of methods or techniques
                3. Data Engineering tasks - c) Input for learning patterns
                4. Real time analysis - d) Data gathering, cleaning and representing
                5. Data Visualization - e) Deployed into production systems
                Answer : [1-b, 2-c, 3-d, 4-e, 5-a]
                '''
    },
    {"role": "user", "content": "generate 5 Match the following questions with answers for below content"+ " : "  +prompt}]
    return GPT_35.generate_response4(message_log)