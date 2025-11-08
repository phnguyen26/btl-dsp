import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

#doc file csv
data = pd.read_csv('features.csv').drop('filename', axis=1)

# ma hoa 
# female -> 0
# male -> 1
le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])


X = data.drop('label', axis=1)
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

# train model
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

# du doan tren tap test
y_pred = lr.predict(X_test)
print(f'Accuracy score: {accuracy_score(y_test, y_pred)}')

#luu model da duoc train
joblib.dump(lr, 'model.pkl')
joblib.dump(le, 'label_encoder.pkl')





