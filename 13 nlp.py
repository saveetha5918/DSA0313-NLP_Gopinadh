import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> V NP
V -> 'likes'
NP -> 'pizza'
""")

parser = nltk.ChartParser(grammar)
sentence = "John likes pizza"
tokens = sentence.split()

for tree in parser.parse(tokens):
    tree.pretty_print()
