from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# sample data
resume = "I know Python, Machine Learning and Data Science"

jobs = [
    "Looking for a Python developer with ML experience",
    "Frontend developer with React skills",
    "Data Scientist with deep learning knowledge"
]

# -------------------------------
# BASELINE: TF-IDF
# -------------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([resume] + jobs)

tfidf_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

print("🔹 TF-IDF Scores:")
for job, score in zip(jobs, tfidf_scores):
    print(f"{job} → {score:.2f}")

# -------------------------------
# YOUR MODEL: EMBEDDINGS
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

resume_emb = model.encode(resume)
job_embs = model.encode(jobs)

embed_scores = cosine_similarity([resume_emb], job_embs).flatten()

print("\n🔹 Embedding Scores:")
for job, score in zip(jobs, embed_scores):
    print(f"{job} → {score:.2f}")