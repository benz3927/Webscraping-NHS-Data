from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt

# def country_counter(url):
url = 'https://www.nhsinform.scot/illnesses-and-conditions/diabetes/type-1-diabetes/'
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

# main()