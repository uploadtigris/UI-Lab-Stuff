# Name: Tigris Mendez
# Organization: UT Austin Urban Information lab
# Affiliation: Undergraduate Research Assistant
# Data Created: 10/1/2023
# Last Date Editted: 
# Program Goal:
# - To find the correlation between prices of Vehicles registered in the Texas region
# - and whether they are BEV, PHEV, or HEV. 
# - Hypothesis: BEV vehicles are more expensive than PHEV and PHEV is > HEV

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


wide_df = pd.read_csv('E:\Jun EV Task\Correlation_Analysis\CSVs\price_type_vanilla.csv')

#Melt HEV, PHEV, and BEV into a single column
long_df = wide_df.melt(id_vars=['MODEL', 'MAKE', 'PRICE'], 
                    value_vars=['HEV', 'PHEV', 'BEV'],  
                    # Name of new column that holds all value from columns specified in value_vars
                    var_name='Vehicle_Type', 
                    #binary value denoting whether it is the type of vehicle listed in value_vars
                    value_name='value')

# Replace NaN values in 'Vehicle_Type' column with 0
long_df['value'].fillna(0, inplace=True)

# Drop rows with no Price
filtered_df = long_df[long_df['PRICE'] != 0]


# print(filtered_df['ttl_bought'])

print(filtered_df)

#####################
# Counting Types
#####################
#Sanity check that num of vehicle type is consistent with Excel sheet
vehicle_type_counts = filtered_df['Vehicle_Type'].value_counts()

# Count the occurrences of 'HEV' when its value is equal to 1
hev_count = filtered_df[filtered_df['Vehicle_Type'] == 'HEV']['value'].eq(1).sum()
phev_count = filtered_df[filtered_df['Vehicle_Type'] == 'PHEV']['value'].eq(1).sum()
bev_count = filtered_df[filtered_df['Vehicle_Type'] == 'BEV']['value'].eq(1).sum()

# Print the count
print(f'Total HEV with value 1: {hev_count}')
print(f'Total PHEV with value 1: {phev_count}')
print(f'Total BEV with value 1: {bev_count}')

# Initialize a counter
ev_count = 0
phev_count = 0
bev_count = 0

# Iterate through each row in the DataFrame
for index, row in filtered_df.iterrows():
    # Check if the Vehicle_Type is 'HEV' and the value is 1
    if row['Vehicle_Type'] == 'HEV' and row['value'] == 1:
        # If the condition is met, increment the counter by 1
        ev_count += 1
    if row['Vehicle_Type'] == 'PHEV' and row['value'] == 1:
        phev_count += 1
    if row['Vehicle_Type'] == 'BEV' and row['value'] == 1:
        bev_count += 1

print(hev_count, phev_count, bev_count)


# Correlation without any filters!
# (other than removing rows with price == $0)
###############################################################################
# Finding the correlation and the P-Value for BEV

# Filter the DataFrame for BEV vehicles
bev_df = filtered_df[filtered_df['Vehicle_Type'] == 'BEV']

x1 = bev_df['PRICE']
x2 = bev_df['value']

# Replace np.inf and -np.inf with zeros
x1 = x1.replace([np.inf, -np.inf], 0)
x2 = x2.replace([np.inf, -np.inf], 0)


# Create a copy of the DataFrame to avoid the SettingWithCopyWarning
filtered_df_copy = filtered_df.copy()

# Filter the DataFrame for BEV vehicles
bev_df = filtered_df[filtered_df['Vehicle_Type'] == 'BEV']

correlation = x1.corr(x2)

bev_corr, p_value = pearsonr(x1, x2)

print("\nPearson Correlation Coefficient for is BEV to price:", bev_corr)
print("P-value for BEV to price:", p_value)

# # ###############################################################################
# Finding the correlation and the P-Value for PHEV to price
phev_df = filtered_df[filtered_df['Vehicle_Type'] == 'PHEV']

x1 = phev_df['PRICE']
x2 = phev_df['value']

correlation = x1.corr(x2)

phev_corr, p_value = pearsonr(x1, x2)

print("\nPearson Correlation Coefficient for is PHEV to price:", phev_corr)
print("P-value for PHEV to price:", p_value)

###############################################################################
# Finding the correlation and the P-Value for HEV to price
# Finding the correlation and the P-Value for PHEV to price
hev_df = filtered_df[filtered_df['Vehicle_Type'] == 'HEV']

x1 = hev_df['PRICE']
x2 = hev_df['value']

correlation = x1.corr(x2)

hev_corr, p_value = pearsonr(x1, x2)

print("\nPearson Correlation Coefficient HEV to price:", hev_corr)
print("P-value for HEV to price:", p_value)
print('')
# ##################################################################################
# ##################################################################################


