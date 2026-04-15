class ExplainAgent:
    def __init__(self):
        # simple stopwords (ignore useless words)
        self.stopwords = {"with", "for", "and", "the", "a", "to", "of", "in", "looking"}

    def explain(self, job_text, resume_text, missing_skills):
        job_words = set(job_text.lower().split()) - self.stopwords
        resume_words = set(resume_text.lower().split()) - self.stopwords

        matched_skills = job_words.intersection(resume_words)

        explanation = {
            "matched_skills": list(matched_skills)[:5],
            "missing_skills": list(missing_skills - self.stopwords)[:5]
        }

        return explanation