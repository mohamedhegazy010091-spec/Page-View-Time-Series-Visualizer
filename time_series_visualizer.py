# import liberaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data from csv file
data = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'],index_col='date')
# print(data.head())

#  Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
lower = data['value'].quantile(0.025) # 2.5th percentile
upper = data['value'].quantile(0.975) # 97.5th percentile
data_cleaned = data[(data['value']>=lower) & (data['value']<=upper)]
print(data_cleaned.head())  

# Draw line plot
def draw_line_plot():
    plt.figure(figsize=(15,5)) # set the figure size
    plt.plot(data_cleaned.index,data_cleaned['value'],color='red') # plot the line plot
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019') # set the title
    plt.xlabel('Date') # set the x label
    plt.ylabel('Page Views') # set the y label
    return plt.show() 
draw_line_plot() 

# Draw bar plot
def draw_bar_plot():
    df_bar = data_cleaned.copy() # copy the cleaned data
    df_bar['Year'] = df_bar.index.year # extract year from the index
    df_bar['Month'] = df_bar.index.month_name()  # extract month name from the index
    # group by year and month and calculate the mean
    df_bar_grouped = df_bar.groupby(['Year','Month'])['value'].mean().unstack()
    df_bar_grouped = df_bar_grouped[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]
    df_bar_grouped.plot(kind='bar', figsize=(10,7))
    plt.xlabel('Years') # set the x label
    plt.ylabel('Average Page Views') # set the y label  
    plt.legend(title='Months') # set the legend title
    return plt.show()
draw_bar_plot()

# Draw box plots
def draw_box_plot():    
    df_box = data_cleaned.copy() # copy the cleaned data
    df_box.reset_index(inplace=True) # reset the index
    df_box['Year'] = df_box['date'].dt.year # extract year from the date
    df_box['Month'] = df_box['date'].dt.strftime('%b') # extract month abbreviation from the date
    # order the months correctly
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.figure(figsize=(15,5)) # set the figure size
    # create year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='Year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    # create month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='Month', y='value', data=df_box, order=month_order)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    return plt.show()
draw_box_plot()