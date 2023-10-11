import csv
import argparse
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer



def parse_args():
    parser = argparse.ArgumentParser(description='CLI tool for suggesting substitutions based on cosine similarity of words')
    parser.add_argument('text_path', help='Path to file with text')
    parser.add_argument('--threshold', type=float, default=0.4, help='Threshold for cosine similarity (default: 0.4)')
    return parser.parse_args()

def load_terms_list():
    with open('StandardisedTerms.csv', 'r') as f:
        terms_list = list(csv.reader(f))
        terms_list = [str(x)[2:-2] for x in terms_list]
    return terms_list


def load_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
    return text

def generate_three_word_phrases(text):
    sentences = sent_tokenize(text)
    phrases = []
    for sentence in sentences:
        words = sentence.split()
        phrases.extend([' '.join(words[i:i+3]) for i in range(0, len(words), 3)])
    return phrases


def vectorize_text(text_list):
    vector_model = TfidfVectorizer().fit(text_list)
    return vector_model.transform(text_list), vector_model