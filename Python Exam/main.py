import pandas as pd 
import numpy as np 

r=pd.read_csv('AQI_Data.csv')

# Display first five rows of dataset
print("\n \n")
print("First five rows of dataset :- ")
print(r.head())

# Display last six rows of dataset
print("\n \n")
print("Last six rows of dataset :- ")
print(r.tail(6))

# Calculating summary statistics for all numeric columns
print("\n \n")
print("Summary statistics for all numeric column :- ")
print(r.describe())

# Mean of AQI, PM2.5 and PM10
print("\n \n")
print("Mean of AQI, PM_2.5 and PM_10 values for each city :- ")
print(r[['City','AQI','PM2.5','PM10']].groupby('City').mean())

# Calculating cities with highest and lowest average AQI
print("\n \n")
print("Cities with highest and lowest average AQI values : ")
di=dict(r.groupby('City')['AQI'].mean().sort_values(ascending=False))

li=list(di.keys())
print("Cities with highest average AQI values is ",li[0]," with values ",di[li[0]])
print("Cities with lowest average AQI values is ",li[-1]," with values ",di[li[-1]])