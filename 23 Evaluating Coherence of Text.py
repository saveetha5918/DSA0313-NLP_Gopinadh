import spacy

nlp = spacy.load("en_core_web_sm")

def evaluate_coherence(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    for i in range(1, len(sentences)):
        if sentences[i].start <= sentences[i-1].end:
            return False
    return True

def main():
    text = "John went to the market. He bought some apples."
    is_coherent = evaluate_coherence(text)
    print("Is the text coherent?", is_coherent)

if __name__ == "__main__":
    main()
