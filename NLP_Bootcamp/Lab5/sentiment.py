# # import spacy

# # nlp = spacy.load('en_core_web_lg')

# # # print(nlp(u'the brown fox jumped').vector.shape)

# # # tokens = nlp(u'lion cat pet')

# # # for token1 in tokens:
# # #     for token2 in tokens:
# # #         print(token1.text, token2.text, token1.similarity(token2))

# # # tokens = nlp(u'like love hate')

# # # for token1 in tokens:
# # #     for token2 in tokens:
# # #         print(token1.text, token2.text, token1.similarity(token2))

# # # tokens = nlp(u'dog cat nargle')

# # # for t in tokens:
# # #     print(t.text, t.has_vector, t.vector_norm, t.is_oov)

# # from scipy import spatial

# # cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1, vec2)

# # king = nlp.vocab['king'].vector
# # man = nlp.vocab['man'].vector
# # woman = nlp.vocab['woman'].vector

# # # king - man + woman ----> queen, princess, highness

# # new_vector = king - man + woman
# # computed_similarities = []

# # for s in nlp.vocab.vectors:
# #     word=nlp.vocab[s]
# #     if word.has_vector and word.is_lower and word.is_alpha:
# #         similarity = cosine_similarity(new_vector, word.vector)
# #         computed_similarities.append((word, similarity))

# # computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])

# # for t in computed_similarities[:10]:
# #     print(t[0].text)

# import nltk

# #nltk.download('vader_lexicon')

# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sid = SentimentIntensityAnalyzer()

# a = "Hi"

# print(sid.polarity_scores(a))

# import pandas as pd

# df = pd.read_csv('..\\Material\\TextFiles\\amazonreviews.tsv', sep='\t')

# df.dropna(inplace=True)
# blanks = []
# for i,lb,rv in df.itertuples():
#     if type(rv)==str and rv.isspace():
#         blanks.append(i)
# print(blanks) # no blanks

# print(sid.polarity_scores(df.iloc[0]['review']))

# df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))

# df['compound'] = df['scores'].apply(lambda d: d['compound'])

# df['comp_score'] = df['compound'].apply(lambda s: 'pos' if s>=0 else 'neg')

# print(df.head())

# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# print(accuracy_score(df['label'], df['comp_score']))

# print(classification_report(df['label'], df['comp_score']))

# print(confusion_matrix(df['label'], df['comp_score']))

# Assessment

import spacy

nlp = spacy.load('en_core_web_lg')

from scipy import spatial

cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1, vec2)

a = nlp.vocab['red'].vector
b = nlp.vocab['round'].vector
c = nlp.vocab['fruit'].vector
d = nlp.vocab['food'].vector
e = nlp.vocab['eat'].vector
f = nlp.vocab['meat'].vector
g = nlp.vocab['vegetable'].vector


new_vector = a+b+c+d+e-f-g
computed_similarities = []

for s in nlp.vocab.vectors:
    word=nlp.vocab[s]
    if word.has_vector and word.is_lower and word.is_alpha:
        similarity = cosine_similarity(new_vector, word.vector)
        computed_similarities.append((word, similarity))

computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])

for t in computed_similarities[:10]:
    print(t[0].text)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

a = "this movie was so bad it was so disgusting and horrible, god it made me want to PUKE!! horrible just a disgrace to society"

print(sid.polarity_scores(a))