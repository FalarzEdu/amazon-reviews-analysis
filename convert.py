import csv
import json

def normalize_field_names(row):
    return {key.replace('.', '_'): value for key, value in row.items()}

def make_json(csvFilePath, jsonFilePath):
    data = []
    turn_into_int = ['reviews_doRecommend', 'reviews_numHelpful', 'reviews_rating']

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for row in csvReader:
            normalized_row = normalize_field_names(row)
            
            for key in turn_into_int:
                if key in normalized_row and normalized_row[key]:
                    try:
                        normalized_row[key] = int(normalized_row[key])
                    except ValueError:
                        pass

            data.append(normalized_row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'7817_1.csv'
jsonFilePath = r'reviews.json'

make_json(csvFilePath, jsonFilePath)
