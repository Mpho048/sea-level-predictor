import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np 

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df.info()
    
    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    print(df.columns.to_list())
    fig,ax = plt.subplots()
    plt.scatter(x,y)


    # Create first line of best fit
    reg = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred =  reg.slope * x_pred  + reg.intercept
    plt.plot(x_pred,y_pred,"r",label = "Best Fit 1880-2050",linewidth =2)


    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    reg_recent = linregress(df_recent["Year"],df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series([ i for i in range(2000,2051)])
    y_recent = reg_recent. slope * x_recent + reg_recent.intercept
    plt.plot(x_recent,y_recent,"blue",label = "Best Fit 2000-2050",linewidth=2)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    plt.xlim(1870,2060)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    
    
draw_plot()