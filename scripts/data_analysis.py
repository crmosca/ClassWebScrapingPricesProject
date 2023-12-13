import pandas as pd

#loading the data from the CSV file
ebay_data = pd.read_csv('data/raw_data/<your_search_term>_ebay_prices_and_names.csv')

#extracting the search term from the metadata (assuming it's in the first row)
search_term = ebay_data.iloc[0]['Search Term']

#data cleaning: convert 'Prices' column to numeric, get rid of non-numeric symbols, convert to float
ebay_data['Prices'] = ebay_data['Prices'].replace('[\$,]', '', regex=True).astype(float)

#calculating average price for each listing on eBay
average_price_per_listing_ebay = ebay_data.groupby('Listing Names')['Prices'].mean()

#display results
print(f"Analysis for search term: {search_term}")

print("\nAnalysis for eBay:")
print("\nAverage Price for Each Listing (eBay):")
print(average_price_per_listing_ebay)
