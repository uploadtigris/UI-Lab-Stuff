
# Name : Tigris Mendez
# Organization: UT Austin Urban Information lab
# Affiliation: Undergraduate Research Assistant
# Data Created: 10/7/2023
# Description : My goal is to leverage two CSV files to understand the correlation
#               of Types of Hybrid or Electrical Vehicles and their price. 
# Input:
#   ~ CSV titled "MODEL_PRICE_AVERAGED"
#   ~ CSV titled ""
#
# Ouput:
#   ~ 3 correlation figures:
#       1) Number of PHEV Vehicles vs. Avg Price of PHEV
#       2) Number of BEV Vehicles vs. Avg Price of BEV
#       2) Number of Total Vehicles vs. Avg Price of Total EV Vehicles

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import csv
import time

def ttl_avg_price(zip_ttlbought_long_df, model_price_long_df):
    # Merge 'zip_ttlbought_long_df' with 'model_price_long_df' on 'MODEL'
    merged_df = pd.merge(zip_ttlbought_long_df, model_price_long_df, left_on='variable', right_on='MODEL')

    print(zip_ttlbought_long_df)
    print(model_price_long_df)


    # Calculate the total price for each zip code and the average price
    result_df = pd.DataFrame(columns=['Zip Code', 'AVG_PRICE'])
    for zipcode in merged_df['Zip Code'].unique():
        zip_filtered_df = merged_df[merged_df['Zip Code'] == zipcode]
        total_price = (zip_filtered_df['PRICE'] * zip_filtered_df['value_x']).sum()
        total_count = zip_filtered_df['value_x'].sum()

        if total_count > 0:
            avg_price = total_price / total_count
        else:
            avg_price = 0

        result_df = pd.concat([result_df, pd.DataFrame({'Zip Code': [zipcode], 'AVG_PRICE': [avg_price]})],
                              ignore_index=True)

    # Set the data types for the columns
    result_df['AVG_PRICE'] = result_df['AVG_PRICE'].astype(float)

    # create a new data frame with the PRICE replaced with the average per Make

    print(result_df)

    return result_df

def avg_price_by_type(zip_ttlbought_long_df, model_price_long_df, zip_count_result_df, vehicle_type):
    # Filter 'model_price_long_df' for the current vehicle type
    vehicle_rows = model_price_long_df[(model_price_long_df['Vehicle_Type'] == vehicle_type) &
                                       (model_price_long_df['value'] == 1.0)]

    # Merge 'zip_ttlbought_long_df' with 'zip_count_result_df' on 'Zip Code'
    merged_df = pd.merge(zip_ttlbought_long_df, zip_count_result_df, on='Zip Code')

    # Now, merged_df will have the "MAKE" column matched with the "MODEL" based on a common key.

    print('merged_1', merged_df)

    # Merge the resulting DataFrame with the filtered 'model_price_long_df' on 'MODEL'
    merged_df = pd.merge(merged_df, vehicle_rows, left_on='variable', right_on='MODEL')

    print('merged_2', merged_df)


    # Calculate the total price for each zip code and the average price
    result_df = pd.DataFrame(columns=['Zip Code', 'AVG_PRICE'])
    for zipcode in merged_df['Zip Code'].unique():
        zip_filtered_df = merged_df[merged_df['Zip Code'] == zipcode]
        total_price = (zip_filtered_df['PRICE'] * zip_filtered_df['value_x']).sum()
        total_count = zip_filtered_df['value_x'].sum()

        if total_count > 0:
            avg_price = total_price / total_count
        else:
            avg_price = 0

        result_df = pd.concat([result_df, pd.DataFrame({'Zip Code': [zipcode], 'AVG_PRICE': [avg_price]})],
                              ignore_index=True)

    # Set the data types for the columns
    result_df['AVG_PRICE'] = result_df['AVG_PRICE'].astype(float)

    return result_df

def total_Vehicles(zip_ttlbought_long_df, model_price_long_df, vehicle_type):
    # Filter model_price_long_df for the given vehicle_type and value == 1.0
    vehicle_rows = model_price_long_df[(model_price_long_df['Vehicle_Type'] == vehicle_type) &
                                       (model_price_long_df['value'] == 1.0)]

    # Extract the unique models for the given vehicle_type
    vehicle_models = vehicle_rows['MODEL'].unique()

    # Create a list to store DataFrames for each zipcode
    result_dfs = []

    for zipcode, group in zip_ttlbought_long_df.groupby('Zip Code'):
        # Filter 'group' DataFrame to only include relevant MODEL values
        relevant_models = group['variable'].unique()
        
        # Find the intersection of relevant_models and vehicle_models
        common_models = set(relevant_models).intersection(vehicle_models)
        
        # Calculate the sum of 'count' for common models
        total_count = sum(group[group['variable'].isin(common_models)]['value'])
        
        # Create a DataFrame for the current zipcode and total count
        zipcode_df = pd.DataFrame({'Zip Code': [zipcode], f'Number {vehicle_type}': [total_count]})
        
        # Append the data to the list of DataFrames
        result_dfs.append(zipcode_df)

    # Concatenate all DataFrames in the list into a single result DataFrame
    result_df = pd.concat(result_dfs, ignore_index=True)

    return result_df

