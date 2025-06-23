import streamlit as st
import pandas as pd
import pickle
from resume_parser import parse_resume
from utils import clean_text

st.title("📝 Smart Resume Ranker")

# Load trained model
with open('models/ranker_model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

# Load Job Descriptions
jd_df = pd.read_csv('data/job_description.csv')
jd_list = jd_df['description'].tolist()
selected_jd = st.selectbox("Select Job Description", jd_list)

# Upload Resumes
uploaded_files = st.file_uploader("Upload Resumes (.pdf, .docx)", accept_multiple_files=True)

if st.button("Rank Resumes"):
    if not selected_jd or not uploaded_files:
        st.warning("Please select a JD and upload resumes.")
    else:
        jd_clean = clean_text(selected_jd)
        results = []

        for file in uploaded_files:
            with open(f"data/resumes/{file.name}", "wb") as f:
                f.write(file.getbuffer())

            resume_text = parse_resume(f"data/resumes/{file.name}")
            text_clean = clean_text(resume_text)
            combined = jd_clean + " " + text_clean

            X_input = vectorizer.transform([combined])
            score = model.predict(X_input)[0]

            results.append((file.name, score))

        sorted_resumes = sorted(results, key=lambda x: x[1], reverse=True)
        st.success("Resumes Ranked:")
        for res, score in sorted_resumes:
            st.write(f"{res} — Match Score: {score:.2f}")
