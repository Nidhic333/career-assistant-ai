import streamlit as st
from agents.resume_agent import ResumeAgent
from agents.matching_agent import MatchingAgent
from agents.decision_agent import DecisionAgent
from agents.explain_agent import ExplainAgent
from agents.learning_agent import LearningAgent
from sentence_transformers import SentenceTransformer

# initialize agents
resume_agent = ResumeAgent()
matching_agent = MatchingAgent()
decision_agent = DecisionAgent()
explain_agent = ExplainAgent()
learning_agent = LearningAgent()
model = SentenceTransformer('all-MiniLM-L6-v2')

st.title("🤖 AI Career Assistant")

# user input
resume = st.text_area("Paste your Resume")

jobs = [
    "Looking for a Python developer with ML experience",
    "Frontend developer with React skills",
    "Data Scientist with deep learning knowledge"
]

if st.button("Analyze Jobs"):
    if resume:
        resume_embedding = resume_agent.get_embedding(resume)
        job_embeddings = model.encode(jobs)

        results = matching_agent.match_jobs(resume_embedding, job_embeddings)

        st.subheader("📊 Results")

        for idx, score in results:
            job_text = jobs[idx]

            decision, missing = decision_agent.decide(score, job_text, resume)
            explanation = explain_agent.explain(job_text, resume, missing)

            preference_score = learning_agent.get_preference_score(job_text)

            st.write("### 💼 Job:", job_text)
            st.write("Score:", round(score, 2))
            st.write("Decision:", decision)
            st.write("Matched Skills:", explanation["matched_skills"])
            st.write("Missing Skills:", explanation["missing_skills"])
            st.write("Preference Score:", preference_score)
            st.write("---")

            if score > 0.6:
                learning_agent.update_preferences(job_text)