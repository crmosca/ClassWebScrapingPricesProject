# Web Scraping Prices Project 

##Overview 
This project is an attempt to practice the skills gained in my python course as well as to use some basic data cleaning and visualization using python in Visual Studio. 

## Project Structure
**scripts:** Contains Python scripts for web scraping and data analysis.
**data:** Stores raw and processed data.
**visualizations:** Holds scripts for data visualizations.

##Getting started
1. Install required libraries:
'''bash
pip install pandas numpy beautifulsoup4 requests seaborn matplotlib httpx asyncio 

##Running the program
1. Run the web scraping script:
python scripts/web_scraper.py

2. Analyze the data:
python scripts/data_analysis.py

3. Run visualization: 
python visualizations/visualizing_data.py

###Story of the programs and git commits
This is a project for my python class. I started very ambitiously by trying to scrape pricing data from Amazon, Google Shopping, and Ebay, but really struggled with the webscraper. After hours of trying to get it to work but to no avail, running into issues with the html classes as well as from Amazon blocking, I explored API options but also struggled to get these set up in a timely manner. I returned to the idea of webscraping by reverting to an old commit, and then decided to keep things simple and focus on ebay. While I would like to have been able to clean up the data more and to group based on brands and whether they are auctions or buy it now listings for example, these are all things that I can incorporate in the future. I am just happy that I was able to get it up and running and doing what I wanted it to do for the most part! 

####Important information 
When you run scripts/web_scraper.py it prompts you to enter the name of a product and then it searches for that product and pulls data from the search page results. It pulls the names of the product listings as well as the prices. 
When you run scripts/data_analysis.py it prompts you to enter the same product name, make sure it is the same as the product you entered into the web scraper and spelled the same way. It then cleans up that data so that the visualizer piece can do statistics and make charts with it.
Finally, when you run the visualizations/visualizing_data.py it also prompts you for the product again. Again, make sure that it is spelled the same. 

Best wishes all! Although not perfect, I'm glad to have gained some experience by trying this project.  
