'''''1.Display Top 10 Rows of The Dataset
2. Check Last 10 Rows of The Dataset
3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
5. Fetch Random Sample From the Dataset (50%)
6.Check Null Values In The Dataset
7.Perform Data Cleaning [ Replace '?' with NaN ]
8. Drop all The Missing Values
9. Check For Duplicate Data and Drop Them
10. Get Overall Statistics About The Dataframe
11. Drop The Columns education-num, capital-gain, and capital-loss
12. What Is The Distribution of Age Column?
13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
14. What is The Distribution of Workclass Column?
15. How Many Persons Having Bachelors or Masters Degree?
20. Covert workclass Columns Datatype To Category Datatype?

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries/Pandas/adult.csv')

#1.Display Top 10 Rows of The Dataset
print("---Top 10 Rows of The Dataset---")
print(data.head(10))

#2. Check Last 10 Rows of The Dataset
print("---Last 10 Rows of The Dataset---")
print(data.tail(10))

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("---Shape of Our Dataset (Number of Rows And Number of Columns---")
print("Number of Columns : ", len(data.columns))
print("Number of Rows : ", data.shape[0])

#4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print("---Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement---")
print(data.info())

#5. Fetch Random Sample From the Dataset (50%)
print("---Fetch Random Sample From the Dataset (50%)---")
print(data.sample(frac=0.5))

#6.Check Null Values In The Dataset
print("---Check Null Values In The Dataset---")
print(sns.heatmap(data.isnull()))
#plt.show()
print(data.isnull().sum(axis=1))

#7.Perform Data Cleaning [ Replace '?' with NaN ]
print("---7.Perform Data Cleaning [ Replace '?' with NaN ]---")
print("Before Replacement : ")
print(data.isin(['?']).sum())
data['workclass'] = data['workclass'].replace('?',np.nan)
data['occupation'] = data['occupation'].replace('?',np.nan)
data['native-country'] = data['native-country'].replace('?',np.nan)
print("After Replacement : ")
print(data.isin(['?']).sum())
print(sns.heatmap(data.isnull()))
#plt.show()
 

#8. Drop all The Missing Values
print("---8. Drop all The Missing Values---")
print(data.isnull().sum()*100/len(data))   ##to check percentage of missing values 
print(data.dropna(how = "any"))
print(data.shape)

#9. Check For Duplicate Data and Drop Them
print("---Duplicate Data and Drop Them---")
print("Duplicate data : ",data.duplicated().any())         ##to check whether duplicate data is present or not
print(data.drop_duplicates())

#10. Get Overall Statistics About The Dataframe
print("---Overall Statistics About The Dataframe---")
print(data.describe(include='all'))


#11. Drop The Columns education-num, capital-gain, and capital-loss
print("---Drop The Columns education-num, capital-gain, and capital-loss---")
print(data.columns)
drop_columns = data.drop(['educational-num', 'capital-gain', 'capital-loss'], axis=1)
print(drop_columns.columns)

#12. What Is The Distribution of Age Column?
print("---Distribution of Age Column---")
print(data['age'].describe())
print(data['age'].hist())
#plt.show()

#13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
print("---Total Number of Persons Having Age Between 17 To 48---")
print(sum((data['age'] >= 17) & (data['age'] <= 48)))
print(sum(data['age'].between(17, 48)))

#14. What is The Distribution of Workclass Column?
print("---Distribution of Workclass Column---")
print(data['workclass'].describe())
print(data['workclass'].hist())
#plt.show()

#15. How Many Persons Having Bachelors or Masters Degree?
print("---Persons Having Bachelors and Masters Degree---")
filter1 = data['education'] == 'Bachelors'
filter2 = data['education'] == 'Masters'
print(len(data[filter1 | filter2]))  #or
print(sum(data['education'].isin(['Bachelors', 'Masters'])))

#20. Covert workclass Columns Datatype To Category Datatype?
print("---Covert workclass Columns Datatype To Category Datatype---")
data['workclass'] = data['workclass'].astype('category')
print(data.info())
print(data['workclass'].dtype)