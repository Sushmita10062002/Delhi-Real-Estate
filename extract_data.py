import property_data_format
import json

# Code for extracting important features from messy json file.
def extract_data():
    with open('./scraped_data/house_output1.json', 'r') as json_file:
        data = json.load(json_file)
    response_form = {}
    i = 1
    for id, property_detail in data.items():
        print(i)
        response_form[id] = property_data_format.data_format(property_detail)
        i = i+1
    with open('./scraped_data/house_data1.json', 'a', encoding ='utf-8') as json_file:
        json.dump(response_form, json_file, ensure_ascii=False, indent=4)


