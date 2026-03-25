import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report ,precision_score , recall_score , f1_score
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA

# ================================
#Load data 
#================================

data = load_breast_cancer(as_frame=True);
df = data.frame

#print  head of the data 
print(df.head())

#feature and target 
x = df.drop(columns = ["target"])
y = df["target"]

#split data into train and test
x_train ,x_test , y_train ,y_test  = train_test_split(x,y,test_size=0.2 , random_state= 42)

#train the model 
model = LogisticRegression(max_iter=1000)
model.fit(x_train ,y_train)

#prediction
y_pred = model.predict(x_test)

#evaluate the model
accuracy = accuracy_score(y_test , y_pred)
precision = precision_score(y_test , y_pred)
recall = recall_score(y_test ,y_pred)
f1 = f1_score(y_test , y_pred)

print("Accuracy :" ,accuracy)
print("precision :" ,precision)
print("recall :" ,recall)
print("F1 score :" , f1)

#visulization of confusion matrix

cm = confusion_matrix(y_test , y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm ,annot = True , fmt = "d" , cmap = "Blues")
plt.xlabel("predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


#classification report 

report = classification_report(y_test , y_pred)
print("classification report :\n" , report)


#plt decision boundary 

pca  = PCA (n_components=2)
x_pca = pca.fit_transform(x)

# Split the PCA-transformed data
x_train_pca, x_test_pca, y_train, y_test = train_test_split(x_pca, y, test_size=0.2, random_state=42)

# Train logistic regression on PCA data
model_pca = LogisticRegression(max_iter=1000)
model_pca.fit(x_train_pca, y_train)

# Create a mesh grid for plotting decision boundary
x_min, x_max = x_pca[:, 0].min() - 1, x_pca[:, 0].max() + 1
y_min, y_max = x_pca[:, 1].min() - 1, x_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.5),
                     np.arange(y_min, y_max, 0.5))

# Predict on the grid
Z = model_pca.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.figure(figsize=(8,6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y, s=50, edgecolor='k', cmap=plt.cm.Paired)
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("Logistic Regression Decision Boundary (PCA-reduced data)")
plt.show()




