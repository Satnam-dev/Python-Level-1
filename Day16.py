# Machine Learnig
# Supervised Learning :- Data is labeled or model is trained using labled data
# It makee prediction and decision based on the labeled data
# Example:- Spam detection , Fraud detection ,Face recognition  , Netflix or amazon recmmendation ,ChatBots

# Ad :- highly accurate with sufficient labeled data , used for prediction tasks , 
# used for classification( used to predict categories values) and regression tasks(Used to predict numeric values)

# Disad :- Requires large amount of labeled data , expensive and time consuming to label data , not suitable for complex tasks\

# Types of Supervised Learning:-
# 1.Classification:- It is used to predict categories values (or class labels)
# Types of Classification:-
# Binary Classification:- It is used to predict two class labels ( yes or no ,spam or not spam)
# Multiclass Classification:- It is used to predict more than two class labels (Yes, No, Maybe)


# 2. Regression:- It is used to predict continuous values or numeric values
# Example:- Predicting house prices , stock prices , weather forecasting
# Ad:- Used for prediction tasks , used for regression tasks , can handle large amount of data
# Disad:- Requires large amount of data , not suitable for complex tasks , sensitive to outliers

# Types of Regression:-
# Linear Regression:- It is used to predict continuous values or numeric values based on linear relationship between independent and dependent variables
# Example:- Predicting house prices based on square footage , number of bedrooms

# Logistic Regression:- It is used to predict binary values (yes or no , spam or not spam) based on linear relationship between independent and dependent variables
# Decision Tree Regression:- It is used to predict continuous values or numeric values based on decision tree algorithm
# Random Forest Regression:- It is used to predict continuous values or numeric values based on random forest algorithm
# k-Nearest Neighbors Regression:- It is used to predict continuous values or numeric values based on k-nearest neighbors algorithm
# support Vector Regression:- It is used to predict continuous values or numeric values based on support vector machine algorithm



# Pre requisite:- Google colab , python + Seikit Learn library , Pandas library , Numpy library , Matplotlib library , Seaborn library                          

# Step 1:- Open Google Colab and create a new notebook.

# A library is a collection of pre-written code that provides useful functions, classes, and tools.
# Step 2:- Import the required libraries such as import pandas as pd.
# Import pandas as pd (used to create and manage DataFrames).
# Import numpy as np (used to perform mathematical and numerical operations).
# Import matplotlib.pyplot as plt (used to create graphs and visualizations).
# Import seaborn as sns (used to create statistical visualizations).
# Import S

# Step 3:- Enter the dataset.
# data={
# "Study_Hours":[1,2,3,4,5,6,7,8],
# "Result":['0','0','0','0','1','1','1','1']
# }

# Step 4:- Create a DataFrame using the dataset, such as df=pd.DataFrame(data).
# df =pd.DataFrame(data)
# print(df)

# Step 5:- Split the dataset into training and testing sets.
# Import train_test_split from sklearn.model_selection. 

# Step 6:- from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# Select the input feature and target variable.
# X = df[["Study_Hours"]]
# y = df["Result"]

# Create a Logistic Regression model.
# model = LogisticRegression()

# Train the model using the training data.
# model.fit(X_train, y_train)
# print("Model trained successfully.")

# Step 6:- Train the model using the training data.
# model.fit(X_train, y_train)

# Make a prediction for a student who studied for 2 hours.
# prediction = model.predict([[2]])
# print("Prediction:", prediction)

# Install numpy in a specific folder
# python3 -m pip install numpy 
