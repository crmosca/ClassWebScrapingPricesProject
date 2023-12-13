# visualizations/visualizing_data.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
ebay_data = pd.read_csv('../data/raw_data/<your_search_term>_ebay_prices_and_names.csv')

# Convert 'Prices' column to numeric
ebay_data['Prices'] = ebay_data['Prices'].replace('[\$,]', '', regex=True).astype(float)

# Creating a boxplot for eBay data
plt.figure(figsize=(10, 6))
sns.boxplot(x='Source', y='Prices', data=ebay_data)
plt.title('Boxplot of Prices for eBay Data')
plt.show()

# Creating a boxplot for each listing
plt.figure(figsize=(15, 8))
sns.boxplot(x='Listing Names', y='Prices', data=ebay_data)
plt.title('Boxplot of Prices for Each Listing on eBay')
plt.xticks(rotation=90)
plt.show()
