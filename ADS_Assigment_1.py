# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:01:45 2023

@author: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Read the files into dataframes



df_gdp = pd.read_excel("Popular_Indicators.xlsx")
print (df_gdp)

def LinePlot(Country1,Country2,Country3,Country4) :

    """"Plotting four countries with labels"""
    plt.figure()
    # plot the four countries with labels
    plt.plot(df_gdp["YEAR"], df_gdp[Country1], label=Country1)
    plt.plot(df_gdp["YEAR"], df_gdp[Country2], label=Country2)
    plt.plot(df_gdp["YEAR"], df_gdp[Country3], label=Country3)
    plt.plot(df_gdp["YEAR"], df_gdp[Country4], label=Country4)
    
    #Setting labels and showing the legends
    plt.xlim(2005,2015)
    plt.ylim(0,25)
    plt.xlabel("% of GDP from 2005 to 2015")
    plt.ylabel("% of GDP")
    plt.title("Percentage of GDP Growth Annual") 
    plt.legend(title="COUNTRIRES",edgecolor = "brown")#coloring the boundary
    plt.savefig("LinePlot.png")#Saving the line plot
    plt.show()
    return  

LinePlot("Afghanistan","Australia","India","Sri Lanka")    

def BarPlot(Width,Height):
    
    data_Bar = pd.read_excel("uk_paper_production.xlsx")
    print(data_Bar)
    plt.figure(figsize=(Width,Height))
    data_Bar.plot(x='Year', kind='bar')
    plt.ylim(0,87)
    plt.title('Uk papaer production 2015-2019')
    plt.xlabel("Year")
    plt.ylabel("production (thousand tonnes)")
    plt.legend(title="COUNTRIRS",edgecolor = "Black",loc = "upper right")
    plt.show()
    return

BarPlot(10,8)

def PieGraph(GDP):

    IMR= pd.read_excel("export_2016.xlsx")
    print(IMR)
    
    # pie chart for the seven countries
    
    plt.figure()
    plt.pie(IMR[GDP], labels = IMR['country'], autopct='%1.1f%%' , pctdistance = 0.5 , 
       labeldistance = 1.1,wedgeprops = {'linewidth' : 1.0,'edgecolor' : 'white'} )
    
    
    plt.title("Percenteage of Export of Goods and Services ")
    plt.savefig("Barplot.png")
    plt.figure()
    plt.show()
    
    return


PieGraph("2005")
PieGraph("2016")