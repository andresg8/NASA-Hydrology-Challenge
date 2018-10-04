import csv
import urllib.request
import math

def fetch_data() -> ".csv":
    url =  'http://rapid-hub.org/data/angles_UCI_CS.csv'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
        return data
    except:
        print("url: " + url + " currently unreachable")

def parse_data(decodedData: str) -> [[]]:
    values = []
    for line in decodedData[1:]:
        if line: values.append(line.split(','))
    return values

def print_data(data: ".csv"):
    data = data.decode('utf-8')
    lines = data.split('\r\n')
    first = lines[0].split(',')
    print(first[0].strip() + '\t' + first[1].strip() + '\t' + "cosine_values")
    values = parse_data(lines)
    for value in values:
        print('{}\t\t{}\t\t{:.3f}'.format(value[0], value[1], math.cos(math.radians(int(value[1])))))

if __name__ == "__main__":
    data = fetch_data()
    print_data(data)

