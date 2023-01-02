import requests
from bs4 import BeautifulSoup
import re
import matplotlib as plt

def main():
    symptom_url = 'https://www.nhsinform.scot/illnesses-and-conditions/cancer/cancer-types-in-adults/acute-lymphoblastic-leukaemia/#symptoms-of-acute-lymphoblastic-leukaemia'
    source_code = requests.get(symptom_url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")

    everything = parsed_code.find_all('p')

# find the first few li bullet points after the symptom header and stop till the next major heading
    
    for p in everything:
        p = p.text
#         if 'include:' and 'Symptoms' in p:
#             symptom_header = p
            
    print(p)
main()