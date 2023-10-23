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
    avg_prices = pd.read_csv(r'E:\Jun EV Task\Correlation_Analysis\CSVs\avg_price_by_type.csv')
    print(avg_prices)

    # Exclude data points where both x and y values are 0 for NUM_PHEV and AVG_PRICE_PHEV
    avg_prices_phev = avg_prices[(avg_prices['NUM_PHEV'] != 0) | (avg_prices['AVG_PRICE_PHEV'] != 0)]

    # Calculate correlations for NUM_PHEV and AVG_PRICE_PHEV
    corr_phev, corr_phev_pvalue = pearsonr(avg_prices_phev['NUM_PHEV'], avg_prices_phev['AVG_PRICE_PHEV'])
    corr_phev = round(corr_phev, 4) 
    print("\nThe Pearson Correlation Coefficient for number of PHEV and Average Price by Zipcode:", corr_phev)
    print("The corresponding P-value:", corr_phev_pvalue)

    # Create the scatter plot for NUM_PHEV and AVG_PRICE_PHEV
    plt.scatter(avg_prices_phev['AVG_PRICE_PHEV'], avg_prices_phev['NUM_PHEV'])
    
    # Add labels and title
    plt.xlabel('Average Price of PHEV Vehicles')
    plt.ylabel('Number of PHEV Vehicles')
    plt.title('Scatter Plot of Average PHEV Price vs. Number of PHEV Vehicles')
    
    # Show the plot
    plt.show()

    # Exclude data points where both x and y values are 0 for NUM_BEV and AVG_PRICE_BEV
    avg_prices_bev = avg_prices[(avg_prices['NUM_BEV'] != 0) | (avg_prices['AVG_PRICE_BEV'] != 0)]

    # Calculate correlations for NUM_BEV and AVG_PRICE_BEV
    corr_bev, corr_bev_pvalue = pearsonr(avg_prices_bev['NUM_BEV'], avg_prices_bev['AVG_PRICE_BEV'])
    corr_bev = round(corr_bev, 4) 
    print("\nThe Pearson Correlation Coefficient for number of BEV and Average Price by Zipcode:", corr_bev)
    print("The corresponding P-value:", corr_bev_pvalue)

    # Create the scatter plot for NUM_BEV and AVG_PRICE_BEV
    plt.scatter(avg_prices_bev['AVG_PRICE_BEV'], avg_prices_bev['NUM_BEV'])
    plt.xlabel('Average Price of BEV Vehicles')
    plt.ylabel('Number of BEV Vehicles')
    plt.title('Scatter Plot of Average BEV Price vs. Number of BEV Vehicles')
    plt.show()

    # Exclude data points where both x and y values are 0 for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    avg_prices_total = avg_prices[(avg_prices['NUM_TOTAL_EV'] != 0) | (avg_prices['AVG_PRICE_TOTAL_EV'] != 0)]

    # Calculate correlations for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    corr_total, corr_total_pvalue = pearsonr(avg_prices_total['NUM_TOTAL_EV'], avg_prices_total['AVG_PRICE_TOTAL_EV'])
    corr_total = round(corr_total, 4) 
    print("\nThe Pearson Correlation Coefficient for total vehicles and Average Price by Zipcode:", corr_total)
    print("The corresponding P-value:", corr_total_pvalue)

    # Create the scatter plot for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    plt.scatter(avg_prices_total['AVG_PRICE_TOTAL_EV'], avg_prices_total['NUM_TOTAL_EV'])
    plt.xlabel('Average Price of TOTAL EV Vehicles')
    plt.ylabel('Number of TOTAL EV Vehicles')
    plt.title('Scatter Plot of Overall Average Price vs. Number of TOTAL EV Vehicles')
    plt.show()

if __name__ == '__main__':
    main()
