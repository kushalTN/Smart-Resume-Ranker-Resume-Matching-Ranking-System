import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)
