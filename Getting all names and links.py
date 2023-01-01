from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def main():
    url = "https://www.nhsinform.scot/illnesses-and-conditions/a-to-z"
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    
    chunks = parsed_code.find_all('li')
    # for finding links
    # find_all "a href"
    names = []
#     for name in chunks:
#         name = name.find("a")
#         names.append(name)
    
    counter = 0
    for index in range(35,378):
        item = chunks[index]
        item = item.text
        
        item = re.sub(r'[\r\t\n ]+', ' ', item).strip()
        names.append(item)

    for name in names:
        if name == 'Back to top':
            names.remove(name)
    

    index = []
    for i in range(1,len(names)+1):
        index.append(i)
         
    disease_dict = {'Disease': names, 'ID': index}
    # add link to this
           
    names_df = pd.DataFrame(disease_dict) 
        
    names_df.to_csv('NHS_Disease_Data.csv')
    print(disease_dict)
  

# add link to dictionary

# last thing is index 377

#     all_diseases = chunks[
        
#     names = chunks.find_all("a href")

    
main()