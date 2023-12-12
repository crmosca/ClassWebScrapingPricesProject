# visualizations/visualizing_data.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# first load the data from the CSV files
ebay_data = pd.read_csv('../data/raw_data/<your_search_term>_ebay_details.csv')
amazon_data = pd.read_csv('../data/raw_data/<your_search_term>_amazon_details.csv')
google_shopping_data = pd.read_csv('../data/raw_data/<your_search_term>_google_shopping_details.csv')

# then concatenate the data from different sources into a single DataFrame
all_data = pd.concat([ebay_data, amazon_data, google_shopping_data], ignore_index=True)

# convert 'price' column to numeric
all_data['Price'] = all_data['Price'].replace('[\$,]', '', regex=True).astype(float)

# Create a boxplot for overall data
plt.figure(figsize=(10, 6))
sns.boxplot(x='Source', y='Price', data=all_data)
plt.title('Boxplot of Prices for Overall Data')
plt.show()

# Create separate boxplots for each website
plt.figure(figsize=(15, 8))
sns.boxplot(x='Brand', y='Price', hue='Source', data=all_data)
plt.title('Boxplot of Prices for Each Brand and Source')
plt.show()
