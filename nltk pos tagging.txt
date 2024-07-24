import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "the sun is shining brightly,I love reading interesting books."
tokens = nltk.word_tokenize(sentence)

for token in tokens:
    pos_tag = nltk.pos_tag([token])[0][1]
    lemmatized_word = nltk.WordNetLemmatizer().lemmatize(token)
    print(f"org: {token}, pos={pos_tag}, Lemma={lemmatized_word}")
