import spacy

nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(sentence):
    doc = nlp(sentence)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases

def main():
    sentence = "The quick brown fox jumps over the lazy dog."
    noun_phrases = extract_noun_phrases(sentence)
    print("Noun Phrases:", noun_phrases)

if __name__ == "__main__":
    main()
