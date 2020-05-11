import nltk
# print(nltk.corpus.gutenberg.fileids())

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(len(emma))
print(emma[:100])
