'''
Questions:
1. Display Top 10 Rows of The Dataset
2. Check Last 5 Rows of The Dataset
3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
5. Check Null Values In The Dataset
6. Check For Duplicate Data and Drop Them
7. Find Out Number of Courses Per Subjects
8. For Which Levels, Udemy Courses Providing The Courses
10. Which Course Has More Lectures (Free or Paid)?
11. Which Courses Have A Higher Number of Subscribers Free or Paid?
12. Which Level Has The Highest Number of Subscribers?
13. Find Most Popular Course Title
14. Display 10 Most Popular Courses As Per Number of Subscribers
15. Find The Course Which Is Having The Highest Number of Reviews.
16. Does Price Affect the Number of Reviews?
17. Find Total Number of Courses Related To Python
18. Display 10 Most Popular Python Courses As Per Number of Subscribers
19. In Which Year The Highest Number of Courses Were Posted?
20. Display Category-Wise Count of Posted Subjects [Year Wise] 
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries/Pandas/Udemy Courses Project/udemy_courses_dataset.csv")

#1. Display Top 10 Rows of The Dataset
print("---Top 10 Rows of The Dataset---")
print(data.head(10))

#2. Check Last 5 Rows of The Dataset
print("---Last 5 Rows of The Dataset---")
print(data.tail(5))

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("---Shape of Our Dataset (Number of Rows And Number of Columns)---")
print("Number of Columns : ",len(data.columns))
print("Number of Rows : ", data.shape[0])


#4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print("---Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement---")
print(data.info())

#5. Check Null Values In The Dataset
print("---Check Null Values In The Dataset---")
print(data.isnull())
print("Any Null Values : ",data.isnull().values.any())

#6. Check For Duplicate Data and Drop Them
print("---Check For Duplicate Data and Drop Them---")
print("Duplicates in data : ",data.duplicated().values.any())
data = data.drop_duplicates()
print("Duplicates in data : ",data.duplicated().values.any())


#7. Find Out Number of Courses Per Subjects
print("---Number of Courses Per Subjects---")
print(data['subject'].value_counts())

sns.countplot(data['level'])
plt.xlabel('Subjects')
plt.ylabel('Number of Courses per subject')
#plt.show()  


#8. For Which Levels, Udemy Courses Providing The Courses
print("---For Which Levels, Udemy Courses Providing The Courses---")
print(data['level'].value_counts())
sns.countplot(data['subject'])
plt.xlabel('Levels')
plt.ylabel('Number of Courses per level')
#plt.show()  

#9. Display The Count of Paid and Free Courses 
print("---Display The Count of Paid and Free Courses---")
print(data['is_paid'].value_counts())
sns.countplot(data['is_paid'])
plt.xlabel('No of Free and Paid Courses')
plt.ylabel('Count')
#plt.show()  

#10. Which Course Has More Lectures (Free or Paid)?
print("---Which Course Has More Lectures (Free or Paid)?---")
print(data.groupby(['is_paid'])['num_lectures'].mean())

#11. Which Courses Have A Higher Number of Subscribers Free or Paid?
print("---Which Courses Have A Higher Number of Subscribers Free or Paid?---")
print(data.groupby(['is_paid'])['num_subscribers'].mean())

#12. Which Level Has The Highest Number of Subscribers?
print("---Which Level Has The Highest Number of Subscribers?---")
print(data['level'].value_counts().idxmax())
print(data['level'].value_counts().max())

#13. Find Most Popular Course Title
print("---Find Most Popular Course Title---")
print(data.columns)
most_pop = data[data['num_subscribers'].max() == data['num_subscribers']]
out = most_pop['course_title']
print(out)

#14. Display 10 Most Popular Courses As Per Number of Subscribers
print("---Display 10 Most Popular Courses As Per Number of Subscribers---")
print(data.columns)
top_10 = data.sort_values(by = "num_subscribers", ascending = False).head(10)
print(top_10)
sns.barplot(x = "num_subscribers", y = "course_title", data = top_10)
#plt.show()

#15. Find The Course Which Is Having The Highest Number of Reviews.
print("---Find The Course Which Is Having The Highest Number of Reviews---")
print(data.columns)
max_reviews = data[data['num_reviews'].max() == data['num_reviews']]
out = max_reviews['course_title']
print(out)
sns.barplot(x = "num_reviews", y = "course_title", data = max_reviews)
#plt.show()

#16. Does Price Affect the Number of Reviews?
print("---Does Price Affect the Number of Reviews?---")
print(data['price'].corr(data['num_reviews']))
sns.scatterplot(x = "price", y = "num_reviews", data = data)
plt.figure(figsize = (10,10))
#plt.show()

#17. Find Total Number of Courses Related To Python
print("---Find Total Number of Courses Related To Python---")
print(data[data['course_title'].str.contains('python', case = False)])
print("Total : ", data['course_title'].str.contains('Python').sum())

#18. Display 10 Most Popular Python Courses As Per Number of Subscribers
print("---Display 10 Most Popular Python Courses As Per Number of Subscribers---")
python_courses = data[data['course_title'].str.contains('python', case = False)]
out = python_courses.sort_values(by = 'num_subscribers', ascending = False).head(10)
print(out)

#19. In Which Year The Highest Number of Courses Were Posted?
print("---In Which Year The Highest Number of Courses Were Posted?---")
#data['year'] = data['published_timestamp'].dt.year
#print(data['year'].value_counts().idxmax())
#print(data['year'].value_counts().max())

#20. Display Category-Wise Count of Posted Subjects [Year Wise]
print("---Display Category-Wise Count of Posted Subjects [Year Wise]---")
