#Loading pandas library
import math
import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt

data = pd.read_csv('irisdata.csv')


#Using the pandas read_csv function to read the iris data csv file


#Printing out first 5 lines 


#Setting Iris classes to variables







IrisSetosa = data[1:50]
IrisVersicolor = data[51:100]
IrisVirginica = data[101:151]



#print(data.head())

#print(data.sample(10))

# sample method pulls ten random rows of the data

#print(data.columns)

# looking at the column heads

#print(data.shape)

 #data method in numpy returns shape of the date



#using iloc to create variables based on each class of flower's attributes starting with Sepal Length


IrisSetosa_SepalLength = data.iloc[1:50,0:1] 

IrisVersicolor_SepalLength = data.iloc[51:100,0:1] 

IrisVirginica_SepalLength = data.iloc[101:151,0:1] 

#using mean method in pandas to create mean variables for each Classes Sepal Length
IrisSetosa_SepalLength_Mean = IrisSetosa_SepalLength.mean()
IrisVersicolor_SepalLength_Mean = IrisVersicolor_SepalLength.mean()
IrisVirginica_SepalLength_Mean = IrisVirginica_SepalLength.mean()


#using iloc to create variables based on each class of flower's attributes : Sepal Width

IrisSetosa_SepalWidth = data.iloc[1:50,1:2]
IrisVersicolor_SepalWidth = data.iloc[51:100,1:2]
IrisVirginica_SepalWidth = data.iloc[101:151,1:2]


#using mean method in pandas to create mean variables for each Classes Sepal Width
IrisSetosa_SepalWidth_Mean = IrisSetosa_SepalWidth.mean()
IrisVersicolor_SepalWidth_Mean = IrisVersicolor_SepalWidth.mean()
IrisVirginica_SepalWidth_Mean = IrisVirginica_SepalWidth.mean()


#print(IrisVersicolor_SepalLength.mean())
#print(IrisVirginica_SepalLength.mean())

#print(IrisVirginica_SepalWidth)

#using iloc to create variables based on each class of flower's attributes : Petal Length

IrisSetosa_PetalLength = data.iloc[1:50,2:3]
IrisVersicolor_PetalLength = data.iloc[51:100,2:3]
IrisVirginica_PetalLength = data.iloc[101:151,2:3]


#using mean method in pandas to create mean variables for each Classes Petal Length
IrisSetosa_PetalLength_Mean = IrisSetosa_PetalLength.mean()
IrisVersicolor_PetalLength_Mean = IrisVersicolor_PetalLength.mean()
IrisVirginica_PetalLength_Mean = IrisVirginica_PetalLength.mean()


#using iloc to create variables based on each class of flower's attributes : Petal Width

IrisSetosa_PetalWidth = data.iloc[1:50,3:4]
IrisVersicolor_PetalWidth = data.iloc[51:101,3:4]
IrisVirginica_PetalWidth = data.iloc[101:151,3:4]

#using mean method in pandas to create mean variables for each Classes Petal Width

IrisSetosa_PetalWidth_Mean = IrisSetosa_PetalWidth.mean()
IrisVersicolor_PetalWidth_Mean = IrisVersicolor_PetalWidth.mean()
IrisVirginica_PetalWidth_Mean = IrisVirginica_PetalWidth.mean()


with open('analysis.py','w')as f:
    f.write('Analyis of Iris Data Set \n Analysis of Each Class Sepal Length... \n Iris Setosa Sepal Length Mean:{}  \n Iris Versicolor Sepal Length Mean: {} \n  Iris Virginica Sepal Length Mean : {} '.format(IrisSetosa_SepalLength_Mean,IrisVersicolor_SepalLength_Mean,IrisVirginica_SepalLength_Mean))

#print(data.describe())



#Creating a histogram for Septal Length


x = data["Sepal Length"]

plt.hist(x,bins = 20, color = 'blue')
plt.title('Sepal Length ')
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.savefig('SepalLengthhist.png')


#print(data[" Class"].value_counts)

cols = data.columns
print(cols)


#Research and articles used below:
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#https://www.askpython.com/python/built-in-methods/python-iloc-function
# https://www.youtube.com/watch?v=naRQyRZrXCE
#http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
