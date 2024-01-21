import streamlit as st
import google.generativeai as genai
import os
import Pypdf2 as pdf


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_ley=os.getenv("GOOGLE_API_KEY"))


## gemini pro response

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(upload_file):
    reader=pdf.PdfReader(upload_file)
    text=""
    for page in reader(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

input_prompt=
f"""
Context:
You will act like an ATN (Application tracking system) system expertwith deep understanding
of tech field, software, data science, big data. Your task is to evaluate the resume based
on the given description.
You must consider that the job market is very competitive and you provide best assistancefor improving resume.



Job Description {jd}: [Provide the full job description text here.]
Applicant Resume {text}: [Provide the full applicant resume text here.]
Task:

Score: Generate a score between 0-100 indicating the overall match between the applicant's skills and experience as described in the resume and the requirements and qualifications listed in the job description.
Missing Keywords: Identify a list of relevant keywords from the job description that are missing from the applicant's resume. These keywords should be specific to the skills and experience required for the role.
Feedback Summary: Provide a concise and informative summary of the key areas where the applicant's resume aligns with the job description and areas where improvements can be made to increase their score and chances of landing an interview. This summary should be actionable and highlight specific suggestions for the applicant to enhance their resume.

"""

# streamlit app 

st.title("Jobkit")
st.text("Beat the ATS")
jd=st.text_area("Paste your job description")
uploaded_file=st.f