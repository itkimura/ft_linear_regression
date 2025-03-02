import csv

def load_data(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    print(data)
    return data
