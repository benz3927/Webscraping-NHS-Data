from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt

# def country_counter(url):
url = 'https://www.nhsinform.scot/healthy-living/womens-health/later-years-around-50-years-and-over/menopause-and-post-menopause-health/menopause'
source_code = requests.get(url).text
parsed_code = BeautifulSoup(source_code, "html.parser")

everything = parsed_code.find_all('h2')
print(everything)

# chunk = everything[1].find_all("tr")
# countries = []
# 
# for item in chunk:
#     item = item.text
#     item = item.split("\n")
#     
#     print(item)
            
# def main():
# # Scraping 2022 Data
#     year2022 = "https://www.tennisexplorer.com/ranking/atp-men/2022/"
#     year2022_dict = country_counter(year2022)
#     
#     # sorted takes a dictionary and makes it a list of tuples. Sorts the values of the counts within the lists
#     
#     year2022_sorted = sorted(year2022_dict.items(), key=lambda x:x[1], reverse = True)
#     
#     # We take our sorted list of tuples and make it back into a dictionary
#     year2022_dict = dict(year2022_sorted)
#     
#     # extract the scores (country) and keys (counts of top 100 ATP-ranked tennis player) for use in graphing
#     countries2022 = list(year2022_dict.keys())
#     player_counts2022 = np.sort(list(year2022_dict.values()))[::-1]
#     print(year2022_dict)
    
    
# main()