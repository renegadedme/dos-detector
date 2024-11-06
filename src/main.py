from model import train_model, detect_ddos
from preprocess import load_and_preprocess_data

def main():
    # Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # Train the model
    model = train_model(X_train, y_train)

    # Run detection on test set
    detect_ddos(model, X_test, y_test)

if __name__ == "__main__":
    main()
