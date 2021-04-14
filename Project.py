#Loading pandas library
import math
import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt

data = pd.read_csv('irisdata.csv')


#Using the pandas read_csv function to read the iris data csv file


#Printing out first 5 lines 


#Setting Iris classes to variables







IrisSetosa = data[0:50]
IrisVersicolor = data[51:100]
IrisVirginica = data[101:151]



print(data.head())

print(data.sample(10))

print(data.columns)

print(data.shape)



#using iloc to create variables based on each class of flower's attributes starting with Sepal Length

#print(data.columns)

IrisSetosa_SepalLength = data.iloc[:50,0:1] 

IrisVersicolor_SepalLength = data.iloc[51:100,0:1] 

IrisVirginica_SepalLength = data.iloc[101:151,0:1] 


#using mean method in pandas to calculate each classes mean sepal length

print(IrisSetosa_SepalLength.mean())
print(IrisVersicolor_SepalLength.mean())
print(IrisVirginica_SepalLength.mean())





#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#https://www.askpython.com/python/built-in-methods/python-iloc-function
# https://www.youtube.com/watch?v=naRQyRZrXCE
