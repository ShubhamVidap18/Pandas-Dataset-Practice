'''''
1. Display Top 5 Rows of The Dataset
2. Check the Last 3 Rows of The Dataset
3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
5. Get Overall Statistics About The Dataframe
6. Data Filtering
7.Check Null Values In The Dataset
8. Drop the Column
9. Handle Missing Values
10. Categorical Data Encoding
11. What is Univariate Analysis?
How Many People Survived And How Many Died?
How Many Passengers Were In First Class, Second Class, and Third Class?
Number of Male And Female Passengers
12. Bivariate Analysis
How Has Better Chance of Survival Male or Female?
Which Passenger Class Has Better Chance of Survival (First, Second, Or Third Class)? 
13. Feature Engineering
'''''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries\Pandas/titanic_dataset.csv')
print(data.head())

#1. Display Top 5 Rows of The Dataset
print("---Top 5 Rows of The Dataset---")
print(data.head(5))

#2. Check the Last 3 Rows of The Dataset
print("---Last 5 Rows of The Dataset---")
print(data.tail(3))

#3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
print("---Shape of Our Dataset (Number of Rows & Number of Columns)---")
print("Number of Rows : ", data.shape[0])
print("Number of Columns : ", data.shape[1])

#4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print("---Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement---")
print(data.info())

#5. Get Overall Statistics About The Dataframe
print("---Overall Statistics About The Dataframe---")
print(data.describe(include = "all"))

#6. Data Filtering
print("---Data Filtering---")
print(data.columns)
print(data[['Name', 'Age']])
print(data[data['Sex'] == 'male'])
print('Sum of rows : ',sum(data['Sex'] == 'male'))
print('Sum of Survived : ',sum(data['Survived']==1))

#7.Check Null Values In The Dataset
print(data.isnull().sum())
sns.heatmap(data.isnull())
#plt.show() 

per_missing = data.isnull().sum()*100/len(data)
print("Percentage of Missing Values : ",per_missing)

#8. Drop the Column
drop_cabin = data.drop('Cabin', axis = 1, inplace = True) 
print(drop_cabin)

print(data.isnull().sum())

#9. Handle Missing Values

print(data['Embarked'].mode()) #Most frequently repeating
print(data['Embarked'].fillna('S', inplace = True))     #handling missing values in Embarked column
print(data.isnull().sum())

print(data['Age'].fillna(data['Age'].mean(), inplace = True))   #handling missing values in Age column
print("Total Null values in Age columns : ",data['Age'].isnull().sum())

#10. Categorical Data Encoding
print("---Categorical Data Encoding---")
print(data['Sex'].unique())
data['Gender'] = data['Sex'].map({'male':1, 'female':0})    #assigning & accessing categorical using 1/0 
print(data.head(2))

x = data['Sex'].map({'male':1, 'female':0})
print(data.insert(5, 'Gender_new', x))  #adjusting columns as per our convenience
print(data.head(1))

#11. What is Univariate Analysis?
#How Many People Survived And How Many Died---?
print("---How Many People Survived And How Many Died---")
print(data['Survived'].value_counts())
sns.countplot(data['Survived'].value_counts())
#plt.show()

#How Many Passengers Were In First Class, Second Class, and Third Class?
print("---How Many Passengers Were In First Class, Second Class, and Third Class---")
print(data['Pclass'].value_counts())
sns.countplot(data['Pclass'])
#plt.show()

#Number of Male And Female Passengers
print("---Number of Male And Female Passengers---")
print(data['Sex'].value_counts())

plt.hist(data['Age'])
#plt.show() 

'''''
Note: 
-Countplot is suitable for representation of categorical data
-Boxplot and Histogram are used to represent graphical visualization to find frequency of numerical values
'''''

#12. Bivariate Analysis
#Who Has Better Chance of Survival Male or Female?
print("---Who Has Better Chance of Survival Male or Female---")
sns.barplot(x='Sex', y='Survived', data=data)
#plt.show()

#Which Passenger Class Has Better Chance of Survival (First, Second, Or Third Class)? 
print("---Which Passenger Class Has Better Chance of Survival (First, Second, Or Third Class)---")
sns.barplot(x='Pclass', y='Survived', data=data)
#plt.show()

#13. Feature Engineering
print("--- Feature Engineering---")
print(data.columns)
#create new column using 2 existing columns
print("---Create new column using 2 existing columns---")
data['Family_Size'] = data['SibSp'] + data['Parch'] 
print(data.head(1))

#fare per person, also creating new columns of Fair_per_person
print("---Fare per person, also creating new columns of Fair_per_person---")
data['Fare_per_person'] = data['Fare'] / (data['Family_Size']+1)   
print(data.head(1)) 



