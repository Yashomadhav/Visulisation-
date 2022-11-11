# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:48:03 2022

@author: ym22aac
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


def df():
    """This is function (df) that we use to read csv file i.e.(WHO Mortality Database) for plotting line plot.
    
    Returns
    -------
    None.

    """
     
    df = pd.read_csv("WHOMortalityDatabase.csv")
    #Line plotting WHO file
    return df

def lineplot():
    """This is a function lineplot in which has no return as an argument.
    Returns
    -------
    None.

    """
    
    male = df[df['Sex'].eq('Male')]
    female = df[df['Sex'].eq('Female')]
    all_df = df[df['Sex'].eq('All')]
    unknown = df[df['Sex'].eq('Unknown')]
     
    plt.figure(dpi=144)      # For Ploting the figure 
    plt.plot( all_df['Year'], all_df['Number'], label='All')
    plt.plot( female['Year'], female['Number'], label='Female')
    plt.plot( male['Year'], male['Number'], label='Male')
    plt.plot( unknown['Year'], unknown['Number'], label='Unknown')
    plt.xticks(np.arange(2000, 2022, 2))
    plt.xlim(2000, 2020)
    plt.xlabel("Years")#showing years on x axis
    plt.ylabel("Number Of Deaths")
    plt.title("Mortality rate of Mexico")
    plt.legend()


#New dataset
def dt():
    """
    We have created this function to import new data set i.e.(Cause of deaths) database for India

    Returns
    -------
    None.

    """

    dt= pd.read_csv("cause_of_deaths.csv")#for fetching data from csv file
    print(dt)
    ind_df  = dt[dt["Code"].eq("IND")]#this function is used for extracting Indian database from world data by using country code
    ind_df
    
    ind_df.dropna#for dropping all null values
    return ind_df


# pie chart

def piechart():
    """
    We have defined this function for piechart with no argument.

    Returns
    -------
    None.

    """
    
    # We took any four deseases from the data set for plotting pie chart
    maternal_disorders= np.sum(ind_df['Maternal Disorders'])
    hiv_aids= np.sum(ind_df['HIV/AIDS'])
    chronic_kidney_disease= np.sum(ind_df['Chronic Kidney Disease'])
    tuberculosis= np.sum(ind_df['Tuberculosis'])
    
    total= maternal_disorders + hiv_aids + chronic_kidney_disease + tuberculosis
    
    mat_dis= maternal_disorders/ total*100
    aids= hiv_aids/ total*100
    ch_kidney= chronic_kidney_disease/ total*100  # Taking each percentage before plotting 
    t_b= tuberculosis/ total*100
    
    mortality= np.array([mat_dis, aids, ch_kidney, t_b])
    diseases= ['Maternal Disorders', 'HIV/AIDS', 'Chronic Kidney Disease', 'Tuberculosis']
    explode= (0.1,0,0.1,0.1)
    
    plt.figure(dpi=144)
    plt.pie(mortality, labels= diseases, shadow=True, explode= explode, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
    plt.title("Mortality rate by Diseases in India") # This function is for showing title of data
    plt.show()






#bar chart

def barchart():
    """
    This function we have used again with no argument for bar graphs.

    Returns
    -------
    None.

    """
    ind_df = dt()
    ind_df = ind_df.loc[2436:2441]  # To assign index numbers for bar plot 
    num = np.arange(6)
    width = 0.2
    print(ind_df['Year'])
    years = ind_df['Year'].tolist()  # Used (tolist) to convert array values to list 
    print(years)
    
    plt.figure(dpi=144)
    plt.title('Causes of Death in india')
    plt.bar(num, ind_df['Poisonings'], width, label='Poisonings')
    plt.bar(num+0.2, ind_df['Acute Hepatitis'], width, label='Acute Hepatitis')
    plt.bar(num-0.2, ind_df['Fire, Heat, and Hot Substances'], width, label='Fire, Heat, and Hot Substances')
    plt.bar(num+0.4, ind_df['Conflict and Terrorism'], width, label='Conflict and Terrorism')
    plt.xticks(num, years) # This is for showing years in x asis
    plt.yticks(np.arange(0,110000,10000)) # This is for setting range and jump to get desired plot
    plt.xlabel('Years')
    plt.ylabel('Number of deaths')
    plt.legend()
    plt.show()



df = df() 
# For calling function df
lineplot()
# For calling function line plot
ind_df = dt()
 # for calling function that import another data set
piechart()
 # for calling function pie chart
barchart()
 # for calling function bar chart 
