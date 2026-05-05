from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 🔹 Match resume with job description
def match_resume_to_jd(resume_text, jd_text):
    
    # Combine texts
    documents = [resume_text, jd_text]

    # Convert to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    # Return score
    return similarity[0][0]