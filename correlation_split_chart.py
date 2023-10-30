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

    avg_prices = pd.read_csv(r'/Users/tigris/Documents/UI Lab/Jun EV Task/Correlation_Analysis/Above 5000/top6.csv')
    print(avg_prices)

# PHEV
# -----------------------

    # Exclude data points where both x and y values are 0 for NUM_PHEV and AVG_PRICE_PHEV
    avg_prices_phev = avg_prices[(avg_prices['NUM_PHEV'] != 0) & (avg_prices['AVG_PRICE_PHEV'] != 0)]

    # Calculate the mean of 'AVG_PRICE_PHEV'
    mean_phev = avg_prices_phev['AVG_PRICE_PHEV'].mean()

    # Create a DataFrame for data before or equal to the mean
    data_before_mean = avg_prices_phev[avg_prices_phev['AVG_PRICE_PHEV'] <= mean_phev]

    # Create a DataFrame for data after the mean
    data_after_mean = avg_prices_phev[avg_prices_phev['AVG_PRICE_PHEV'] > mean_phev]

    # Calculate correlations for data before and after the mean
    corr_before_mean, corr_before_mean_pvalue = pearsonr(data_before_mean['NUM_PHEV'], data_before_mean['AVG_PRICE_PHEV'])
    corr_after_mean, corr_after_mean_pvalue = pearsonr(data_after_mean['NUM_PHEV'], data_after_mean['AVG_PRICE_PHEV'])

    corr_before_mean = round(corr_before_mean, 4)
    corr_after_mean = round(corr_after_mean, 4)

    # Print correlation figures
    print("\nCorrelation for PHEV data before or equal to the mean:")
    print(f"Pearson Correlation Coefficient: {corr_before_mean}")
    print(f"Corresponding P-value: {corr_before_mean_pvalue}")

    print("\nCorrelation for PHEV data after the mean:")
    print(f"Pearson Correlation Coefficient: {corr_after_mean}")
    print(f"Corresponding P-value: {corr_after_mean_pvalue}")

    # BEFORE MEAN:

    # Create the first chart for data before or equal to the mean
    fig, ax1 = plt.subplots()
    ax1.set_facecolor('#16253B')
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart
    ax1.scatter(data_before_mean['AVG_PRICE_PHEV'], data_before_mean['NUM_PHEV'], s=10, color='#99F7AB')
    ax1.axvline(mean_phev, color='#CE2D4F', linestyle='-', label='Mean')
    ax1.set_xlabel('Average Price of PHEV Vehicles', labelpad=10)
    ax1.set_ylabel('Number of PHEV Vehicles', labelpad=10)
    ax1.set_title('Average PHEV Price vs. Number of PHEV Vehicles (Before Mean)', pad=20)

    # Before Mean Styling:

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax1.xaxis.label.set_color('#A5C4D4')
    ax1.yaxis.label.set_color('#A5C4D4')
    ax1.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax1.spines['left'].set_color('#A5C4D4')
    ax1.spines['bottom'].set_color('#A5C4D4')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax1.tick_params(axis='x', colors='#A5C4D4')
    ax1.tick_params(axis='y', colors='#A5C4D4')

    # Show Legend with a white text color
    legend = ax1.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')   

    # # Save Plot
    # fig.savefig('b4_mean_PHEV.svg', format='svg', dpi=1200)

    # AFTER MEAN:

    # Create the second chart for data after the mean
    fig, ax2 = plt.subplots()
    ax2.set_facecolor('#16253B')
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart
    ax2.scatter(data_after_mean['AVG_PRICE_PHEV'], data_after_mean['NUM_PHEV'], s=10, color='#99F7AB')
    ax2.axvline(mean_phev, color='#CE2D4F', linestyle='-', label='Mean')
    ax2.set_xlabel('Average Price of PHEV Vehicles', labelpad=10)
    ax2.set_ylabel('Number of PHEV Vehicles', labelpad=10)
    ax2.set_title('Average PHEV Price vs. Number of PHEV Vehicles (After Mean)', pad=20)

    # After Mean Styling:

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax2.xaxis.label.set_color('#A5C4D4')
    ax2.yaxis.label.set_color('#A5C4D4')
    ax2.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax2.spines['left'].set_color('#A5C4D4')
    ax2.spines['bottom'].set_color('#A5C4D4')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax2.tick_params(axis='x', colors='#A5C4D4')
    ax2.tick_params(axis='y', colors='#A5C4D4')

    # Show Legend with a white text color
    legend = ax2.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')  

    # # Save Plot
    # fig.savefig('after_mean_PHEV.svg', format='svg', dpi=1200) 

    # Show both plots
    plt.show()


