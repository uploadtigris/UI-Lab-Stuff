import pandas as pd
import matplotlib.pyplot as plt

#read in from CSV
df = pd.read_csv("E:\Jun EV Task\Correlation_Analysis\CSVs\prices_by_total.csv")

#remove NAN values
df = df.dropna()

#total correlation for all data
correlation = df['PRICE'].corr(df['ttl_bought'])
print(f'The total correlation of price to total bought is: {correlation}')

###################
# Without Filter
###################

# #correlation for data
# correlation= df['price'].corr(df['total_bought'])
# print(f'The total correlation of price to total bought (non-adjusted) is: {correlation}')

# plt.figure(figsize=(10, 6))
# plt.scatter(df['price'], df['total_bought'], c='skyblue', alpha=0.6)
# plt.title('Scatter Plot: Price vs. Total Bought (non-adjusted)')
# plt.xlabel('Price')
# plt.ylabel('Total Bought')
# plt.grid(True)
# plt.show()


###################
# With Price Filter
###################

# #filter for prices less than 150000
# df_filtered_price = df[df['price'] <= 150000]

# #correlation for price filtered data
# correlation_priceadj = df_filtered_price['price'].corr(df_filtered_price['total_bought'])
# print(f'The total correlation of price to total bought (adjust for price < $150000) is: {correlation_priceadj}')

# #plot chart for vehicles under $150,000
# plt.figure(figsize=(10, 6))
# plt.scatter(df_filtered_price['price'], df_filtered_price['total_bought'], c='skyblue', alpha=0.6)
# plt.title('Scatter Plot: Price vs. Total Bought (Outliers >$150000 Removed)')
# plt.xlabel('Price')
# plt.ylabel('Total Bought')
# plt.grid(True)
# plt.show()

#####################################
# With Price and Total Bought Filter
#####################################

# #filter for total_bought under 6000 (non-tesla)
# df_filtered_price_totalbought = df[(df['total_bought'] <= 6000) & (df['price'] <= 150000)]

# correlation_price_totalbought_adj = df_filtered_price_totalbought['price'].corr(df_filtered_price_totalbought['total_bought'])

# print(f'The total correlation of price to total bought (adjust for price) is: {correlation_price_totalbought_adj}')

# #plot chart for vehicles under $150,000
# plt.figure(figsize=(10, 6))
# plt.scatter(df_filtered_price_totalbought['price'], df_filtered_price_totalbought['total_bought'], c='skyblue', alpha=0.6)
# plt.title('Scatter Plot: Price vs. Total Bought (Outliers; >6000 Bought & >$150000 Price Removed)')
# plt.xlabel('Price')
# plt.ylabel('Total Bought')
# plt.grid(True)
# plt.show()

##########################################################################
# With Price (<$150000) and Total Bought Filter (1000 <= X <= 150000)
##########################################################################

#filter for total_bought under 6000 (non-tesla)
df_filtered_price_totalbought = df[(500 <= df['total_bought']) & (df['total_bought'] <= 6000) & (df['price'] <= 150000)]

correlation_price_totalbought_adj = df_filtered_price_totalbought['price'].corr(df_filtered_price_totalbought['total_bought'])

print(f'The total correlation of price to total bought (adjust for price) is: {correlation_price_totalbought_adj}')

#plot chart for vehicles under $150,000
plt.figure(figsize=(10, 6))
plt.scatter(df_filtered_price_totalbought['price'], df_filtered_price_totalbought['total_bought'], c='skyblue', alpha=0.6)
plt.title('Scatter Plot: Price vs. Total Bought (Outliers; 500<X<6000 Bought & >$150000 Price Removed)')
plt.xlabel('Price')
plt.ylabel('Total Bought')
plt.grid(True)
plt.show()





