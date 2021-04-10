#Loading pandas library

import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt

data = pd.read_csv('irisdata.csv')

#Using the pandas read_csv function to read the iris data csv file

print(data.head())

#Printing out first 5 lines 


#Setting Iris classes to variables

IrisVersicolor = data[51:100]

IrisSetosa = data[1:50]

IrisVirginica = data[101:150]

