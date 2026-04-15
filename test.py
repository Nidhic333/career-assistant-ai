from agents.resume_agent import ResumeAgent 
from agents.matching_agent import MatchingAgent
from agents.decision_agent import DecisionAgent
from sentence_transformers import SentenceTransformer
from agents.explain_agent import ExplainAgent
from agents.learning_agent import LearningAgent

# initialize agents
resume_agent = ResumeAgent()
model = SentenceTransformer('all-MiniLM-L6-v2')
matching_agent = MatchingAgent()
decision_agent = DecisionAgent()
explain_agent = ExplainAgent()
learning_agent = LearningAgent()

# sample data
resume = "I know Python, Machine Learning and Data Science"

jobs = [
    "Looking for a Python developer with ML experience",
    "Frontend developer with React skills",
    "Data Scientist with deep learning knowledge"
]

# embeddings
resume_embedding = resume_agent.get_embedding(resume)
job_embeddings = model.encode(jobs)

# matching
results = matching_agent.match_jobs(resume_embedding, job_embeddings)

# print results
for idx, score in results:
    job_text = jobs[idx]

    decision, missing = decision_agent.decide(score, job_text, resume)
    explanation = explain_agent.explain(job_text, resume, missing)

    preference_score = learning_agent.get_preference_score(job_text)

    print(f"Job: {job_text}")
    print(f"Score: {score:.2f}")
    print(f"Decision: {decision}")
    print(f"Matched skills: {explanation['matched_skills']}")
    print(f"Missing skills: {explanation['missing_skills']}")
    print(f"Preference Score: {preference_score}")
    print("-----")

    # simulate user liking good jobs
    if score > 0.6:
        learning_agent.update_preferences(job_text)