# Smart-Resume-Ranker-Resume-Matching-Ranking-System

**Description:**
Smart Resume Ranker is an AI-powered platform designed to automate resume screening and candidate shortlisting. Using advanced Natural Language Processing (NLP) and Machine Learning (ML) techniques, it compares candidate resumes against job descriptions to calculate match scores and ranks applicants based on relevance. This system helps recruiters quickly identify the best-fit candidates, saving time and improving hiring accuracy.

**Key Features:**
✔️ AI-Powered Resume Matching
✔️ Intelligent Candidate Ranking based on Job Fit
✔️ Supports PDF and DOCX Resume Uploads
✔️ Real-Time Match Score Generation
✔️ User-Friendly Streamlit Interface

---

🛠️ Tech Stack
Python

Streamlit (Frontend)

Natural Language Processing (NLP)

Scikit-learn, Pandas, Numpy

Preprocessing Libraries (NLTK, SpaCy)

Resume Parsing Techniques

📂 Project Structure
bash
Copy
Edit
├── app.py                   # Streamlit Frontend Application
├── resume_data.csv          # Sample Resume Dataset
├── job_description.csv      # Job Descriptions for Matching
├── resume_jd_match.csv      # Output: Resume & JD Match Scores
├── utils.py                 # Helper Functions for Preprocessing
├── requirements.txt         # Project Dependencies
└── README.md                # Project Documentation
🚀 How to Run the Project
1.cd path/to/smart_resume_ranker
2.python -m venv venv
3..\venv\Scripts\Activate
4.Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
5.pip install -r requirements.txt
6.python model_training.py
7.D:\smart_resume_ranker\data\resumes
8.streamlit run app.py

📊 How it Works
Upload candidate resumes and job descriptions.

The system preprocesses both texts using NLP techniques.

Calculates similarity scores using TF-IDF and ML models.

Ranks resumes based on how well they match the job requirements.

Displays ranked candidates with real-time scores in the Streamlit interface.

🎯 Benefits
✔️ Speeds up Resume Screening
✔️ Reduces Manual Shortlisting Errors
✔️ Provides Data-Driven Candidate Rankings
✔️ Enhances Recruitment Efficiency

💡 Future Enhancements
Add Deep Learning models like BERT for better matching accuracy

Support additional file formats

Integrate with ATS or external databases

Visual Analytics for Recruiters


