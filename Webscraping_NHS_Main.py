import requests
from bs4 import BeautifulSoup
import re
import matplotlib as plt

def finder(everything):
    for index in range(len(everything)):
        p = everything[index].text
        sentence = p.split(' ')
        if 'include:' and 'Symptoms' in sentence:
            symptom_header = ' '.join(sentence)
            return index

def main():
    symptom_url = 'https://www.nhsinform.scot/illnesses-and-conditions/cancer/cancer-types-in-adults/acute-lymphoblastic-leukaemia/#symptoms-of-acute-lymphoblastic-leukaemia'
    source_code = requests.get(symptom_url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")

    everything = parsed_code.find_all('p')
    divs = parsed_code.find_all('div',class_="editor")
    counter = 0
#     for index in range(10):
#         counter +=1
#         print(counter)
#         print(divs[index])
#         if 'symptoms' in divs[index]:
#             print(divs[index])
    
    symptoms_chunk = divs[1].find_all('ul')
    
    symptoms = []

    for symptoms in symptoms_chunk:
        for symptom in symptoms:
            
            symptom = re.sub(r'[\r\t\n ]+', ' ',symptom).strip()
            symptoms.append(symptom)
    print(symptoms)
        
        
    
    
    uls = parsed_code.find_all('ul')

# find the first few li bullet points after the symptom header and stop till the next major heading
    
    index = finder(everything)
#     print(everything[index])
# index 6 and 7

#     print(uls[6])
#     print(uls[7])

main()