
from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'Thierry Pierre Dutoit'

import rake
import operator
import io

# EXAMPLE ONE - SIMPLE
stoppath = "data/stoplists/PortugueseStoplist.txt"


# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/articles/juliette_title.txt", 'r', encoding="utf-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Texto:", text, "\n")
print("Keywords:", keywords)

print("----------")

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/articles/juliette_subtitle.txt", 'r', encoding="utf-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Texto:", text, "\n")
print("Keywords:", keywords,"\n\n")

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/articles/judicial_title.txt", 'r', encoding="utf-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Texto:", text, "\n")
print("Keywords:", keywords)

print("----------")

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/articles/judicial_subtitle.txt", 'r', encoding="utf-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Texto:", text, "\n")
print("Keywords:", keywords, "\n\n")

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/articles/educacao_title.txt", 'r', encoding="utf-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Texto:", text, "\n")
print("Keywords:", keywords)

print("----------")

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/articles/educacao_subtitle.txt", 'r', encoding="utf-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Texto:", text, "\n")
print("Keywords:", keywords, "\n\n")


"""
# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

sample_file = io.open("data/docs/articles/juliette_subtitle.txt", 'r', encoding="utf-8")
text = sample_file.read()

# 1. Split text into sentences
sentenceList = rake.split_sentences(text)

for sentence in sentenceList:
    print("Sentence:", sentence)

# generate candidate keywords
stopwords = rake.load_stop_words(stoppath)
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern, stopwords)
print("Phrases:", phraseList)

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

# sort candidates by score to determine top-scoring keywords
sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# for example, you could just take the top third as the final keywords
for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
    print("Keyword: ", keyword[0], ", score: ", keyword[1])

print(rake_object.run(text))
"""