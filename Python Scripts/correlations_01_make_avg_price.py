# Name : Tigris Mendez
# Organization: UT Austin Urban Information lab
# Affiliation: Undergraduate Research Assistant
# Data Created: 10/7/2023
# Description : My goal is to leverage a CSV file to understand the correlation
#               of Types of Hybrid or Electrical Vehicles and their price.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def main():
    avg_prices = pd.read_csv(r'/Volumes/ESD-USB/Jun EV Task/Correlation_Analysis/CSVs/avg_price_by_type_make_only.csv')
    print(avg_prices)

    # Exclude data points where both x and y values are 0 for NUM_PHEV and AVG_PRICE_PHEV
    avg_prices_phev = avg_prices[(avg_prices['NUM_PHEV'] != 0) | (avg_prices['AVG_PRICE_PHEV'] != 0)]

    # Filter data for the PHEV chart: 5000 < AVG_PRICE_PHEV < 100000
    avg_prices_phev = avg_prices_phev[(avg_prices_phev['AVG_PRICE_PHEV'] > 5000) & (avg_prices_phev['AVG_PRICE_PHEV'] < 100000)]

    # Calculate correlations for NUM_PHEV and AVG_PRICE_PHEV
    corr_phev, corr_phev_pvalue = pearsonr(avg_prices_phev['NUM_PHEV'], avg_prices_phev['AVG_PRICE_PHEV'])
    corr_phev = round(corr_phev, 4)
    print("\nThe Pearson Correlation Coefficient for number of PHEV and Average Price by Zipcode:", corr_phev)
    print("The corresponding P-value:", corr_phev_pvalue)

    # Calculate mean and median for AVG_PRICE_PHEV
    mean_phev = avg_prices_phev['AVG_PRICE_PHEV'].mean()
    median_phev = avg_prices_phev['AVG_PRICE_PHEV'].median()

    # Create the scatter plot for NUM_PHEV and AVG_PRICE_PHEV
    plt.scatter(avg_prices_phev['AVG_PRICE_PHEV'], avg_prices_phev['NUM_PHEV'])

    # Add vertical lines for mean and median
    plt.axvline(mean_phev, color='red', linestyle='--', label='Mean')
    plt.axvline(median_phev, color='green', linestyle='--', label='Median')

    # Calculate and plot the best-fit line
    x_phev = avg_prices_phev['AVG_PRICE_PHEV']
    y_phev = avg_prices_phev['NUM_PHEV']
    coefficients_phev = np.polyfit(x_phev, y_phev, 1)  # Fit a linear regression line
    best_fit_line_phev = np.poly1d(coefficients_phev)
    plt.plot(x_phev, best_fit_line_phev(x_phev), color='blue', label='Best Fit Line')

    # Add labels and title
    plt.xlabel('Average Price of PHEV Vehicles')
    plt.ylabel('Number of PHEV Vehicles')
    plt.title('Scatter Plot of Average PHEV Price vs. Number of PHEV Vehicles')

    # Show the legend
    plt.legend()

    # Show the plot
    plt.show()

    # Exclude data points where both x and y values are 0 for NUM_BEV and AVG_PRICE_BEV
    avg_prices_bev = avg_prices[(avg_prices['NUM_BEV'] != 0) | (avg_prices['AVG_PRICE_BEV'] != 0)]


    # Filter data for the BEV chart: 5000 < AVG_PRICE_BEV < 125000
    avg_prices_bev = avg_prices[(avg_prices['AVG_PRICE_BEV'] > 5000) & (avg_prices['AVG_PRICE_BEV'] < 125000)]

    # Calculate correlations for NUM_BEV and AVG_PRICE_BEV
    corr_bev, corr_bev_pvalue = pearsonr(avg_prices_bev['NUM_BEV'], avg_prices_bev['AVG_PRICE_BEV'])
    corr_bev = round(corr_bev, 4) 
    print("\nThe Pearson Correlation Coefficient for number of BEV and Average Price by Zipcode:", corr_bev)
    print("The corresponding P-value:", corr_bev_pvalue)

    # Calculate mean and median for AVG_PRICE_PHEV
    mean_bev = avg_prices_bev['AVG_PRICE_BEV'].mean()
    median_bev = avg_prices_bev['AVG_PRICE_BEV'].median()

    # Create the scatter plot for NUM_BEV and AVG_PRICE_BEV
    plt.scatter(avg_prices_bev['AVG_PRICE_BEV'], avg_prices_bev['NUM_BEV'])

    # Add vertical lines for mean and median
    plt.axvline(mean_bev, color='red', linestyle='--', label='Mean')
    plt.axvline(median_bev, color='green', linestyle='--', label='Median')

    plt.xlabel('Average Price of BEV Vehicles')
    plt.ylabel('Number of BEV Vehicles')
    plt.title('Scatter Plot of Average BEV Price vs. Number of BEV Vehicles')

    # Calculate and plot the best-fit line
    x_bev = avg_prices_bev['AVG_PRICE_BEV']
    y_bev = avg_prices_bev['NUM_BEV']
    coefficients_bev = np.polyfit(x_bev, y_bev, 1)  # Fit a linear regression line
    best_fit_line_bev = np.poly1d(coefficients_bev)
    plt.plot(x_bev, best_fit_line_bev(x_bev), color='blue', label='Best Fit Line')

    # Show the legend + show chart
    plt.legend()
    plt.show()

    # Exclude data points where both x and y values are 0 for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    avg_prices_total = avg_prices[(avg_prices['NUM_TOTAL_EV'] != 0) | (avg_prices['AVG_PRICE_TOTAL_EV'] != 0)]

    # Filter data for prices in the Total EV chart: x < 100000
    avg_prices_total = avg_prices[(avg_prices['AVG_PRICE_TOTAL_EV'] < 110000)]

    # Calculate correlations for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    corr_total, corr_total_pvalue = pearsonr(avg_prices_total['NUM_TOTAL_EV'], avg_prices_total['AVG_PRICE_TOTAL_EV'])
    corr_total = round(corr_total, 4) 
    print("\nThe Pearson Correlation Coefficient for total vehicles and Average Price by Zipcode:", corr_total)
    print("The corresponding P-value:", corr_total_pvalue)

    # Calculate mean and median for AVG_PRICE_PHEV
    mean_total_ev = avg_prices_phev['AVG_PRICE_TOTAL_EV'].mean()
    median_total_ev = avg_prices_phev['AVG_PRICE_TOTAL_EV'].median()

    # Create the scatter plot for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    plt.scatter(avg_prices_total['AVG_PRICE_TOTAL_EV'], avg_prices_total['NUM_TOTAL_EV'])

    # Add vertical lines for mean and median
    plt.axvline(mean_total_ev, color='red', linestyle='--', label='Mean')
    plt.axvline(median_total_ev, color='green', linestyle='--', label='Median')

    plt.xlabel('Average Price of TOTAL EV Vehicles')
    plt.ylabel('Number of TOTAL EV Vehicles')
    plt.title('Scatter Plot of Overall Average Price vs. Number of TOTAL EV Vehicles')

    # Calculate and plot the best-fit line
    x_total = avg_prices_total['AVG_PRICE_TOTAL_EV']
    y_total = avg_prices_total['NUM_TOTAL_EV']
    coefficients_total = np.polyfit(x_total, y_total, 1)  # Fit a linear regression line
    best_fit_line_total = np.poly1d(coefficients_total)
    plt.plot(x_total, best_fit_line_total(x_total), color='blue', label='Best Fit Line')


    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
