import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data and set the 'date' column as the index
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean the data by filtering out the top and bottom 2.5% of page views
lower_percentile = df['page_views'].quantile(0.025)
upper_percentile = df['page_views'].quantile(0.975)
df_cleaned = df[(df['page_views'] > lower_percentile) & (df['page_views'] < upper_percentile)]

# Line Plot function
def draw_line_plot():
    df_line = df_cleaned.copy()
    plt.figure(figsize=(12, 6))
    plt.plot(df_line.index, df_line['page_views'], color='b', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.savefig('line_plot.png')
    return plt

# Bar Plot function
def draw_bar_plot():
    df_bar = df_cleaned.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_monthly_avg = df_bar.groupby(['year', 'month'])['page_views'].mean().unstack()
    df_monthly_avg.plot(kind='bar', figsize=(12, 6), stacked=False)
    plt.title('Average Daily Page Views for Each Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.savefig('bar_plot.png')
    return plt

# Box Plot function
def draw_box_plot():
    df_box = df_cleaned.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='page_views', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.savefig('year_box_plot.png')
    plt.clf()

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='month', y='page_views', data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.savefig('month_box_plot.png')
    return plt
