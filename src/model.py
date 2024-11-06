from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

def train_model(X_train, y_train):
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    print("Model trained successfully.")
    return model

def detect_ddos(model, X_test, y_test):
    predictions = model.predict(X_test)
    print("Detection Results:")
    print(classification_report(y_test, predictions))
    print("Accuracy:", accuracy_score(y_test, predictions))
