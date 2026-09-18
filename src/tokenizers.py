import nltk
import spacy
from transformers import BertTokenizer, XLNetTokenizer
from datetime import datetime

class TokenizerBenchmark:
    def __init__(self):
        print("Loading models... This may take a moment.")
        self.nlp_spacy = spacy.load("en_core_web_sm")
        self.bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.xlnet_tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
        print("Models loaded successfully.")

    def tokenize_nltk(self, text: str):
        start = datetime.now()
        tokens = nltk.word_tokenize(text)
        end = datetime.now()
        return tokens, (end - start).total_seconds()

    def tokenize_spacy(self, text: str):
        start = datetime.now()
        doc = self.nlp_spacy(text)
        tokens = [token.text for token in doc]
        end = datetime.now()
        return tokens, (end - start).total_seconds()

    def tokenize_bert(self, text: str):
        start = datetime.now()
        tokens = self.bert_tokenizer.tokenize(text)
        end = datetime.now()
        return tokens, (end - start).total_seconds()

    def tokenize_xlnet(self, text: str):
        start = datetime.now()
        tokens = self.xlnet_tokenizer.tokenize(text)
        end = datetime.now()
        return tokens, (end - start).total_seconds()