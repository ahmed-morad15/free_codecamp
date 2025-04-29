import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import the dataset from CSV
df = pd.read_csv('epa-sea-level.csv')

def draw_scatter_plot():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

def plot_best_fit_line():
    # Line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Plot the line of best fit for the entire dataset
    years_extended = range(1880, 2051)  # Extend the year range up to 2050
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], color='red', label='Best Fit Line (1880-2050)')

def plot_recent_best_fit_line():
    # Filter data from the year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    
    # Line of best fit for data since 2000
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Plot the line of best fit for the recent data
    years_extended = range(1880, 2051)
    plt.plot(years_extended, [slope_recent * year + intercept_recent for year in years_extended], color='green', label='Best Fit Line (2000-2050)')

def finalize_plot():
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add a legend
    plt.legend()
    
    # Save the plot to a file
    plt.savefig('sea_level_rise.png')
    plt.show()

# Main function to run all tasks
def main():
    draw_scatter_plot()
    plot_best_fit_line()
    plot_recent_best_fit_line()
    finalize_plot()
