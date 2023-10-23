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
#pearsonr returns the corr. and a 2-tailed p-value.

def main():
    avg_prices = pd.read_csv(r'E:\Jun EV Task\Correlation_Analysis\CSVs\avg_price_by_type.csv')
    print(avg_prices)
    
    corr_phev, corr_phev_pvalue = pearsonr(avg_prices['NUM_PHEV'], avg_prices['AVG_PRICE_PHEV'])
    corr_bev, corr_bev_pvalue = pearsonr(avg_prices['NUM_BEV'], avg_prices['AVG_PRICE_BEV'])
    corr_hev, corr_hev_pvalue = pearsonr(avg_prices['NUM_HEV'], avg_prices['AVG_PRICE_HEV'])
    corr_total, corr_total_pvalue = pearsonr(avg_prices['NUM_TOTAL_EV'], avg_prices['AVG_PRICE_TOTAL_EV'])

    print("The Pearson Correlation Coefficient for number of PHEV and Average Price by Zipcode:", corr_phev)
    print("The corresponding P-value:", corr_phev_pvalue)

    print("The Pearson Correlation Coefficient for number of BEV and Average Price by Zipcode:", corr_bev)
    print("The corresponding P-value:", corr_bev_pvalue)

    # print("The Pearson Correlation Coefficient for number of PHEV and Average Price by Zipcode:", corr_hev)
    # print("The corresponding P-value:", corr_hev_pvalue)

    print("The Pearson Correlation Coefficient total vehicles and Average Price by Zipcode:", corr_total)
    print("The corresponding P-value:", corr_total_pvalue)

    #################################################
    # Charting
    #################################################

    #AVERAGE PHEV PRICE V. NUM PHEV
    # Create the scatter plot with flipped axes
    plt.scatter(avg_prices['AVG_PRICE_PHEV'], avg_prices['NUM_PHEV'])
    
    # Add labels and title
    plt.xlabel('Average Price of PHEV Vehicles')
    plt.ylabel('Number of PHEV Vehicles')
    plt.title('Scatter Plot of Average PHEV Price vs. Number of PHEV Vehicles')
    
    # Show the plot
    plt.show()

    # AVERAGE BEV PRICE V NUM PHEV
    # Create the scatter plot with flipped axes
    plt.scatter(avg_prices['AVG_PRICE_BEV'], avg_prices['NUM_BEV'])
    
    # Add labels and title
    plt.xlabel('Average Price of BEV Vehicles')
    plt.ylabel('Number of BEV Vehicles')
    plt.title('Scatter Plot of Average BEV Price vs. Number of BEV Vehicles')
    
    # Show the plot
    plt.show()

    # AVERAGE TOTAL PRICE V NUM TOTAL
    # Create the scatter plot with flipped axes
    plt.scatter(avg_prices['AVG_PRICE_PHEV'], avg_prices['NUM_PHEV'])
    
    # Add labels and title
    plt.xlabel('Average Price of TOTAL EV Vehicles')
    plt.ylabel('Number of TOTAL EV Vehicles')
    plt.title('Scatter Plot of Overall Average Price vs. Number of TOTAL EV Vehicles')
    
    # Show the plot
    plt.show()

if __name__ == '__main__':
    main()