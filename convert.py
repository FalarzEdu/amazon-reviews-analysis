import csv
import json

def make_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for rows in csvReader:
            data.append(rows)  # Append each row as a document

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))  # Write the list of documents
    
csvFilePath = r'7817_1.csv'
jsonFilePath = r'reviews.json'

make_json(csvFilePath, jsonFilePath)
