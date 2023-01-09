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
    
#     if "symptoms" or "Symptoms" not in h2s:
#         return 'Symptom is not a bullet point'
    
    
     # Generic method for all symptom bullet points
     # have to find bullets directly under a paragraph
     
    if len(divs) > 1:
        symptoms_list = []
        
        for div in divs:
            ps = div.find_all('p')
            p_list = []
            for p in ps:
                p_list.append(p.text)
            words = []
            for sentence in p_list:
                sentence = sentence.split(' ')
                for word in sentence:
                    words.append(word)
                
                if 'include:' in words:
                    chunk_div = div
        
                    symptoms_chunk = chunk_div.find_all('ul')
            #                 print(symptoms_chunk)
                    
                    for symptoms in symptoms_chunk:
                        for symptom in symptoms:
                            symptom = symptom.text
                            symptom = re.sub(r'[\r\t\n ]+', ' ',symptom).strip()
                            symptoms_list.append(symptom)
                    
                    updated_symptoms_list = []
                    for item in symptoms_list:
                        if item != '':
                            updated_symptoms_list.append(item)
                    
                    symptoms = updated_symptoms_list
                    return symptoms
    
    else:
        return 'null'

def main():
    print(get_symptoms('https://www.nhsinform.scot/illnesses-and-conditions/heart-and-blood-vessels/conditions/abdominal-aortic-aneurysm/'))
    


main()