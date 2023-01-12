import numpy as np
from sklearn.datasets import load_iris
from PyPDF2 import PdfReader

# iris = load_iris()

# X = iris.data

# y = iris.target

# from keras.utils import to_categorical

# y = to_categorical(y)

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# from sklearn.preprocessing import MinMaxScaler

# scaler_object = MinMaxScaler()

# scaler_object.fit(X_train)

# scaled_X_train = scaler_object.transform(X_train)

# scaled_X_test = scaler_object.transform(X_test)

# from keras.models import Sequential
# from keras.layers import Dense
# model = Sequential()
# model.add(Dense(8, input_dim=4, activation='relu'))
# model.add(Dense(8, input_dim=4, activation='relu'))
# model.add(Dense(3, activation='softmax'))

# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# print(model.summary())

# model.fit(scaled_X_train, y_train, epochs=150, verbose=2)

# predictions = model.predict(scaled_X_test)
# predictions=np.argmax(predictions,axis=1)


# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# print(accuracy_score(y_test.argmax(axis=1), predictions))

# print(classification_report(y_test.argmax(axis=1), predictions))

# print(confusion_matrix(y_test.argmax(axis=1), predictions))


#model.save('dsa.h5')
#from keras.models import load_model

#s = load_model('dsa.h5')
#s.predict etc use this one now

pdf_loc = 'TheCatcher.pdf'
reader = PdfReader(pdf_loc)
page = reader.pages[1]
text = ''
for p in reader.pages:
    text += p.extract_text()

import spacy
nlp = spacy.load('en_core_web_lg', disable=['parser', 'tagger', 'ner'])
def separate_punc(doc_text):
    return [token.text.lower() for token in nlp(doc_text) if token.text not in '!@#$%^&*()_+--=<>,.?/:;"~`[]}{\t \n\n\n \n\n \n \n \n \n  \n  \n \n  \n \n \n \n \n \n \n \n \n \n\n\n\n\n\n\n\n\n']

tokens = separate_punc(text)
#print(tokens)

#25 words
train_len = 25+1
text_sequences = []

for i in range(train_len, len(tokens)):
    seq = tokens[i-train_len:i]
    text_sequences.append(seq)

from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()

tokenizer.fit_on_texts(text_sequences)
sequences = tokenizer.texts_to_sequences(text_sequences)

vocabulary_size = len(tokenizer.word_counts)
#print(sequences[0])

sequences = np.array(sequences)
#print(sequences)

from keras.utils import to_categorical

X = sequences[:,:-1] # grab it all except the last column

y = sequences[:,-1] # grab only last column

y = to_categorical(y, num_classes=vocabulary_size+1)

#print(y)

seq_len = X.shape[1]

from keras.models import Sequential

from keras.layers import Dense,LSTM,Embedding

def create_model(vocab_size, seq_len):
    model = Sequential()
    model.add(Embedding(vocab_size,seq_len,input_length=seq_len))
    model.add(LSTM(50,return_sequences=True))
    model.add(LSTM(50))
    model.add(Dense(50,activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model

model = create_model(vocabulary_size+1, seq_len)

from pickle import dump, load

model.fit(X,y,batch_size=128, epochs=1000, verbose=1)
model.save('model_catcher.h5')

from keras.models import load_model
#model = load_model('model_catcher.h5')

dump(tokenizer, open('simple_tok', 'wb'))

from keras_preprocessing.sequence import pad_sequences
def generate_text(model, tokenizer, seq_len, seed_text, num_gen_words):
    output_text= []
    input_text = seed_text
    for i in range(num_gen_words):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len, truncating='pre')
        pred_word_ind=np.argmax(model.predict(pad_encoded,verbose=0)[0])
        
        pred_word = tokenizer.index_word[pred_word_ind]
        input_text += ' '+pred_word

        output_text.append(pred_word)
    return ' '.join(output_text)

import random
random.seed(101)
random_pick = random.randint(0, len(text_sequences))
random_seed_text = text_sequences[random_pick]
seed_text = ' '.join(random_seed_text)

print(generate_text(model, tokenizer, seq_len, seed_text, 25))