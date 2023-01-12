import pandas as pd

# npr = pd.read_csv('..\\Material\\05-Topic-Modeling\\npr.csv')

# print(npr.head())

# from sklearn.feature_extraction.text import CountVectorizer

# cv = CountVectorizer(max_df=0.9, stop_words='english')

# dtm = cv.fit_transform(npr['Article'])

# from sklearn.decomposition import LatentDirichletAllocation

# LDA = LatentDirichletAllocation(n_components=7, random_state=42)

# # WARNING: this will take a while
# LDA.fit(dtm)

# print(cv.get_feature_names()[:100])

# single_topic = LDA.components_[0]

# top_words = single_topic.argsort()[-20:]

# for index in top_words:
#     print(cv.get_feature_names()[index])

# for i,topic in enumerate(LDA.components_):
#     print("TOP WORDS FOR TOPIC #"+ str(i))
#     top_words = topic.argsort()[-20:]
#     for index in top_words:
#         print(cv.get_feature_names()[index])

npr = pd.read_csv('..\\Material\\05-Topic-Modeling\\npr.csv')

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')

dtm = tfidf.fit_transform(npr['Article'])

from sklearn.decomposition import NMF

nmf_model = NMF(n_components=7, random_state=42)

nmf_model.fit(dtm)

tfidf.get_feature_names()[2300]

for i,topic in enumerate(nmf_model.components_):
    print("TOP WORDS FOR TOPIC #"+ str(i))
    top_words = topic.argsort()[-20:]
    for index in top_words:
        print(tfidf.get_feature_names()[index], end=' ')

topic_results = nmf_model.transform(dtm)

topic_results.argmax(axis=1)
print(npr.head())

