import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "The cat sat on the mat.",
    "The dog chased the cat.",
    "The dog and the cat sat on the mat.",
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

cosine_sim = (tfidf_matrix * tfidf_matrix.T).toarray()

print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())

print("\nCosine Similarity Matrix:")
print(cosine_sim)
