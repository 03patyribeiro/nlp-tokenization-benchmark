import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.tokenizers import TokenizerBenchmark

@pytest.fixture
def benchmark():
    return TokenizerBenchmark()

def test_nltk_tokenization(benchmark):
    text = "Hello world!"
    tokens, time = benchmark.tokenize_nltk(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0
    assert time >= 0

def test_spacy_tokenization(benchmark):
    text = "Hello world!"
    tokens, time = benchmark.tokenize_spacy(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0

def test_bert_tokenization(benchmark):
    text = "Hello world!"
    tokens, time = benchmark.tokenize_bert(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0

def test_xlnet_tokenization(benchmark):
    text = "Hello world!"
    tokens, time = benchmark.tokenize_xlnet(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0