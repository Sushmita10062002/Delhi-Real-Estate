import json

# code for extracting locality_id for each property
# extracted locality_id is saved into locality.json
def extracting_locality_id():
    with open('./scraped_data/data/output.json', 'r') as json_file:
        data = json.load(json_file)
    with open('./scraped_data/data/output1.json', 'r') as json_file:
        data1 = json.load(json_file)
    with open('./scraped_data/data/output2.json', 'r') as json_file:
        data2 = json.load(json_file)
    with open('./scraped_data/data/output3.json', 'r') as json_file:
        data3 = json.load(json_file)
    with open('./scraped_data/data/house_output.json', 'r') as json_file:
        data4 = json.load(json_file)
    with open('./scraped_data/data/house_output1.json', 'r') as json_file:
        data5 = json.load(json_file)
    response_form = {}
    i = 0
    for id, property_detail in data.items():
        response_form[id] = property_detail["location"]["LOCALITY_ID"]
        i = i+1
    for id, property_detail in data1.items():
        response_form[id] = property_detail["location"]["LOCALITY_ID"]
        i = i+1
    for id, property_detail in data2.items():
        response_form[id] = property_detail["location"]["LOCALITY_ID"]
        i = i+1
    for id, property_detail in data3.items():
        response_form[id] = property_detail["location"]["LOCALITY_ID"]
        i = i+1
    for id, property_detail in data4.items():
        response_form[id] = property_detail["location"]["LOCALITY_ID"]
        i = i+1
    for id, property_detail in data5.items():
        response_form[id] = property_detail["location"]["LOCALITY_ID"]
        i = i+1
    with open('./scraped_data/cleaned/locality_data.json', 'a', encoding ='utf-8') as json_file:
        json.dump(response_form, json_file, ensure_ascii=False, indent=4)

