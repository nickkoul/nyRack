from sklearn.externals import joblib
from sklearn import svm
import main

def classify(node):
    clf = joblib.load('model.pkl')
    # Build feature X from node
    X = [[  node.feature_nearby_accident,
            # node.feature_nearby_venues )
            node.feature_biking_popularity,
            node.feature_nearby_transportation,
            node.feature_average_rack_distance ]]
    return clf.predict(X)

if __name__ == '__main__':
    # Get citibike station points
    # Develop feature set for each
    # Build X
    # Build Y
    citiStations = main.get_citiBike_stations()
    stations = zip(*citiStations)
    for x in stations[0]:
        x.node.calculate_desireability()
    X = [[  x.node.feature_nearby_accident,
            # x.node.feature_nearby_venues )
            x.node.feature_biking_popularity,
            x.node.feature_nearby_transportation,
            x.node.feature_average_rack_distance ] for x in stations[0]]
    y = stations[1]
    # X = [[0, 0], [2, 2]]
    # y = [0.5, 2.5]
    clf = svm.SVR()
    clf.fit(X, y)
    joblib.dump(clf, 'model.pkl')
