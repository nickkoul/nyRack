import main, node

from sklearn.externals import joblib
from sklearn import svm

def classify(node):
    clf = joblib.load('model.pkl')
    # Build feature X from node
    return clf.predict([[1, 1]])

if __name__ == '__main__':
    # Get citibike station points
    # Develop feature set for each
    # Build X
    # Build Y
    X = [[0, 0], [2, 2]]
    y = [0.5, 2.5]
    clf = svm.SVR()
    clf.fit(X, y)
    joblib.dump(clf, 'model.pkl')
