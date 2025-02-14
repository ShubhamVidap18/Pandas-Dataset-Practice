import pandas as pd

#Dataframes
myNames = {
    'Names' : ["ShubhamVidap", "RasikaVanga"],
    'DOB' : [18, 28],
    "Education" : ["B.Tech", "BAMS"],
    "Gender" : ["Male", "Female"]
}
df = pd.DataFrame(myNames, index = ["A","B"])
print(df)


#check pandas version
print(pd.__version__)


#Series
a = [24,25,26]
print(pd.Series(a))


#Labels
myLabel = pd.Series(a, index = ["A","B","C"])
print(myLabel)
print(myLabel["B"])


#Loc
print(df.loc["B"])

'''''
#Load Files Into a DataFrame
df2 = pd.read_excel('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/sample-data-10mins.xlsx')
print(df2)

df3 = pd.read_csv("C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/ac-sample.csv")
print(df3)
#To Avoid Truncation--> use to_string()
print(df3.to_string())
'''''

'''''

##check max and min rows
print(pd.options.display.max_rows)
print(pd.options.display.min_rows)
'''''

'''''

#Reading JSON files
df4 = pd.read_json('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/example_1.json', typ = "series")
df4 = df4.to_frame().T
print(df4.to_string())
'''''

'''''

##Viewing the Data 
df5 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/data.csv')
#head() method
print(df5.head())
print(df5.head(10))
#tail() method
print(df5.tail())
#info() method
print(df5.info())
'''''

'''''
#Cleaning data
df6 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/dataset_with_issues.csv')
#Deleting rows using dropna()
df6.dropna(inplace = True)
print(df6.to_string())
'''''

'''''
#replace empty values
df6 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/dataset_with_issues.csv')
df6["Calories"].fillna(1828, inplace = True)
'''''

'''''
#Converting data in correct format
df6 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/dataset_with_issues.csv')
if 'Date' in df6.columns:
    df6['Date'] = pd.to_datetime(df6['Date'])
else:
    print("The 'Date' column is missing.")
'''''

'''''
## Removing NAT(Datetime missing cells) using dropna
df6 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/dataset_with_issues.csv')
if 'Calories' in df6.columns:
    df.dropna(subset = ['Calories'], inplace = True)
    print(df6.to_string())
else:
    print('No Date Column Found!')
'''''


##Cleaning Wrong Data 
df6 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/dataset_with_issues.csv')

#Loop through all values in the "Duration" column.
for x in df6.index:
    if df6.loc[x, "Duration"] == 30:
        df6.loc[x, "Duration"] = 100
print(df6.to_string())

#Removing Duplicates
print(df6.duplicated())
#For dropping duplicates
print(df6.drop_duplicates(inplace = True))


##Data Correlations
df7 = pd.read_csv('C:/Users/shubh/OneDrive/Documents/Coding Stuff/Interview Prep Codes/data.csv')
print(df7.corr())


#Plotting
import matplotlib.pyplot as plt
#simple plotting
df7.plot()
#Using Scatter plot
df7.plot(kind = "scatter", x = "Duration", y = "Maxpulse")
df7.plot(kind = "hist", x = "Duration", y = "Calories") #histogram accepts single axis argument too
plt.show()


import pandas as pd

from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Example student data
student_data = [
    [1, 20],
    [2, 21],
    [3, 22],
    [4, 23]
]

# Create DataFrame
df_students = createDataframe(student_data)
print(df_students)