'''
Questions: 
1. Display All Rows Except the Last 5 rows Using Head Method
2. Display All Rows Except the First 5 Rows Using Tail Method
3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
5. Get Overall Statistics About The Dataframe
6. Data Cleaning  (Replace '--'  to NaN)
7. Check Null Values In The Dataset
8. Data Cleaning [ Rank Column ]
9. Data Cleaning [ Video Uploads & Subscribers ]
10. Data Cleaning [ Grade Column ]
11. Find Average Views For Each Channel
12. Find Out Top Five Channels With Maximum Number of Video Uploads
14.  Which Grade Has A Maximum Number of Video Uploads?
15.Which Grade Has The Highest Average Views?
16.  Which Grade Has The Highest Number of Subscribers? 
17. Which Grade Has The Highest Video Views? 
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Load the dataset
data = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries/Pandas/Youtube Channel Dataset Project/top-5000-youtube-channels.csv')

#1. Display All Rows Except the Last 5 rows Using Head Method
print("--- Display All Rows Except the Last 5 rows Using Head Method ---")
print(data.head(-5))

#2. Display All Rows Except the First 5 Rows Using Tail Method
print("--- Display All Rows Except the First 5 Rows Using Tail Method ---")
print(data.tail(-5))

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("--- Find Shape of Our Dataset (Number of Rows And Number of Columns) ---")   
print("Number of Rows : ", data.shape[0])
print("Number of Columns : ", data.shape[1])

#4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print("--- Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement ---")
print(data.info())

#5. Get Overall Statistics About the Dataframe
print("--- Get Overall Statistics About the Dataframe ---")
print(data.describe())

#6. Data Cleaning  (Replace '--'  to NaN)
print("--- Data Cleaning  (Replace '--'  to NaN) ---")
print(data.tail(10))
data = data.replace('--', np.nan, regex = True)
print(data.tail(10))

#7. Check Null Values In The Dataset
print("--- Check Null Values In The Dataset ---")
print(data.isnull().sum())
per_missing = data.isnull().sum() * 100 / len(data)
print("Percentage of Null Values : ",per_missing)
sns.heatmap(data.isnull())
#plt.show()

print(data.dropna(axis = 0, inplace = True))  # Drop all rows with NaN values
print(data.isnull().sum())      # Check if all NaN values are removed
per_missing = data.isnull().sum() * 100 / len(data)     # Check the percentage of missing values
print("Percentage of Null Values : ",per_missing)   # Print the percentage of missing values    
sns.heatmap(data.isnull())
#plt.show()

#8. Data Cleaning [ Rank Column ]
print("--- Data Cleaning [ Rank Column ] ---")
print(data['Rank'].head(10))   
data['Rank'] = data['Rank'].str[0:-2]  # Remove the last two characters from the Rank Column
print(data['Rank'].head(10))

data['Rank'] = data['Rank'].str.replace(",","")  # Remove the comma from the Rank Column
print(data['Rank'].tail(10))

print("Rank DataType before : ", data['Rank'].dtype)
data['Rank'] = data['Rank'].astype(int)  # Convert the Rank Column to Integer
print("Rank DataType after : ", data['Rank'].dtype)

print(data.dtypes)

#9. Data Cleaning [ Video Uploads & Subscribers ]
print("--- Data Cleaning [ Video Uploads & Subscribers ] ---")
print(data['Video Uploads'].head(10))

print("Video Uploads Before DataType : ", data["Video Uploads"].dtype)
data['Video Uploads'] = data['Video Uploads'].astype(int)  # Convert the Video Uploads Column to Integer
print("Video Uploads After DataType : ", data["Video Uploads"].dtype)

print('Subscribers Before DataType : ', data['Subscribers'].dtype)
data['Subscribers'] = data['Subscribers'].astype(int)  # Convert the Subscribers Column to Integer
print("Subscribers After DataType : ", data['Subscribers'].dtype)

#10. Data Cleaning [ Grade Column ]

print("--- Data Cleaning [ Grade Column ] ---")

print(data.dtypes)
print("Before Grades : ", data['Grade'].unique()) 
data['Grade'] = data['Grade'].map({'A++ ':5, 'A+ ':4, 'A ':3, 'A- ':2, 'B+ ':1})  # Map the Grade Column to Numerical Values
print("After Grades : ", data['Grade'].unique())
print(data.dtypes)

#11. Find Average Views For Each Channel
print("--- Find Average Views For Each Channel ---")
print(data.columns)
data['Avg_Views'] = data['Video views'] / data['Video Uploads']
print(data.head(10))

#12. Find Out Top Five Channels With Maximum Number of Video Uploads    
print("--- Find Out Top Five Channels With Maximum Number of Video Uploads ---")
print(data.sort_values(by='Video Uploads', ascending = False).head(5)['Channel name'])

#14. Which Grade Has A Maximum Number of Video Uploads?
print("--- Which Grade Has A Maximum Number of Video Uploads? ---")
print(data.groupby('Grade')['Video Uploads'].sum())
sns.barplot(x = 'Grade', y = 'Video Uploads', data = data)
#plt.show()

print(",.,.,.,.")
print(data.sort_values(by='Grade', ascending = False)['Views'].mean)

#15. Which Grade Has The Highest Average Views?
print("--- Which Grade Has The Highest Average Views? ---")
print(data.groupby('Grade')['Avg_Views'].mean())
sns.barplot(x = 'Grade', y = 'Avg_Views', data = data)

#16. Which Grade Has The Highest Number of Subscribers?
print("--- Which Grade Has The Highest Number of Subscribers? ---")
print(data.groupby('Grade')['Subscribers'].sum())

#17. Which Grade Has The Highest Video Views?
print("--- Which Grade Has The Highest Video Views? ---")
print(data.groupby('Grade')['Video views'].sum())
