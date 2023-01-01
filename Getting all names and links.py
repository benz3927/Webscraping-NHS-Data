from bs4 import BeautifulSoup
import requests
import pandas as pd  

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
        item = item.split("\n")
        item = item[2]
        item.replace('				','')
        names.append(item)
#         print(item)

#     for name in names:
#         name = name[9:]
#         name = name[:-2]
#         print(name)
    print(names)
    for name in names:
        print(name)

    index = []
    for i in range(len(names)):
        index.append(i)
         
    disease_dict = {'Disease': names, 'ID': index}
    # add link to this
           
    names_df = pd.DataFrame(disease_dict) 
        
    names_df.to_csv('NHS_Disease_Data.csv')
    print(disease_dict)
  

# last thing is index 377

#     all_diseases = chunks[
        
#     names = chunks.find_all("a href")

    
main()