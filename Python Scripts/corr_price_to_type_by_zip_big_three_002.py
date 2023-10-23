
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
import csv

def ttl_avg_price(new_merged_df):

    # Calculate the total price for each zip code and the average price
    result_df = pd.DataFrame(columns=['Zip Code', 'AVG_PRICE'])

    for zipcode in new_merged_df['Zip Code'].unique():
        zip_filtered_df = new_merged_df[new_merged_df['Zip Code'] == zipcode]
        total_price = (zip_filtered_df['PRICE'] * zip_filtered_df['value_x']).sum()
        total_count = zip_filtered_df['value_x'].sum()

        if total_count > 0:
            avg_price = total_price / total_count
            # print(total_count, avg_price)
        else:
            avg_price = 0
            # print(total_count, 0)

        result_df = pd.concat([result_df, pd.DataFrame({'Zip Code': [zipcode], 'AVG_PRICE': [avg_price]})],
                              ignore_index=True)
        
        # print(result_df)
    # Set the data types for the columns
    result_df['AVG_PRICE'] = result_df['AVG_PRICE'].astype(float)

    return result_df

def avg_price_by_type(new_merged_df, zip_count_result_df, vehicle_type):
    # Filter 'model_price_long_df' for the current vehicle type
    vehicle_rows = new_merged_df[(new_merged_df['Vehicle_Type'] == vehicle_type) &
                                       (new_merged_df['value_y'] == 1.0)]
    
    print('vehicle rows', vehicle_rows)
    
     # Calculate the total price for each zip code and the average price
    result_df = pd.DataFrame(columns=['Zip Code', 'AVG_PRICE'])
    for zipcode in vehicle_rows['Zip Code'].unique():
        zip_filtered_df = vehicle_rows[vehicle_rows['Zip Code'] == zipcode]
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

#Input：A long-format data frame with columns Zipcode, variable, value_x (number of vehicle), Model, Make, Price, Type
#       The vehicle type to search for (PHEV, BEV, HEV)
# Output: A dataframe of only the vehicles you are searching for (filtered by Vehicle Type)
def total_Vehicles(dataframe, vehicle_type):
    result_df = pd.DataFrame(columns=['Zip Code', f'Number {vehicle_type}'])
    
    filtered_df = dataframe[(dataframe['Vehicle_Type'] == vehicle_type) & (dataframe['value_y'] == 1.0)]

    # #checking counts
    # total_count = filtered_df['value_x'].sum()
    # print('the total', vehicle_type, 'is', total_count)

    for zip_code in filtered_df['Zip Code'].unique():
        zip_filtered_df = filtered_df[filtered_df['Zip Code'] == zip_code]
        zip_sum = zip_filtered_df['value_x'].sum()

        # Create a new DataFrame for the current ZIP code
        zip_result_df = pd.DataFrame({'Zip Code': [zip_code], f'Number {vehicle_type}': [zip_sum]})

        # Concatenate the zip_result_df to the result_df
        result_df = pd.concat([result_df, zip_result_df], ignore_index=True)

    # double_check_totals = result_df[f'Number {vehicle_type}'].sum()
    # print('the total is still', double_check_totals, 'for vehicles of type', vehicle_type)
    return result_df

