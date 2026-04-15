class LearningAgent:
    def __init__(self):
        self.preferences = {}

    def update_preferences(self, job_text):
        words = job_text.lower().split()

        for word in words:
            if word not in self.preferences:
                self.preferences[word] = 0
            self.preferences[word] += 1

    def get_preference_score(self, job_text):
        words = job_text.lower().split()
        score = sum(self.preferences.get(word, 0) for word in words)
        return score