# importing packages

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import re
import json
import warnings
warnings.filterwarnings("ignore")

# Loading the data from local machine, the location of data should be modified accordingly 

df=data.iloc[:,:12]
df=data.loc[df['Name']=='India']
df.drop(['CCA3','Area (km²)','Density (per km²)','GrowthRate','World Population Percentage','Rank'],axis=1,inplace=True)
df=df.T

df=df.reset_index().rename(columns={1:'population','index':'year'})
df=df.iloc[1:,:]

# Creating a function to call LR that predicts the population of specified country with different models

def LR():
    country = input("Please input the country name: ")
    year = int(input("Please input the year to predict: "))
    df = pd.read_csv('population.csv')
    lists=df.iloc[:,:15]
    lists.drop(['CCA3','Area (km²)','Density (per km²)','GrowthRate','World Population Percentage','Rank'],axis=1,inplace=True)
    lists=lists.T
    temp=lists.iloc[0,:]
    l=[i for i in temp]
    if country in l:
      df = pd.read_csv('population.csv')
      df=data.iloc[:,:12]
      df=data.loc[df['Name']==country]
      df.drop(['CCA3','Area (km²)','Density (per km²)','GrowthRate','World Population Percentage','Rank'],axis=1,inplace=True)
      df=df.T
  
      df=df.reset_index().rename(columns={1:'population','index':'year'}) 
      df=df.iloc[1:,:]

      x = df.iloc[:, 0].values.reshape(-1,1)
      y = df.iloc[:, 1].values.reshape(-1,1)
      model = LinearRegression().fit(x,y)
      print("Estimated population using Linear Regression model is :"+str(int(model.coef_[0][0] * year + model.intercept_[0])))
        
    else:
        print('kindly check country name spelling\n')
        
  # Calling LR() function to enter input data 
  
  LR()
  
  
