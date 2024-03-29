import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    file_path = input("Please Enter File Path : ")
    if(file_path[-1] == "n"):
        data = pd.read_json(file_path)
	return data
    elif(file_path[-1] == "v"):
        data = pd.read_csv(file_path)
	return data
    elif(file_path[-1] == "x"):
        data = pd.read_xlsx(file_path)
	return data
    else:
        print("This File Isn't Valid")

def data_summary(data,target_row):
    data.info()
    #general information about the whole table colums and more
    data.describe() 
    #the most repieted value in one of the columns
    data[target_row].mode() 
    #the mean for one of the colums using pandas
    data[target_row].mean()
    #the mean for one of the colums using numpy
    np.mean(data[target_row]) 
    # to know the greatest value in the colum usign numpy
    np.max(data[target_row]) 
    # to know the smallest value in the colum usign numpy
    np.min(data[target_row]) 
    #to know how much is the values and how much it repeated
    data[target_row].value_counts() 


def clear_missing(data):
    print("First The Empty Rows is \n")
    empty_rows = data[data.isnull().any(axis=1)]
    ans = input("Do you wanna delete or fill the empty cells (D/F): ")
    if(ans == "D"):
        data = data.dropna()
    if(ans == "F"):
        fill = input("you wanna fill it with : ")
        data = data.fillna(fill)

def  categorys(data,categ):
    data.groupby(categ).describe()
    




        
    

    
    
    