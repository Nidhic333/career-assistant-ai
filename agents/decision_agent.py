class DecisionAgent:
    def __init__(self):
        pass

    def decide(self, score, job_text, resume_text):
        # simple skill gap logic (basic version)
        job_skills = set(job_text.lower().split())
        resume_skills = set(resume_text.lower().split())

        missing_skills = job_skills - resume_skills

        # decision rules
        if score > 0.75 and len(missing_skills) < 5:
            decision = "Apply ✅"
        elif score > 0.5:
            decision = "Maybe ⚠️"
        else:
            decision = "Skip ❌"

        return decision, missing_skills