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
    # Setup the csv
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

    for link in links:
        link = str(link)
    
    names = []
    for index in range(35,378):
        item = chunks[index]
        
        
        item = item.text
        
        item = re.sub(r'[\r\t\n ]+', ' ', item).strip()
        names.append(item)

    for name in names:
        if name == 'Back to top':
            names.remove(name)
    

    indices = []
    for i in range(1,len(names)+1):
        indices.append(i)
         
    disease_dict = {'Disease': names, 'ID': indices, 'Links': links}
    # add link to this
           
    names_df = pd.DataFrame(disease_dict) 
        
    names_df.to_csv('NHS_Disease_names_links.csv')
    
    disease_symptoms = []
#     print(get_symptoms('https://www.nhsinform.scot/illnesses-and-conditions/heart-and-blood-vessels/conditions/abdominal-aortic-aneurysm/'))
    for index in range(len(links)):
        disease_symptoms.append(get_symptoms(links[index]))
    
    all_symptoms = []
    
    index = 0
    all_indices = []
    
    all_names = []
    
    
    for index in range(len(disease_symptoms)):

        if disease_symptoms[index] is None:
            all_names.append(names[index])
            all_indices.append(index+1)
            all_symptoms.append('null')
            
        else:
            num_symptoms = len(disease_symptoms[index])
        
            for i in range(num_symptoms):
                all_indices.append(index+1)
                all_names.append(names[index])
            
            for symptom in disease_symptoms[index]:
                all_symptoms.append(symptom)
    

#     disease_symptoms_dict = {'Disease': all_names, 'ID': all_indices, 'Symptoms': all_symptoms}
#     all_disease_symptoms = pd.DataFrame(disease_symptoms_dict) 
#     all_disease_symptoms.to_csv('NHS_Disease_Symptoms.csv')
            



main()


