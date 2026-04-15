from sentence_transformers import SentenceTransformer

class ResumeAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_embedding(self, resume_text):
        embedding = self.model.encode(resume_text)
        return embedding