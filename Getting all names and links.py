from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.nhsinform.scot/illnesses-and-conditions/a-to-z"
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    
    chunks = parsed_code.find_all('li')
    
    # find_all "a href"
    
    names = []
    counter = 0
    for index in range(378):
        item = chunks[index]
        item = item.text
        item = item.split("\t\t\t\t")
        print(item)
        names.append(item)
            

# last thing is index 377

#     all_diseases = chunks[
        
#     names = chunks.find_all("a href")

    
main()