def main():
    # Read the CSVs
    model_price_wide_df = pd.read_csv('/Users/tigris/Documents/UI Lab/Jun EV Task/Correlation_Analysis/CSVs/MODEL_PRICE_WATERFALL.csv')
    zip_totalbought_wide_df = pd.read_csv('/Users/tigris/Documents/UI Lab/Jun EV Task/Correlation_Analysis/CSVs/ZIP_TTLBOUGHT.csv')

    # Convert MODEL_PRICE_WATERFALL to a long-format CSV
    model_price_long_df = model_price_wide_df.melt(id_vars=['MODEL', 'MAKE', 'PRICE'],
                                                   value_vars=['HEV', 'PHEV', 'BEV'],
                                                   var_name='Vehicle_Type',
                                                   value_name='value')
    
    # Replace NaN values in 'Vehicle_Type' column with 0
    model_price_long_df['value'].fillna(0, inplace=True)

    # # Drop rows with no Price (ONLY NEEDED WHEN MODEL HAS NO PRICE)
    # filtered_model_price_long_df = model_price_long_df[model_price_long_df['PRICE'] != 0]

    # Remove "Grand Total" items from zip_totalbought (one far right column, one bottom row)
    zip_totalbought_wide_df = zip_totalbought_wide_df.iloc[:-1, :-1]

    # Convert ZIP_TTLBOUGHT to a long-format CSV
    zip_ttlbought_long_df = zip_totalbought_wide_df.melt(id_vars=['Zip Code'],
                                                         value_name='value')
    zip_ttlbought_long_df['value'].fillna(0, inplace=True)

    # add MAKE column to entries in zip_ttlbought_long_df

    # Merge 'zip_ttlbought_long_df' with 'model_price_long_df' on 'MODEL'
    merged_df = pd.merge(zip_ttlbought_long_df, model_price_long_df, left_on='variable', right_on='MODEL')

    #filter for MODEL == Nissan, Tesla, or Chevy
    new_merged_df = merged_df[(merged_df['MAKE'] == 'Nissan') | (merged_df['MAKE'] == 'Chevrolet') | (merged_df['MAKE'] == 'Tesla')]

    # Calculate the number of PHEV, BEV, and HEV vehicles for each zip code
    phev_result_df = total_Vehicles(new_merged_df, 'PHEV')
    bev_result_df = total_Vehicles(new_merged_df, 'BEV')
    hev_result_df = total_Vehicles(new_merged_df, 'HEV')

    # # FIXME: This (below) is aggregating the total EV, not filtering for just NISSAN, Also fix the top3 calculations to match.

    # Merge the result DataFrames on 'Zip Code'
    merged_result_df = pd.merge(phev_result_df, bev_result_df, on='Zip Code', how='outer')
    merged_result_df = pd.merge(merged_result_df, hev_result_df, on='Zip Code', how='outer')
    
    # Fill NaN values with 0
    merged_result_df.fillna(0, inplace=True)

    merged_result_df['NUM TOTAL EV'] = merged_result_df['Number PHEV'] + merged_result_df['Number BEV'] + merged_result_df['Number HEV']
 
    # # FIXME: Do I need this?
    # Save the updated zip_totalbought_wide_df to a CSV file
    # zip_totalbought_wide_df.to_csv('CSVs\\profiles1.csv', index=False)

    # #Calculate the averages
    print('new merged', new_merged_df)
    print('zip result', phev_result_df)

    phev_price_avg = avg_price_by_type(new_merged_df, phev_result_df, 'PHEV')
    bev_price_avg = avg_price_by_type(new_merged_df, bev_result_df, 'BEV')
    hev_price_avg = avg_price_by_type(new_merged_df, hev_result_df, 'HEV')
    ttl_price_avg = ttl_avg_price(new_merged_df)

    # Create the final CSV with the appropriate column names
    field = ['ZIPCODE', 'NUM_PHEV', 'NUM_BEV', 'NUM_HEV', 'NUM_TOTAL_EV',
             'AVG_PRICE_PHEV', 'AVG_PRICE_BEV', 'AVG_PRICE_HEV', 'AVG_PRICE_TOTAL_EV']
    file_path = '/Users/tigris/Documents/UI Lab/Jun EV Task/Correlation_Analysis/CSVs\TotalVehiclesByMake_Nissan_ONLY.csv'

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
            avg_price_phev = phev_price_avg[phev_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]
            avg_price_bev = bev_price_avg[bev_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]

            hev_price_rows = hev_price_avg[hev_price_avg['Zip Code'] == zipcode]
            if not hev_price_rows.empty:
                avg_price_hev = hev_price_rows['AVG_PRICE'].values[0]
            else:
             avg_price_hev = 0
             
            avg_price_total_ev = ttl_price_avg[ttl_price_avg['Zip Code'] == zipcode]['AVG_PRICE'].values[0]

            # Append the data row to the CSV
            writer.writerow([zipcode, num_phev, num_bev, num_hev, num_total_ev,
                            avg_price_phev, avg_price_bev, avg_price_hev, avg_price_total_ev])


if __name__ == '__main__':
    main()

