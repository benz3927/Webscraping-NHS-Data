import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib as plt

def get_symptoms(symptom_url):
    
    # if there is symptoms header, ul directly under
    
    source_code = requests.get(symptom_url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    divs = parsed_code.find_all('div',class_="editor")
    
    
    # Generic method for all symptom bullet points
    if len(divs) > 1:
        for div in divs:
            h2 = div.find('h2')
            if 'symptoms' in h2.text:
                symptoms_chunk = div
        
        symptoms_chunk = symptoms_chunk.find_all('ul')
#                 print(symptoms_chunk)
        all_symptoms = []

        for symptoms in symptoms_chunk:
            for symptom in symptoms:
                symptom= symptom.text
                symptom = re.sub(r'[\r\t\n ]+', ' ',symptom).strip()
                all_symptoms.append(symptom)
        
        symptoms_list = []
        for item in all_symptoms:
            if item != '':
                symptoms_list.append(item)
            
        return symptoms_list
    
    else:
        return 'null'

def main():
    print(get_symptoms('https://www.nhsinform.scot/illnesses-and-conditions/stomach-liver-and-gastrointestinal-tract/acute-pancreatitis/'))
    


main()