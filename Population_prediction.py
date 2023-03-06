# importing necessary packages

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import re
import json
import warnings
warnings.filterwarnings("ignore")


# Creating a function to call LR to reuse it multiple times

def LR():
    country = input("Please input the country name: ")              
    year = int(input("Please input the year to predict: "))
    
    #loading population dataset
    df = pd.read_csv('population.csv')   
    
    #filtering only country names from the dataset
    lists=df.iloc[:,:15]
    lists.drop(['CCA3','Area (km²)','Density (per km²)','GrowthRate','World Population Percentage','Rank'],axis=1,inplace=True)
    lists=lists.T
    temp=lists.iloc[0,:]
    l=[i for i in temp]
    
    #checking if the given country name is present in the dataset or not
    if country in l:
      df = pd.read_csv('population.csv')
    
      #dropping unnecessary data from the dataset that are irrelevant  
      df=data.iloc[:,:12]
      df=data.loc[df['Name']==country]
      df.drop(['CCA3','Area (km²)','Density (per km²)','GrowthRate','World Population Percentage','Rank'],axis=1,inplace=True)
      df=df.T
      df=df.reset_index().rename(columns={1:'population','index':'year'}) 
      df=df.iloc[1:,:]
      
      #dividing the datasets into x and y, ie : x is independent and y is dependent
      x = df.iloc[:, 0].values.reshape(-1,1)
      y = df.iloc[:, 1].values.reshape(-1,1)
        
      #training the dataset
      model = LinearRegression().fit(x,y)
        
      #retrieving the output
      print("Estimated population using Linear Regression model is :"+str(int(model.coef_[0][0] * year + model.intercept_[0])))
        
    else:
        print('kindly check the name or the country data isnt available \n')
        
  # Calling LR() function to take the input and print the output
  
  LR()
  
  