# # BEV
# # -----------------------

    # Exclude data points where both x and y values are 0 for NUM_BEV and AVG_PRICE_BEV
    avg_prices_bev = avg_prices[(avg_prices['NUM_BEV'] != 0) & (avg_prices['AVG_PRICE_BEV'] != 0)]

    # Filter data for price in the BEV Chart: x < 110000
    avg_prices_bev = avg_prices_bev[(avg_prices_bev['AVG_PRICE_BEV'] < 110000)]

    # Calculate the mean of 'AVG_PRICE_BEV'
    mean_bev = avg_prices_bev['AVG_PRICE_BEV'].mean()

    # Create a DataFrame for data before or equal to the mean
    data_before_mean = avg_prices_bev[avg_prices_bev['AVG_PRICE_BEV'] <= mean_bev]

    # Create a DataFrame for data after the mean
    data_after_mean = avg_prices_bev[avg_prices_bev['AVG_PRICE_BEV'] > mean_bev]

    # Calculate correlations for data before and after the mean
    corr_before_mean, corr_before_mean_pvalue = pearsonr(data_before_mean['NUM_BEV'], data_before_mean['AVG_PRICE_BEV'])
    corr_after_mean, corr_after_mean_pvalue = pearsonr(data_after_mean['NUM_BEV'], data_after_mean['AVG_PRICE_BEV'])

    corr_before_mean = round(corr_before_mean, 4)
    corr_after_mean = round(corr_after_mean, 4)

    # Print correlation figures
    print("\nCorrelation for BEV data before or equal to the mean:")
    print(f"Pearson Correlation Coefficient: {corr_before_mean}")
    print(f"Corresponding P-value: {corr_before_mean_pvalue}")

    print("\nCorrelation for BEV data after the mean:")
    print(f"Pearson Correlation Coefficient: {corr_after_mean}")
    print(f"Corresponding P-value: {corr_after_mean_pvalue}")

    # BEFORE MEAN:

    # Create the first chart for data before or equal to the mean
    fig, ax1 = plt.subplots()
    ax1.set_facecolor('#16253B')
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart
    ax1.scatter(data_before_mean['AVG_PRICE_BEV'], data_before_mean['NUM_BEV'], s=10, color='#99F7AB')
    ax1.axvline(mean_bev, color='#CE2D4F', linestyle='-', label='Mean')
    ax1.set_xlabel('Average Price of BEV Vehicles', labelpad=10)
    ax1.set_ylabel('Number of BEV Vehicles', labelpad=10)
    ax1.set_title('Average BEV Price vs. Number of BEV Vehicles (Before Mean)', pad=20)

    # Before Mean Styling:

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax1.xaxis.label.set_color('#A5C4D4')
    ax1.yaxis.label.set_color('#A5C4D4')
    ax1.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax1.spines['left'].set_color('#A5C4D4')
    ax1.spines['bottom'].set_color('#A5C4D4')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax1.tick_params(axis='x', colors='#A5C4D4')
    ax1.tick_params(axis='y', colors='#A5C4D4')

    # Show Legend with a white text color
    legend = ax1.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')  

    # # Save Plot
    # fig.savefig('b4_mean_BEV.svg', format='svg', dpi=1200)  

    # AFTER MEAN:

    # Create the second chart for data after the mean
    fig, ax2 = plt.subplots()
    ax2.set_facecolor('#16253B')
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart
    ax2.scatter(data_after_mean['AVG_PRICE_BEV'], data_after_mean['NUM_BEV'], s=10, color='#99F7AB')
    ax2.axvline(mean_bev, color='#CE2D4F', linestyle='-', label='Mean')
    ax2.set_xlabel('Average Price of BEV Vehicles', labelpad=10)
    ax2.set_ylabel('Number of BEV Vehicles', labelpad=10)
    ax2.set_title('Average BEV Price vs. Number of BEV Vehicles (After Mean)', pad=20)

    # After Mean Styling:

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax2.xaxis.label.set_color('#A5C4D4')
    ax2.yaxis.label.set_color('#A5C4D4')
    ax2.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax2.spines['left'].set_color('#A5C4D4')
    ax2.spines['bottom'].set_color('#A5C4D4')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax2.tick_params(axis='x', colors='#A5C4D4')
    ax2.tick_params(axis='y', colors='#A5C4D4')

    # Show Legend with a white text color
    legend = ax2.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')   

    # # Save Plot
    # fig.savefig('after_mean_BEV.svg', format='svg', dpi=1200) 

    # Show both plots
    plt.show()

    # # Save Plot
    # fig.savefig('BEV.svg', format='svg', dpi=1200)
    # # fig.savefig('BEV.png', format='png', dpi=1200)

