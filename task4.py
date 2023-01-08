import json
import csv


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename='', delimiter=','):
    json_array = []

    with open(filename) as csv_f:
        csv_reader = csv.DictReader(csv_f, delimiter=delimiter)

        for row in csv_reader:
            json_array.append(row)
        return json_array


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
