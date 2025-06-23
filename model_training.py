import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from utils import clean_text

# Load labeled dataset
df = pd.read_csv('data/resume_jd_match.csv')

# Preprocess text columns
df['resume_text'] = df['resume_text'].apply(clean_text)
df['job_description_text'] = df['job_description_text'].apply(clean_text)
df['combined'] = df['resume_text'] + " " + df['job_description_text']

# Convert continuous scores to binary labels (1 = Good Match, 0 = Poor Match)
df['match_score'] = df['match_score'].apply(lambda x: 1 if x >= 0.5 else 0)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['combined'])
y = df['match_score']

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# Save vectorizer and model
with open('models/ranker_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)

print("✅ Model trained and saved to 'models/ranker_model.pkl'")
