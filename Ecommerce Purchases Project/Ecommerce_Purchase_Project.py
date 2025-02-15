'''''
E-Commerce Purchases Dataset:
1. Display Top 10 Rows of The Dataset
2. Check Last 10 Rows of The Dataset
3. Check Datatype of Each Column
4. Check null values in the dataset
5. How many rows and columns are there in our Dataset? 
6. Highest and Lowest Purchase Prices.
7. Average Purchase Price
8. How many people have French 'fr' as their Language?
9. Job Title Contains Engineer
10. Find The Email of the person with the following IP Address: 132.207.160.22
11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
12. Find the email of the person with the following Credit Card Number: 4664825258997302
13. How many people purchase during the AM and how many people purchase during PM?
14. How many people have a credit card that expires in 2020?
15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...)
'''''

import pandas as pd

data = pd.read_csv("C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries/Pandas/Ecommerce Purchases")

##1. Display Top 10 Rows of The Dataset
print(data.head(10))

##2. Display Last 10 Rows of The Dataset

print(data.tail(10))

#Check Data type of each column
print(data.dtypes)

##Check Null values in dataset
print(data.isnull().sum())

##How many rows and columns are there in dataset
print(data.columns)
print(len(data.columns))

print(len(data))
print(data.info())

##Highest and Lowest Purchase Prices
print(data.columns)
print(data['Purchase Price'].max())
print(data['Purchase Price'].min())

#Avg purchase price
print(data['Purchase Price'].mean())

#How many people have french 'fr' as their language?
print(data[data['Language'] == 'fr'])
#length of those people
print(len(data[data['Language'] == 'fr']))
#or using count()
print(data[data['Language'] == 'fr'].count()) 

print(data[data["Job"].str.contains('engineer')])


##Find Email of person with following IP address
print(data[data["IP Address"] == "132.207.160.22"]['Email'])

## How many People have Mastercard as their credit card provider and made a purchase above 50
print( len(data[(data['CC Provider'] == "Mastercard") & (data["Purchase Price"] > 50)]) )

##Find Email of the person with the following credit card Number: 4664825258997302
print(data[data['Credit Card'] == 4664825258997302] ['Email'])

##How many people purchase during AM and how many people purchase during PM
print(data['AM or PM'].value_counts())

##How many people have credit card that expires in 2020
print(data.columns)
print(data['CC Exp Date'])
def fun():
    count = 0
    for date in data['CC Exp Date']:
        if date.split('/')[1] == '20':
            count += 1
    print(count)
fun()
## or same using lamba-slicing
print(len(data[data['CC Exp Date'].apply(lambda x:x[3:] == '20')]))

##Top 5 most popular email providers(e.g gmail.com, yahoo.com, etc..)
list1 = []
for email in data['Email']:
    list1.append(email.split('@')[1])
data['temp'] = list1
print(data.head(1))
print(data['temp'].value_counts().head())
## or same using lambda-slicing
print(data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head())