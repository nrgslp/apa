# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#define these
directory =
groupingVariable =
groupingLabel =
group1Name =
group2Name =

df = pd.read_csv(directory, 
                 sep=",", 
                 na_values='.', 
                 header = 0,)
print(df.head(5))
#plt keeps the figures in RAM; need to clear.
plt.close('all')

#define boxplot colors
apaColors = {1: "w", 2: "lightgray"}


#here's the code to make a boxplot comparing two groups
def apaBoxplot():
    plt.figure()
    sns.boxplot(
            #this plots each variable by the hardcoded group comparison variable name
            x=df[groupingVariable], 
            y=df[column], 
            palette = apaColors
    ).set(
        #these are the axis labels. The y label axis is pulled from the CSV
         xlabel=groupingLabel, 
         ylabel=column)
    x=np.arange(2)
    #it didn't like string variables in the CSV, so this overwrites group names "1" and "2"
    plt.xticks(x, (group1Name, group2Name))

#for every variable in the CSV
for column in df:
    #these statements call the apaBoxplot function and change the axis scaling depending on the variable type. Make these reasonable for your data. 
    if "Full" in column:
        apaBoxplot()
        plt.ylim(0, 10)
        plt.show
        
    elif "Percent" in column: 
        apaBoxplot()
        plt.ylim(50, 100)
        plt.show
        
    else:
        apaBoxplot()
        plt.ylim(0, 10)
        plt.show
        
