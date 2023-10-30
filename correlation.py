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

    # Filter data for the PHEV chart: 5000 < AVG_PRICE_PHEV < 110000
    avg_prices_phev = avg_prices_phev[(avg_prices_phev['AVG_PRICE_PHEV'] > 1000) & (avg_prices_phev['AVG_PRICE_PHEV'] < 110000)]

    # Calculate correlations for NUM_PHEV and AVG_PRICE_PHEV
    corr_phev, corr_phev_pvalue = pearsonr(avg_prices_phev['NUM_PHEV'], avg_prices_phev['AVG_PRICE_PHEV'])
    corr_phev = round(corr_phev, 4)
    print("\nThe Pearson Correlation Coefficient for number of PHEV and Average Price by Zipcode:", corr_phev)
    print("The corresponding P-value:", corr_phev_pvalue)

    # Calculate mean for AVG_PRICE_PHEV
    mean_phev = avg_prices_phev['AVG_PRICE_PHEV'].mean()

    # PHEV STYLING:
    # ---------

    # Create a figure and axis with a specific background color (navy blue)
    fig, ax = plt.subplots()
    ax.set_facecolor('#16253B')  # Set the background color of the axis
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart

    # Create the scatter plot on the axis for NUM_PHEV and AVG_PRICE_PHEV with smaller dots
    ax.scatter(avg_prices_phev['AVG_PRICE_PHEV'], avg_prices_phev['NUM_PHEV'], s=10, color='#99F7AB') # s=10 ; dot-size , color ; dot-color

    # Add vertical lines for mean
    ax.axvline(mean_phev, color='#CE2D4F', linestyle='-', label='Mean')

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax.xaxis.label.set_color('#A5C4D4')
    ax.yaxis.label.set_color('#A5C4D4')
    ax.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax.spines['left'].set_color('#A5C4D4')
    ax.spines['bottom'].set_color('#A5C4D4')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax.tick_params(axis='x', colors='#A5C4D4')
    ax.tick_params(axis='y', colors='#A5C4D4')

    # Set the padding for the title to add more space
    ax.set_title('Average PHEV Price v. # PHEV bought per zipcode', pad=20)

    # Set the padding for the x-axis label to add more space
    ax.set_xlabel('Average Price of PHEV Vehicles', labelpad=10)

    # Set the padding for the y-axis label to add more space
    ax.set_ylabel('Number of PHEV Vehicles', labelpad=10)

    # Show Legend with a white text color
    legend = ax.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')

    # Show Plot
    plt.show()

    # Save Plot
    fig.savefig('PHEV.svg', format='svg', dpi=1200)
    # fig.savefig('PHEV.png', format='png', dpi=1200)



# BEV
# -----------------------

    # Exclude data points where both x and y values are 0 for NUM_BEV and AVG_PRICE_BEV
    avg_prices_bev = avg_prices[(avg_prices['NUM_BEV'] != 0) & (avg_prices['AVG_PRICE_BEV'] != 0)]


    # Filter data for the BEV chart: 5000 < AVG_PRICE_BEV < 110000
    avg_prices_bev = avg_prices[(avg_prices['AVG_PRICE_BEV'] > 1000) & (avg_prices['AVG_PRICE_BEV'] < 110000)]

    # Calculate correlations for NUM_BEV and AVG_PRICE_BEV
    corr_bev, corr_bev_pvalue = pearsonr(avg_prices_bev['NUM_BEV'], avg_prices_bev['AVG_PRICE_BEV'])
    corr_bev = round(corr_bev, 4) 
    print("\nThe Pearson Correlation Coefficient for number of BEV and Average Price by Zipcode:", corr_bev)
    print("The corresponding P-value:", corr_bev_pvalue)

    # Calculate mean for AVG_PRICE_PHEV
    mean_bev = avg_prices_bev['AVG_PRICE_BEV'].mean()

     # BEV　STYLING:
    # ---------

    # Create a figure and axis with a specific background color (navy blue)
    fig, ax = plt.subplots()
    ax.set_facecolor('#16253B')  # Set the background color of the axis
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart

    # Create the scatter plot on the axis for NUM_BEV and AVG_PRICE_BEV with smaller dots
    ax.scatter(avg_prices_bev['AVG_PRICE_BEV'], avg_prices_bev['NUM_BEV'], s=10, color='#99F7AB') # s=10 ; dot-size , color ; dot-color

    # Add vertical lines for mean
    ax.axvline(mean_bev, color='#CE2D4F', linestyle='-', label='Mean')

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax.xaxis.label.set_color('#A5C4D4')
    ax.yaxis.label.set_color('#A5C4D4')
    ax.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax.spines['left'].set_color('#A5C4D4')
    ax.spines['bottom'].set_color('#A5C4D4')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax.tick_params(axis='x', colors='#A5C4D4')
    ax.tick_params(axis='y', colors='#A5C4D4')

    # Set the padding for the title
    ax.set_title('Average BEV Price v. # BEV bought per zipcode', pad=20)

    # Set the padding for the x-axis label
    ax.set_xlabel('Average Price of BEV Vehicles', labelpad=10)

    # Set the padding for the y-axis label
    ax.set_ylabel('Number of BEV Vehicles', labelpad=10)

    # Show Legend with a white text color
    legend = ax.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')

    # Show Plot
    plt.show()

    # Save Plot
    fig.savefig('BEV.svg', format='svg', dpi=1200)
    # fig.savefig('BEV.png', format='png', dpi=1200)

