# -------------------- IMPORTS --------------------
import numpy as np  
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt 
import seaborn as sns  # used for heatmap


# -------------------- LOAD DATA --------------------
df_Telco = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


# -------------------- PREPROCESSING --------------------

# Encode target (Yes/No → 1/0)
le = LabelEncoder()
df_Telco['Churn'] = le.fit_transform(df_Telco['Churn'])

# Drop unnecessary column
df_Telco = df_Telco.drop('customerID', axis=1)

# Convert categorical → numeric
df_Telco = pd.get_dummies(df_Telco, drop_first=True)


# -------------------- FEATURES & TARGET --------------------
X = df_Telco.drop('Churn', axis=1)
y = df_Telco['Churn']


# -------------------- SPLIT --------------------
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -------------------- SCALING --------------------
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


# -------------------- MODELS --------------------

# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(x_train_scaled, y_train)

# KNN
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(x_train_scaled, y_train)


# -------------------- PREDICTIONS --------------------

log_pred = log_model.predict(x_test_scaled)
knn_pred = knn_model.predict(x_test_scaled)


# -------------------- EVALUATION --------------------

# Accuracy
log_accuracy = accuracy_score(y_test, log_pred)
knn_accuracy = accuracy_score(y_test, knn_pred)

print("Logistic Regression Accuracy:", log_accuracy)
print("K-NN Accuracy:", knn_accuracy)

# Classification report
print("\nLogistic Regression Report:\n", classification_report(y_test, log_pred))
print("\nK-NN Report:\n", classification_report(y_test, knn_pred))


# -------------------- CONFUSION MATRIX --------------------

# Logistic Regression confusion matrix
cm_log = confusion_matrix(y_test, log_pred)

plt.figure()
sns.heatmap(cm_log, annot=True, fmt='d')
plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# KNN confusion matrix
cm_knn = confusion_matrix(y_test, knn_pred)

plt.figure()
sns.heatmap(cm_knn, annot=True, fmt='d')
plt.title("K-NN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# -------------------- COMPARISON BAR CHART --------------------

plt.bar(['Logistic Regression', 'K-NN'], [log_accuracy, knn_accuracy])
plt.title('Model Performance Comparison')
plt.ylabel('Accuracy')
plt.show()