import main, node

from sklearn.externals import joblib
from sklearn import svm

def classify(x):
    clf = joblib.load('model.pkl') 
    clf.predict([[1, 1]])

if __name__ == '__main__':
    X = [[0, 0], [2, 2]]
    y = [0.5, 2.5]
    clf = svm.SVR()
    clf.fit(X, y)
    joblib.dump(clf, 'model.pkl')