# Total
# -----------------------

    # Exclude data points where both x and y values are 0 for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    avg_prices_total = avg_prices[(avg_prices['NUM_TOTAL_EV'] != 0) & (avg_prices['AVG_PRICE_TOTAL_EV'] != 0)]

    # # Filter data for prices in the Total EV chart: x < 110000
    avg_prices_total = avg_prices[(avg_prices['AVG_PRICE_TOTAL_EV'] > 1000) & (avg_prices['AVG_PRICE_TOTAL_EV'] < 110000)]

    # Calculate correlations for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV
    corr_total, corr_total_pvalue = pearsonr(avg_prices_total['NUM_TOTAL_EV'], avg_prices_total['AVG_PRICE_TOTAL_EV'])
    corr_total = round(corr_total, 4) 
    print("\nThe Pearson Correlation Coefficient for total vehicles and Average Price by Zipcode:", corr_total)
    print("The corresponding P-value:", corr_total_pvalue)

    # Calculate mean for AVG_PRICE_PHEV
    mean_total_ev = avg_prices_phev['AVG_PRICE_TOTAL_EV'].mean()

    # TOTAL STYLING:
    # ---------

    # Create a figure and axis with a specific background color (navy blue)
    fig, ax = plt.subplots()
    ax.set_facecolor('#16253B')  # Set the background color of the axis
    fig.set_facecolor('#16253B')  # Set the background color of the entire chart

    # Create the scatter plot on the axis for NUM_TOTAL_EV and AVG_PRICE_TOTAL_EV with smaller dots
    ax.scatter(avg_prices_total['AVG_PRICE_TOTAL_EV'], avg_prices_total['NUM_TOTAL_EV'], s=10, color='#99F7AB') # s=10 ; dot-size , color ; dot-color

    # Add vertical lines for mean
    ax.axvline(mean_total_ev, color='#CE2D4F', linestyle='-', label='Mean')

    # Set the color of the x-axis label, y-axis label, and title to #A5C4D4
    ax.xaxis.label.set_color('#A5C4D4')
    ax.yaxis.label.set_color('#A5C4D4')
    ax.title.set_color('#A5C4D4')

    # Set the color of the entire axis, including ticks and spines
    ax.spines['left'].set_color('#A5C4D4')
    ax.spines['bottom'].set_color('#A5C4D4')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set the color of ticks (axis numbers) to #A5C4D4
    ax.tick_params(axis='x', colors='#A5C4D4')
    ax.tick_params(axis='y', colors='#A5C4D4')

    # Set the padding for the title to add more space
    ax.set_title('Average Price of vehicles v. # bought per zipcode', pad=20)

    # Set the padding for the x-axis label to add more space
    ax.set_xlabel('Average Price of TOTAL EV Vehicles', labelpad=10)

    # Set the padding for the y-axis label to add more space
    ax.set_ylabel('Number of TOTAL EV Vehicles', labelpad=10)

    # Show Legend with a white text color
    legend = ax.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color('#A5C4D4')

    # Show Plot
    plt.show()

    # Save Plot
    fig.savefig('Total.svg', format='svg', dpi=1200)
    # fig.savefig('Total.png', format='png', dpi=1200)


if __name__ == '__main__':
    main()
