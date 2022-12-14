# -*- coding: utf-8 -*-
"""20MIA1119 ML LAB FAT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZKcCYWtUvlXCB3CyMedQoDz5bcoG3oMB

Importing libraries
"""

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn import tree

"""Read the data
`
"""

df = pd.read_csv("/content/winequality.csv")

df

"""Applying EDA on the dataset"""

# See the first five rows of the dataset
df.head()

#mean of the dataset
df.mean()

#median of the dataset
df.median()

df.mode()

# See the number of rows and columns
print("Rows, columns: " + str(df.shape))

"""Finding missing values

"""

# Missing Values
print(df.isna().sum())

"""as all the vaues are 0, we say that there is no null value.

if we observe that hter are null values in the dataset, we remove them by either considerng the mean, mefian or by deleting the null values

applying correlaton and representing in the dataset
"""

fig = px.histogram(df,x='quality')
fig.show()

corr = df.corr()

"""correlation matrix"""

corr

##representing the same in a heat map

plt.pyplot.subplots(figsize=(10,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(330, 30, as_cmap=True))

sns.countplot(x='quality', data=corr)

"""applying classification"""

# Create Classification version of target variable
df['goodquality'] = [1 if x >= 7 else 0 for x in df['quality']]

# Separate feature variables and target variable
X = df.drop(['quality','goodquality'], axis = 1)
y = df['goodquality']

# See proportion of good and bad wines
df['goodquality'].value_counts()

sns.countplot(y)

# Normalize feature variables
from sklearn.preprocessing import StandardScaler
X_features = X
X = StandardScaler().fit_transform(X)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

"""#Splitting dataset into 80% training dataset and 20% test dataset. Random state is set to 1119"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1119)

"""representing the samples of two data"""

print("Number of samples in training set:", X_train.shape[0])
print("Number of samples in testing set:", X_test.shape[0])

"""setting depth max to 1"""

csd_gini = DecisionTreeClassifier(criterion = "gini",random_state = 1119,max_depth=1, min_samples_leaf=5)
csd_gini.fit(X_train, y_train)
csd_gini

y_pred = csd_gini.predict(X_test)
print("Predicted values:")
print(y_pred)

print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)

"""here, the accuracy =77%

Min samples leaf change to 50
"""

csd_gini = DecisionTreeClassifier(criterion = "gini",random_state = 1119,max_depth=3, min_samples_leaf=50)
csd_gini.fit(X_train, y_train)
csd_gini

y_pred = csd_gini.predict(X_test)
print("Predicted values:")
print(y_pred)

print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)

"""With max depth 3, we get 79 accuracy

As we can see the accuracy remains approximately same at 79 from 77 in the previous test so we try to increase min_sample_leaf to 90 and max_depth to 5
"""

csd_gini = DecisionTreeClassifier(criterion = "gini",random_state = 1119,max_depth=3, min_samples_leaf=90)
csd_gini.fit(X_train, y_train)
csd_gini

y_pred = csd_gini.predict(X_test)
print("Predicted values:")
print(y_pred)

print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)

"""here also, we see that the accuracy is 79%, so we increase the value of min_sample_leaf to 150"""

csd_gini = DecisionTreeClassifier(criterion = "gini",random_state = 1119,max_depth=3, min_samples_leaf=150)
csd_gini.fit(X_train, y_train)
csd_gini

y_pred = csd_gini.predict(X_test)
print("Predicted values:")
print(y_pred)

print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)

"""here also, we see that the accuracy is 80%, so we increase the value of min_sample_leaf to 300"""

csd_gini = DecisionTreeClassifier(criterion = "gini",random_state = 1119,max_depth=3, min_samples_leaf=200)
csd_gini.fit(X_train, y_train)
csd_gini

y_pred = csd_gini.predict(X_test)
print("Predicted values:")
print(y_pred)

"""building a confusion matrix"""

print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)

"""here, we can see that the maximum accuracy we hit is 80% which is quiet descent.

if we want more accuracy, we need to change the values of either the min_sample_leaf or by changing the random_state
"""

#applying decision tree classifier
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
model1 = DecisionTreeClassifier(random_state=1119)
model1.fit(X_train, y_train)
y_pred1 = model1.predict(X_test)
print(classification_report(y_test, y_pred1))

"""analysing feature importance"""

results_series = {"actual":y_test, "predicted":y_pred}
results = pd.DataFrame(results_series)

print("dividing into 5 rows of column")
results.head()

"""building the confusion_matrix"""

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=1119)
dt.fit(X_train, y_train)

from sklearn.metrics import plot_confusion_matrix
y_pred = dt.predict(X_test)
plt.plot_confusion_matrix(dt, X_test, y_test)
plt.show()
print(metrics.accuracy_score(y_test, y_pred))



"""we applied the decission tree algorithm.
we split the data to 80% train and 20% test.
the test % was 80% and the train% was 79%.

the same results were represented in the form of confusion matrix and the other plotting methods using the matplotlib library 
"""