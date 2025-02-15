'''''San Francisco City Employee Salary  Dataset:

1.  Display Top 10 Rows of The Dataset
2. Check Last 10 Rows of The Dataset
3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
5. Check Null Values In The Dataset
6. Drop ID, Notes, Agency, and Status Columns
7. Get Overall Statistics About The Dataframe
8. Find Occurrence of The Employee Names  (Top 5)
9. Find The Number of Unique Job Titles
10.Total Number of Job Titles Contain Captain
11. Display All the Employee Names From Fire Department
12. Find Minimum, Maximum, and Average BasePay
13. Replace 'Not Provided' in EmployeeName' Column to NaN 
15. Find Job Title of ALBERT PARDINI
16. How Much ALBERT PARDINI Make (Include Benefits)?
17.Display Name of The Person Having The Highest BasePay
18.Find Average BasePay of All Employee Per Year 
19. Find Average BasePay of All Employee Per JobTitle 
20. Find Average BasePay of Employee Having Job Title ACCOUNTANT  
21. Find Top 5 Most Common Jobs
'''''

import pandas as pd
data = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/Python Libraries/Pandas/Salaries.csv')
print(data.columns)

##1.  Display Top 10 Rows of The Dataset
print(data.head(10))

#2. Check Last 10 Rows of The Dataset
print(data.tail(10))

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("Number of Columns: ",len(data.columns))
print("Number of Rows : ", data.shape[0])
#or 
print("Number of Rows and columns : ",data.shape)

#4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(data.info())

#5. Check Null Values In The Dataset
print(data.isnull().sum())

#6. Drop ID, Notes, Agency, and Status Columns       "axis=1 for columns &&& axis=0 for rows"
print("---Dropping columns---")
drop = data.drop(["Id", "Notes", "Agency", "Status"], axis = 1)
print(drop.head())

#7. Get Overall Statistics About The Dataframe
print("---Overall Statistics---")
print(data.describe(include = 'all'))

#8. Find Occurrence of The Employee Names  (Top 5)
print("---Occurence of Employee Names---")
print(data['EmployeeName'].value_counts().head())

#9. Find The Number of Unique Job Titles
print("---Number of Unique Job Titles---")
print(data['JobTitle'].nunique())
#or
print(len(data['JobTitle'].unique()))

#10.Total Number of Job Titles Contain Captain      "case=False for avoiding case sensitive && case=True for considering case"
print("---Number of Job Titles that contain Captain---")
print(len(data[data['JobTitle'].str.contains('CAPTAIN', case = False)]))
#or
print(data[data['JobTitle'].str.contains('CAPTAIN', case = False)].count())

#11. Display All the Employee Names From Fire Department
print("---Employee Names From Fire Department---")
print(data[data['JobTitle'].str.contains('fire', case = False)]['EmployeeName'])

#12. Find Minimum, Maximum, and Average BasePay
print("---Minimum, Maximum, and Average BasePay---")
print(data['BasePay'].describe())

#13. Replace 'Not Provided' in EmployeeName' Column to NaN 
print("---Replace 'Not Provided' in EmployeeName' Column to NaN---")
import numpy as np
data["EmployeeName"] = data['EmployeeName'].replace('Not provided', np.nan)
print(data['EmployeeName'])

#15. Find Job Title of ALBERT PARDINI
print("---Job Title of ALBERT PARDINI---")
print(data[data['EmployeeName'] == 'ALBERT PARDINI'] ['JobTitle'])

#16. How Much ALBERT PARDINI Make (Include Benefits)?
print("---Job Title of ALBERT PARDINI---")
print(data[data['EmployeeName'] == 'ALBERT PARDINI']['TotalPayBenefits'])

#17.Display Name of The Person Having The Highest BasePay
print("---Name of The Person Having The Highest BasePay---")
# Ensure 'BasePay' is numeric, coercing errors to NaN
data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

# Find the row(s) with the maximum BasePay
max_basepay_row = data[data['BasePay'] == data['BasePay'].max()]

# Print the 'EmployeeName' for that row
print(max_basepay_row['EmployeeName'])


#18.Find Average BasePay of All Employee Per Year 
print("---Average BasePay of All Employee Per Year---")
# Convert 'BasePay' to numeric, coercing non-numeric values to NaN
data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

# Group by 'Year' and calculate the mean 'BasePay'
yearly_mean_basepay = data.groupby('Year')['BasePay'].mean()

# Print the result
print(yearly_mean_basepay)


#19. Find Average BasePay of All Employee Per JobTitle 
print("---Average BasePay of All Employee Per JobTitle---")
# Convert 'BasePay' to numeric, coercing non-numeric values to NaN
data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

# Group by 'Year' and calculate the mean 'BasePay'
yearly_mean_basepay = data.groupby('JobTitle')['BasePay'].mean()

# Print the result
print(yearly_mean_basepay)

#20. Find Average BasePay of Employee Having Job Title ACCOUNTANT  
print("---Average BasePay of Employee Having Job Title ACCOUNTANT---")
# Ensure 'BasePay' is numeric, converting non-numeric values to NaN
data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

# Filter the data for employees with JobTitle "ACCOUNTANT"
accountant_data = data[data['JobTitle'].str.upper() == 'ACCOUNTANT']

# Calculate the average BasePay for accountants
average_basepay_accountant = accountant_data['BasePay'].mean()

# Display the result
print(f"The average BasePay of employees with the job title 'ACCOUNTANT' is: {average_basepay_accountant}")

#21. Find Top 5 Most Common Jobs
print("---Top 5 Most Common Jobs---")
# Count the occurrences of each JobTitle
job_counts = data['JobTitle'].value_counts()

# Get the top 5 most common jobs
top_5_jobs = job_counts.head(5)

# Display the result
print(top_5_jobs)
