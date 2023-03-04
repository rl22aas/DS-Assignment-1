#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 04:03:28 2023

@author: rimsha
"""


import pandas as pd
import matplotlib.pyplot as plt


def pieplot_compare_death_cause(data):
    """
    Parameters
    ----------
    data : DataFrame
        Data representing death causes and counts.

    Returns
    -------
    None.
    
    """
    data.set_index('Cause', inplace=True)
    death_counts = data['Deaths']
    death_counts_percenage = (death_counts / death_counts.sum()) * 100
    top_5_death_causes = death_counts_percenage[:5]
    top_5_death_causes['Others'] = sum(death_counts_percenage[5:])
    plt.pie(top_5_death_causes, labels=top_5_death_causes.index, 
            autopct='%1.1f%%', startangle=90)
    plt.title('Top 5 death causes')
    plt.axis('equal')
    
    plt.show()
    

def bar_plot(data):
    """
    Parameters
    ----------
    data : DataFrame
        Panda's DataFrame holding the corona cases data worldwide.
    Returns
    -------
    None.
    """
    # Create a copy of data
    corona_data = data.copy()
    # Set country name as the index of corona_data
    corona_data.set_index("Country Name", inplace=True)
    death_counts = corona_data['Total Deaths']
    bar = death_counts.plot(kind='bar')
    bar.set_xlabel("Country")
    bar.set_ylabel("No. of Deaths")
    bar.set_title("Total Number of Deaths in Some Countries due to Corona")
    plt.show()
    

def line_plot(data):
    """
    Parameters
    ----------
    data : DataFrame
        Data to display line graph for model prices in USA.

    Returns
    -------
    None.

    """
    # Create a copy of paramter data 
    car_data = data.copy()
    
    # Get all unique car models from dataset
    unique_models = car_data['model'].unique()
    
    df = pd.DataFrame()
    df['year'] = car_data['year'].unique()
    df.set_index('year', inplace=True)
    
    # Create a columns for each of the model on the name of that model
    for model in unique_models:
        model_data = car_data.loc[car_data['model'] == model]
        model_data.set_index('year', inplace=True)
        model_data = model_data['price']
        model_data = model_data[~model_data.index.duplicated(keep='first')]
        df[model] = model_data
    df = df.sort_index()
    df = df.dropna()
    for model in df.columns:
        plt.plot(df.index, df[model], label=model)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel("Car Models")
    plt.title("Car prices in USA")
    plt.show()
    
    


# Read data from csv file
# Resource: https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates/ghe-leading-causes-of-death
who_data = pd.read_csv(r'C:\Users\profesoor\Desktop\ds_assignment/' + 
                       'Leading-Causes-of-Death.csv')

who_data = pd.DataFrame(who_data)
# sort data according to the number of deaths
who_data = who_data.sort_values("Deaths", ascending=False)

pieplot_compare_death_cause(who_data)


# Read corona virus dataset
# Resourcehttps://www.kaggle.com/datasets/sunayanagawde/countrywise-covid-cases
corona_data = pd.read_csv(r'C:\Users\profesoor\Desktop\ds_assignment/' + 
                       'Country-wise-COVID-cases.csv')
corona_data = pd.DataFrame(corona_data)

bar_plot(corona_data.loc[:30, :])


# Read US car prices dataset
#Resource: https://www.kaggle.com/datasets/at3191/us-car-prices
car_prices = pd.read_csv(r'C:\Users\profesoor\Desktop\ds_assignment/' + 
                       'car_prices.csv')

car_prices = pd.DataFrame(car_prices)
line_plot(car_prices)










