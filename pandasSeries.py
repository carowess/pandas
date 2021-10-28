import pandas as pd

## Series IS case sensitive
grades = pd.Series([87,100,94])

print(grades)

grades2 = pd.Series(98.6,range(3))

print(grades2)

print(grades[0])

## you get lots of info with this method
print(grades.describe())

## two ways to make your own indexes
# 1
grades = pd.Series([87,100,94], index=["Wally","Eva","Sam"])
print(grades)
#2
grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})
print(grades)

print(grades['Eva'])

print(grades.Wally)

print(grades.dtype)

print(grades.values)

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

print(hardware)

## calling string methods apply to each element
print(hardware.str.contains('a'))

print(hardware.str.upper())
