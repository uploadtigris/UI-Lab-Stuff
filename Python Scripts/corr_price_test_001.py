import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import csv

def total_PHEV(zip_ttlbought_long_df, model_price_long_df):
    ttl_PHEV = {}

    # Filter model_price_long_df for PHEV and value == 1.0
    phev_rows = model_price_long_df[(model_price_long_df['Vehicle_Type'] == 'PHEV') &
                                    (model_price_long_df['value'] == 1.0)]

    # Create a dictionary to map MODEL to sum of 'count' for PHEV
    model_to_sum = phev_rows.groupby('MODEL')['value'].sum().to_dict()

    for zipcode, group in zip_ttlbought_long_df.groupby('Zip Code'):
        # Print the current zip code on its own line
        print(f"Zip Code: {zipcode}\n")

        # Filter 'group' DataFrame to only include relevant MODEL values
        relevant_models = group['variable'].unique()
        
        # Calculate the sum of 'count' for each relevant MODEL
        counts = [model_to_sum.get(model, 0.0) for model in relevant_models]
        
        # Store the counts list in the dictionary with the zip code as the key
        ttl_PHEV[zipcode] = counts

    return ttl_PHEV


def main():
  #read-in the CSV's
  model_price_wide_df = pd.read_csv('E:\Jun EV Task\Correlation_Analysis\CSVs\MODEL_PRICE_WATERFALL.csv')
  zip_totalbought_wide_df = pd.read_csv('E:\Jun EV Task\Correlation_Analysis\CSVs\ZIP_TTLBOUGHT.csv')

  #Convert MODEL_PRICE_WATERFALL to a long-format CSV
  model_price_long_df = model_price_wide_df.melt(id_vars=['MODEL', 'MAKE', 'PRICE'], 
                                                 value_vars=['HEV', 'PHEV', 'BEV'],  
                                                 # Name of new column that holds all value from columns specified in value_vars
                                                 var_name='Vehicle_Type', 
                                                #binary value denoting whether it is the type of vehicle listed in value_vars
                                                 value_name='value')
  
  # Replace NaN values in 'Vehicle_Type' column with 0
  model_price_long_df['value'].fillna(0, inplace=True)
  # Drop rows with no Price
  filtered_model_price_long_df = model_price_long_df[model_price_long_df['PRICE'] != 0]
  print(filtered_model_price_long_df)

  ### removing "Grand Total" items from zip_ttlbought
  zip_totalbought_wide_df = zip_totalbought_wide_df.iloc[:, :-1]
  # Calculate the index of the last row
  last_row_index = zip_totalbought_wide_df.shape[0] - 1
  # Remove the last row using .drop()
  zip_totalbought_wide_df = zip_totalbought_wide_df.drop(last_row_index)
  print('wide', zip_totalbought_wide_df)

  #Convert ZIP_TTLBOUGHT to a long-format CSV
  zip_ttlbought_long_df = zip_totalbought_wide_df.melt(id_vars=['Zip Code'],
                                                        value_name='value')
  zip_ttlbought_long_df['value'].fillna(0, inplace=True)
  print(zip_ttlbought_long_df)

  ################
  # Calculating Row Entries
  ################
  #find the total PHEV per zipcode
  result = total_PHEV(zip_ttlbought_long_df, model_price_long_df)
  print('ayooooo', result)


if __name__ == "__main__":
    main()