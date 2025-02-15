'''
Questions:
1. Display Top 5 Rows of The Dataset
2. Check the Last 3 Rows of The Dataset
3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
5. Get Overall Statistics About The Dataframe
6. Total Number of App Titles Contain Astrology
7. Find Average App Rating
8.  Find Total Number of Unique Category
9. Which Category Getting The Highest Average Rating?
10. Find Total Number of App having 5 Star Rating
11. Find Average Value of Reviews
12. Find Total Number of Free and Paid Apps
13.  Which App Has Maximum Reviews?
14. Display Top 5 Apps Having Highest Reviews
15. Find Average Rating of Free and Paid Apps
16. Display Top  5 Apps Having Maximum Installs
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries/Pandas/Google Play Store Project/googleplaystore.csv')
#1. Display Top 5 Rows of The Dataset
print("---Top 5 Rows of The Dataset---")
print(data.head())

#2. Check the Last 3 Rows of The Dataset
print("---Last 3 Rows of The Dataset---")
print(data.tail(3))

#3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
print("---Shape of Our Dataset (Number of Rows & Number of Columns)---")
print("Number of Rows : ", data.shape[0])
print("Number of Columns : ", data.shape[1])

#4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print("---Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement---")
print(data.info())

#5. Get Overall Statistics About The Dataframe
print("---Overall Statistics About The Dataframe---")
print(data.describe(include='all'))

#6. Total Number of App Titles Contain Astrology
print("---Total Number of App Titles Contain Astrology---")
print(data.columns)
print("Length : ",len(data[data['App'].str.contains('Astrology', case = False)]))

#7. Find Average App Rating
print("---Average App Rating---")
print("Average : ",data['Rating'].mean())


#8.  Find Total Number of Unique Category
print("---Total Number of Unique Category---")
print("Total Unique Catogeroies : ",data['Category'].nunique())

#9. Which Category Getting The Highest Average Rating?
print("---Category Getting The Highest Average Rating---")
print(data.groupby('Category')['Rating'].mean().sort_values(ascending = False))

#10. Find Total Number of App having 5 Star Rating
print("---Total Number of App having 5 Star Rating---")
print(len(data[data['Rating'] == 5.0]))

#11. Find Average Value of Reviews
print("---Average Value of Reviews---")
print("DataType is : ", data['Reviews'].dtype)
print(data[data['Reviews'] == '3.0M'])
data['Reviews'] = data['Reviews'].replace('3.0M',3.0)   #replacing '3.0M' to 3.0, so tht we can find average of Reviews 
print(data['Reviews'] == '3.0M')    #checking whether '3.0M' is present or not - False.
data['Reviews'] = data['Reviews'].astype('float')   #changing datatype from object to int

print("Changed DataType : ", data['Reviews'].dtype)
print("Average : ",data['Reviews'].mean())       #calculating mean

#12. Find Total Number of Free and Paid Apps
print("--- Total Number of Free and Paid Apps---")
print(data.head(1).to_string())
print(data['Type'].value_counts())


#13.  Which App Has Maximum Reviews?
print("---Which App Has Maximum Reviews---")
print(data[data['Reviews'].max() == data['Reviews']] ['App'])

#14. Display Top 5 Apps Having Highest Reviews
print("---Top 5 Apps Having Highest Reviews---")
#print(data[data['Reviews'].sort_values(ascending=False).head()]['App'])     #this will display index error
#or
index = data['Reviews'].sort_values(ascending=False).head().index   #by specifying index
print(data.iloc[index]['App'])

#15. Find Average Rating of Free and Paid Apps
print('---Average Rating of Free and Paid Apps---')
print(data.groupby('Type')['Rating'].mean())

#16. Display Top  5 Apps Having Maximum Installs
print("---Top  5 Apps Having Maximum Installs---")
print("OG dtype is : ",data['Installs'].dtype)       #dtype is object, need to convert in integer
data['Installs_1'] = data['Installs'].str.replace(',','')   #removing ',' from Installs column
print(data.head(1)) 
 
data['Installs_1'] = data['Installs_1'].str.replace('+','')  #removing '+' from Installs_1 column
print(data.head(1))

data['Installs_1'] = data['Installs_1'].str.replace('Free', '0')   #removing 'Free' from Installs_1 columns
data['Installs_1'] = data['Installs_1'].astype('int')       #change dtype from object to integer
print("Changed dtype is : ",data['Installs_1'].dtype)                         #check dtype

 
index = data['Installs_1'].sort_values(ascending=False).head().index
print("Final Answer : ",data.iloc[index]['App'])
