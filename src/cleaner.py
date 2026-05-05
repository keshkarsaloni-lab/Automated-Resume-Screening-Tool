import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


# 🔹 Clean text function
def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove special characters & numbers
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]

    cleaned_text = " ".join(words)

    return cleaned_text