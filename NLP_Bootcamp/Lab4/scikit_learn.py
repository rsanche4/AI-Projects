import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('..\\Material\\TextFiles\\smsspamcollection.tsv', sep='\t')

# print(df.head())

# print(df.isnull().sum())

# print(len(df))

# print(df['label'].unique())
# print(df['label'].value_counts())

# plt.xscale('log')
# bins = 1.15**(np.arange(0,50))
# plt.hist(df[df['label']=='ham']['length'], bins=bins, alpha=0.8)
# plt.hist(df[df['label']=='spam']['length'], bins=bins, alpha=0.8)
# plt.legend(('ham', 'spam'))
# plt.show()

# plt.xscale('log')
# bins = 1.15**(np.arange(0,15))
# plt.hist(df[df['label']=='ham']['punct'], bins=bins, alpha=0.8)
# plt.hist(df[df['label']=='spam']['punct'], bins=bins, alpha=0.8)
# plt.legend(('ham', 'spam'))
# plt.show()

# from sklearn.model_selection import train_test_split

# # X feature data
# X = df[['length', 'punct']]
# # y is our label
# y = df['label']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# print(X_train.shape)
# print(X_test.shape)
# print(y_train)
# print(y_test)

# from sklearn.linear_model import LogisticRegression

# lr_model = LogisticRegression(solver="lbfgs")
# lr_model.fit(X_train, y_train)

# from sklearn import metrics

# preds = lr_model.predict(X_test)
# print(preds)

# print(y_test)

# print(metrics.confusion_matrix(y_test, preds))

# print(metrics.classification_report(y_test, preds))

# print(metrics.accuracy_score(y_test, preds))

# from sklearn.naive_bayes import MultinomialNB

# nb_model = MultinomialNB()

# nb_model.fit(X_train, y_train)

# predicts = nb_model.predict(X_test)

# print(metrics.confusion_matrix(y_test, predicts))

# -----------------------------------------------------------

# df = pd.read_csv('..\\Material\\TextFiles\\smsspamcollection.tsv', sep='\t')

# #print(df['label'].value_counts())

# X = df['message']
# y = df['label']

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# from sklearn.feature_extraction.text import CountVectorizer

# count_vect = CountVectorizer()

# # FIT VECTORIZER TO THE DATA (build a vocab, count the number of words...)
# # count_vect.fit(X_train)
# # X_train_counts = count_vect.transform(X_train)
# # TRANSFORM THE ORIGINAL TEXT MESSAGE ---> VECTOR

# X_train_counts = count_vect.fit_transform(X_train)

# from sklearn.feature_extraction.text import TfidfTransformer
# tfidf_transformer = TfidfTransformer()

# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# # SHORTER WAY TO DO THIS
# from sklearn.feature_extraction.text import TfidfVectorizer
# vectorizer = TfidfVectorizer()
# X_train_tfidf = vectorizer.fit_transform(X_train)

# from sklearn.svm import LinearSVC

# clf = LinearSVC()

# clf.fit(X_train_tfidf, y_train)

# from sklearn.pipeline import Pipeline

# text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])

# text_clf.fit(X_train, y_train)

# predictions = text_clf.predict(X_test)

# from sklearn.metrics import confusion_matrix, classification_report

# print(confusion_matrix(y_test, predictions))

# print(classification_report(y_test, predictions))

# print(text_clf.predict(['Hi! How are you doing today?']))
# print(text_clf.predict(['CONGRATS!! YO u have been selected to winner. TEXT WON 23434 for this HahahAH']))

# -----------------------------------------------------------
# Assessment

df = pd.read_csv('..\\Material\\TextFiles\\moviereviews2.tsv', sep='\t')
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.isnull().sum())

blanks = []
for i,lb,rv in df.itertuples():
    if type(rv)==str and rv.isspace():
        blanks.append(i)

df.drop(blanks, inplace=True)

X = df['review']
y = df['label']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])

text_clf.fit(X_train, y_train)

predictions = text_clf.predict(X_test)
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
print(accuracy_score(y_test, predictions))