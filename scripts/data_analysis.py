import pandas as pd

#load the data from the CSV files
ebay_data = pd.read_csv('data/raw_data/<your_search_term>_ebay_details.csv')
amazon_data = pd.read_csv(f'data/raw_data/{search_term}_amazon_details.csv')
google_shopping_data = pd.read_csv(f'data/raw_data/{search_term}_google_shopping_details.csv')

#extract the search term from the metadata (assuming its in the first row)
search_term = ebay_data.iloc[0]['Search Term']

#concatenating all data to a single dataframe
all_data = pd.concat([ebay_data, amazon_data, google_shopping_data], ignore_index=True)

#data cleaning: convert 'price' column to numeric, get rid of non-numeric symbols, convert to float
all_data['Price'] = all_data['Price'].replace('[\$,]', '', regex=True).astype(float)

#calculate average price for each brand 
average_price_per_brand = all_data.groupby('Brand')['Price'].mean()

#calculate average price for each listing 
average_price_per_listing = all_data.groupby('Listing Name')['Price'].mean()


#display results
print(f"Analysis for search term: {search_term}")
print("Average Price for each brand:")
print(average_price_per_brand)

print("\nAverage Price for Each Listing:")
print(average_price_per_listing)