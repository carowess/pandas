import pandas as pd

grades_dict = {'Wally':[87,96,70],
                'Eva':[100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

print(grades)

## each column in the dataset is a Series 
print(grades['Eva'])

print(grades.Sam)

print(grades.loc['Test1'])

## only use numbers for iloc method
print(grades.iloc[1])

## when you use custom indexes the upper bound IS included 
print(grades.loc['Test1':'Test3'])

## upper bound IS NOT included when you use the zero-based indexes
print(grades.iloc[0:2])

## getting consecutives, not a range. make sure to add extra parenthesees
print(grades.loc[['Test1','Test3']])

print(grades.iloc[[0,2]])

print(grades.loc['Test1':'Test2',['Eva','Katie']])

print(grades.iloc[0:2,[1,3]])

grades90 = grades[grades>=90]

print(grades90)

gradesB = grades[(grades>=80) & (grades<90)]

print(gradesB)

## OR sign is "|"
gradesAorB = grades[(grades>90) | (grades>= 80)]

print(gradesAorB)

print(grades.at['Test2','Eva'])

grades.at['Test2','Eva'] = 100

print(grades)

print(grades.iat[1,1])

## makes decimal place to 2 
pd.set_option('precision',2)

print(grades.describe())

## transpose method
print(grades.T.describe())

## sorting by the index
print(grades.sort_index(ascending=False))

print(grades.sort_index(axis=1))

print(grades.sort_values(by='Test1',axis=1,ascending=False))

print(grades.T.sort_values(by='Test1',ascending=False))

print(grades.loc["Test1"].sort_values(ascending=False))

