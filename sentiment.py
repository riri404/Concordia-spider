from afinn import Afinn
import re
import nltk

class SentimentAnalyzer:
    def __init__(self):
        self.afinn = Afinn()

    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text)
        return text

    @staticmethod
    def tokenize_text(text):
        return nltk.word_tokenize(text)

    def get_sentiment(self, text):
        cleaned_text = self.clean_text(text)
        return self.afinn.score(cleaned_text)