# # Total
# # -----------------------
# NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV

    # Exclude data points where both x and y values are 0 for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    avg_prices_total = avg_prices[(avg_prices['NUM_TOTAL_EV'] != 0) & (avg_prices['AVG_PRICE_TOTAL_EV'] != 0)]

    # Filter data for price in the total EV Chart: x < 110000
    avg_prices_total = avg_prices_total[(avg_prices_total['AVG_PRICE_TOTAL_EV'] < 110000)]

    # Calculate the mean of 'AVG_PRICE_TOTAL_EV'
    mean_total = avg_prices_total['AVG_PRICE_TOTAL_EV'].mean()

    # Create a DataFrame for data before or equal to the mean
    data_before_mean = avg_prices_total[avg_prices_total['AVG_PRICE_TOTAL_EV'] <= mean_total]

    # Create a DataFrame for data after the mean
    data_after_mean = avg_prices_total[avg_prices_total['AVG_PRICE_TOTAL_EV'] > mean_total]

    # Calculate correlations for data before and after the mean
    corr_before_mean, corr_before_mean_pvalue = pearsonr(data_before_mean['NUM_TOTAL_EV'], data_before_mean['AVG_PRICE_TOTAL_EV'])
    corr_after_mean, corr_after_mean_pvalue = pearsonr(data_after_mean['NUM_TOTAL_EV'], data_after_mean['AVG_PRICE_TOTAL_EV'])

    corr_before_mean = round(corr_before_mean, 4)
    corr_after_mean = round(corr_after_mean, 4)

    # Print correlation figures
    print("\nCorrelation for Total EV data before or equal to the mean:")
    print(f"Pearson Correlation Coefficient: {corr_before_mean}")
    print(f"Corresponding P-value: {corr_before_mean_pvalue}")

    print("\nCorrelation for Total EV data after the mean:")
    print(f"Pearson Correlation Coefficient: {corr_after_mean}")
    print(f"Corresponding P-value: {corr_after_mean_pvalue}")

    # BEFORE MEAN:

    # Create the first chart for data before or equal to the mean
    fig, ax1 = plt.subplots()
    ax1.set_facecolor('#16253B')
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart
    ax1.scatter(data_before_mean['AVG_PRICE_TOTAL_EV'], data_before_mean['NUM_TOTAL_EV'], s=10, color='#99F7AB')
    ax1.axvline(mean_total, color='#CE2D4F', linestyle='-', label='Mean')
    ax1.set_xlabel('Average Price of Total Vehicles', labelpad=10)
    ax1.set_ylabel('Number of Total Vehicles', labelpad=10)
    ax1.set_title('Average Total Price vs. Number of Total Vehicles (Before Mean)', pad=20)

    # Before Mean Styling:

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax1.xaxis.label.set_color('#A5C4D4')
    ax1.yaxis.label.set_color('#A5C4D4')
    ax1.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax1.spines['left'].set_color('#A5C4D4')
    ax1.spines['bottom'].set_color('#A5C4D4')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax1.tick_params(axis='x', colors='#A5C4D4')
    ax1.tick_params(axis='y', colors='#A5C4D4')

    # Show Legend with a white text color
    legend = ax1.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')  

    # # Save Plot
    # fig.savefig('b4_mean_total.svg', format='svg', dpi=1200)  

    # AFTER MEAN:

    # Create the second chart for data after the mean
    fig, ax2 = plt.subplots()
    ax2.set_facecolor('#16253B')
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart
    ax2.scatter(data_after_mean['AVG_PRICE_TOTAL_EV'], data_after_mean['NUM_TOTAL_EV'], s=10, color='#99F7AB')
    ax2.axvline(mean_total, color='#CE2D4F', linestyle='-', label='Mean')
    ax2.set_xlabel('Average Price of Total Vehicles', labelpad=10)
    ax2.set_ylabel('Number of Total Vehicles', labelpad=10)
    ax2.set_title('Average Total Price vs. Number of Total Vehicles (After Mean)', pad=20)

    # After Mean Styling:

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax2.xaxis.label.set_color('#A5C4D4')
    ax2.yaxis.label.set_color('#A5C4D4')
    ax2.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax2.spines['left'].set_color('#A5C4D4')
    ax2.spines['bottom'].set_color('#A5C4D4')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax2.tick_params(axis='x', colors='#A5C4D4')
    ax2.tick_params(axis='y', colors='#A5C4D4')

    # Show Legend with a white text color
    legend = ax2.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4') 

    # # Save Plot
    # fig.savefig('after_mean_total.svg', format='svg', dpi=1200)    

    # Show both plots
    plt.show()

if __name__ == '__main__':
    main()
