from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def main():
    url = "https://www.nhsinform.scot/illnesses-and-conditions/a-to-z"
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    
    chunks = parsed_code.find_all('li')
    
    # find all links
    links = []
    a = parsed_code.find_all('a', href=True)
    for link in a:
        starter = link['href']
        
        if starter[0] == '/':
            link = 'https://www.nhsinform.scot' + starter
            links.append(link)
    
    # 14:335
    links = links[14:336]
    print(links)


    
    names = []
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
         
    disease_dict = {'Disease': names, 'ID': index, 'Links': links}
    # add link to this
           
    names_df = pd.DataFrame(disease_dict) 
        
    names_df.to_csv('NHS_Disease_Data.csv')
    print(names_df)
  

# add link to dictionary

# last thing is index 377

#     all_diseases = chunks[
        
#     names = chunks.find_all("a href")

    
main()