def main():
    #begin stage 1 ~ "Set up"
    start_time = time.time()  # Record the start time

    # Read the CSVs
    
    model_price_wide_df = pd.read_csv('/Volumes/ESD-USB/Jun EV Task/Correlation_Analysis/CSVs/MODEL_PRICE_WATERFALL.csv')
    zip_totalbought_wide_df = pd.read_csv('/Volumes/ESD-USB/Jun EV Task/Correlation_Analysis/CSVs/ZIP_TTLBOUGHT.csv')

    # Convert MODEL_PRICE_WATERFALL to a long-format CSV
    model_price_long_df = model_price_wide_df.melt(id_vars=['MODEL', 'MAKE', 'PRICE'],
                                                   value_vars=['HEV', 'PHEV', 'BEV'],
                                                   var_name='Vehicle_Type',
                                                   value_name='value')

    # Replace NaN values in 'Vehicle_Type' column with 0
    model_price_long_df['value'].fillna(0, inplace=True)

    # Drop rows with no Price
    filtered_model_price_long_df = model_price_long_df[model_price_long_df['PRICE'] != 0]

    # Remove "Grand Total" items from zip_totalbought
    zip_totalbought_wide_df = zip_totalbought_wide_df.iloc[:, :-1]

    # Convert ZIP_TTLBOUGHT to a long-format CSV
    zip_ttlbought_long_df = zip_totalbought_wide_df.melt(id_vars=['Zip Code'],
                                                         value_name='value')
    zip_ttlbought_long_df['value'].fillna(0, inplace=True)

    # print('sanity check', zip_ttlbought_long_df)

    # Calculate the number of PHEV, BEV, and HEV vehicles for each zip code
    phev_result_df = total_Vehicles(zip_ttlbought_long_df, filtered_model_price_long_df, 'PHEV')
    bev_result_df = total_Vehicles(zip_ttlbought_long_df, filtered_model_price_long_df, 'BEV')
    hev_result_df = total_Vehicles(zip_ttlbought_long_df, filtered_model_price_long_df, 'HEV')

    # Merge the result DataFrames on 'Zip Code'
    merged_result_df = pd.merge(phev_result_df, bev_result_df, on='Zip Code', how='outer')
    merged_result_df = pd.merge(merged_result_df, hev_result_df, on='Zip Code', how='outer')
    merged_result_df['NUM TOTAL EV'] = merged_result_df['Number PHEV'] + merged_result_df['Number BEV'] + merged_result_df['Number HEV']

    # Fill NaN values with 0
    merged_result_df.fillna(0, inplace=True)

    # Save the updated zip_totalbought_wide_df to a CSV file
    zip_totalbought_wide_df.to_csv('CSVs\\avg_price_by_type_make_only.csv', index=False)

    #stage 1 complete 
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print("Stage 1 : Setting up *Completed*")

    print("Execution time:", execution_time, "seconds")

    #begin stage 2 ~ "Compute Averages"
    start_time = time.time()  # Record the start time

    #Calculate the averages
    phev_price_avg = avg_price_by_type(zip_ttlbought_long_df, filtered_model_price_long_df, phev_result_df, 'PHEV')
    bev_price_avg = avg_price_by_type(zip_ttlbought_long_df, filtered_model_price_long_df, bev_result_df, 'BEV')
    hev_price_avg = avg_price_by_type(zip_ttlbought_long_df, filtered_model_price_long_df, hev_result_df, 'HEV')
    ttl_price_avg = ttl_avg_price(zip_ttlbought_long_df, filtered_model_price_long_df)

    #stage 2 completed
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print("Stage 2 : Computing Averages *Completed*")
    print("Execution time:", execution_time, "seconds")

    # Create the final CSV with the appropriate column names
    field = ['ZIPCODE', 'NUM_PHEV', 'NUM_BEV', 'NUM_HEV', 'NUM_TOTAL_EV',
             'AVG_PRICE_PHEV', 'AVG_PRICE_BEV', 'AVG_PRICE_HEV', 'AVG_PRICE_TOTAL_EV']
    file_path = 'CSVs\\avg_price_by_type_make_only.csv'

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(field)

        # Loop through each row in merged_result_df and append the data to the CSV
        for index, row in merged_result_df.iterrows():
            zipcode = row['Zip Code']
            num_phev = row['Number PHEV']
            num_bev = row['Number BEV']
            num_hev = row['Number HEV']
            num_total_ev = row['NUM TOTAL EV']
            avg_price_phev = phev_price_avg[hev_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]
            avg_price_bev = bev_price_avg[hev_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]
            avg_price_hev = hev_price_avg[hev_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]
            avg_price_total_ev = ttl_price_avg[ttl_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]

            # Append the data row to the CSV
            writer.writerow([zipcode, num_phev, num_bev, num_hev, num_total_ev,
                            avg_price_phev, avg_price_bev, avg_price_hev, avg_price_total_ev])



if __name__ == '__main__':
    main()

