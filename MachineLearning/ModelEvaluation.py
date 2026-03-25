from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score , KFold
from sklearn.ensemble import RandomForestClassifier


#Load data
data = load_iris(as_frame= True)
X ,y = data.data , data.target 

#initialize classifier
model = RandomForestClassifier(random_state= 42)

#perform k-Fold cross-validation 
kf = KFold(n_splits=5 ,shuffle= True , random_state= 42)
cv_scores = cross_val_score(model , X , y , cv=kf , scoring="accuracy")

#output results
print("cross validation scores :" , cv_scores)
print("mean cross validation score :" , cv_scores.mean())