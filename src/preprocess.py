import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Column names based on NSL-KDD dataset features (truncated for simplicity)
COLUMN_NAMES = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land',
    'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised',
    'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 
    'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 
    'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'class'
]

def load_and_preprocess_data():
    # Load training and testing data
    train_data = pd.read_csv('src/data/KDDTrain+.txt', names=COLUMN_NAMES)
    test_data = pd.read_csv('src/data/KDDTest+.txt', names=COLUMN_NAMES)

    # Encode attack labels as binary (1 for attack, 0 for normal)
    train_data['class'] = train_data['class'].apply(lambda x: 0 if x == 'normal' else 1)
    test_data['class'] = test_data['class'].apply(lambda x: 0 if x == 'normal' else 1)

    # Select numeric features for simplicity
    numeric_features = train_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    X_train = train_data[numeric_features].drop('class', axis=1)
    y_train = train_data['class']
    X_test = test_data[numeric_features].drop('class', axis=1)
    y_test = test_data['class']

    # Normalize feature values
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

