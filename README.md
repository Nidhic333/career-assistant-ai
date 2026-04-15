#  Intelligent Multi-Agent Career Assistant
An AI-powered system that recommends relevant jobs using a multi-agent architecture with decision-making, explainability, and learning capabilities.
##  Features
- Resume understanding using embeddings
- Intelligent job matching using semantic similarity
- Decision-making agent (Apply / Maybe / Skip)
- Explainability (matched skills & missing skills)
- Learning agent (adapts to user preferences)
- Evaluation (TF-IDF vs Embedding comparison)
- Streamlit UI for interactive usage
##  System Architecture
This project is built using multiple AI agents:
- Resume Agent → Converts resume text into embeddings
- Matching Agent → Ranks jobs using cosine similarity
- Decision Agent → Determines whether to apply
- Explain Agent → Provides reasoning for recommendations
- Learning Agent → Adapts based on user interactions
## 🛠️ Tech Stack
- Python
- PyTorch
- Sentence Transformers
- Scikit-learn
- Streamlit
## Evaluation
Compared traditional TF-IDF with embedding-based matching.
Result: Embedding-based model performs better in capturing semantic similarity and improves job relevance ranking.
##  Project Structure
career-assistant-ai/
│
├── agents/
│   ├── resume_agent.py
│   ├── matching_agent.py
│   ├── decision_agent.py
│   ├── explain_agent.py
│   └── learning_agent.py
│
├── evaluation/
│   └── evaluate.py
│
├── app.py
├── test.py
├── requirements.txt
├── README.md
##  How to Run
1. Clone the repository:
git clone https://github.com/Nidhic333/career-assistant-ai.git
cd career-assistant-ai
2. Create virtual environment:
python -m venv venv
venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run the application:
streamlit run app.py
## Future Improvements
- Real-time job scraping (LinkedIn, Indeed)
- Advanced skill extraction using NLP
- Reinforcement learning for better decision-making
- Deploy as a web application
## 👩‍💻 Author
Nidhi Conjeevaram
