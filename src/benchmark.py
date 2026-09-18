import pandas as pd
from src.tokenizers import TokenizerBenchmark

def run_benchmark(text: str):
    benchmark = TokenizerBenchmark()
    
    results = []
    
    tokens, time = benchmark.tokenize_nltk(text)
    results.append({"Library": "NLTK", "Time (s)": time, "Token Count": len(tokens), "Sample Tokens": str(tokens[:5])})
    
    tokens, time = benchmark.tokenize_spacy(text)
    results.append({"Library": "spaCy", "Time (s)": time, "Token Count": len(tokens), "Sample Tokens": str(tokens[:5])})
    
    tokens, time = benchmark.tokenize_bert(text)
    results.append({"Library": "BERT", "Time (s)": time, "Token Count": len(tokens), "Sample Tokens": str(tokens[:5])})
    
    tokens, time = benchmark.tokenize_xlnet(text)
    results.append({"Library": "XLNet", "Time (s)": time, "Token Count": len(tokens), "Sample Tokens": str(tokens[:5])})
    
    df = pd.DataFrame(results)
    print("\n--- Benchmark Results ---")
    print(df.to_string(index=False))
    return df

if __name__ == "__main__":
    with open("data/sample_text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    run_benchmark(text)