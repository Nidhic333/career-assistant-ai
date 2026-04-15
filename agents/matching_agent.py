from sklearn.metrics.pairwise import cosine_similarity

class MatchingAgent:
    def __init__(self):
        pass

    def match_jobs(self, resume_embedding, job_embeddings):
        scores = cosine_similarity([resume_embedding], job_embeddings)[0]

        results = []
        for i, score in enumerate(scores):
            results.append((i, score))

        # sort by highest score
        results.sort(key=lambda x: x[1], reverse=True)

        return results