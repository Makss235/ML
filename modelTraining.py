from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import nltk
import re
import numpy

df = textData = new_text = None
clf = X = y = x_train = x_test = y_train = None
y_test = perc = None

def initDF(file_name = None):
    global df, textData

    if file_name == None:
        file_name = 'train_full.csv'

    try: 
        df = pd.read_csv(file_name)
        textData = df['text']
    except FileNotFoundError as e: 
        return e
    except KeyError as e:
        return e

def normalizeData():
    global textData, new_text

    new_text = []
    for i in textData:
        new_text.append(norm(i))

def vectorizeData():
    global tfidf_vectorizer, X, y, new_text

    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    X = tfidf_vectorizer.fit_transform(new_text).toarray()
    y = df["target"].values

def trainingModel():
    global df, X, y, x_train, x_test, y_train, y_test, clf

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
    clf = (SGDClassifier(max_iter = 1000))
    clf.fit(x_train, y_train)

def calculatingPercentage():
    global clf, x_test, y_test, perc

    dataCalcPerc = clf.predict(x_test)
    perc = accuracy_score(y_test, dataCalcPerc) * 100
    return perc

def testModel(message):
    global tfidf_vectorizer
    message = norm(message)
    test = tfidf_vectorizer.transform(list(message))
    return clf.predict(test)[0]

def norm(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z]", " ", text)
    return text

def normAndTrain():
    normalizeData()
    vectorizeData()
    trainingModel()
