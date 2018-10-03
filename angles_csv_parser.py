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

def print_data(data: ".csv"):
    if not data: return
    data = data.decode('utf-8')
    lines = data.split('\r\n')
    first = lines[0].split(',')
    print(first[0].strip() + '\t' + first[1].strip() + '\t' + "cosine_values")
    for line in lines[1:]:
        values = line.split(',')
        if len(values) != 2:
            break
        print('{}\t\t{}\t\t{:.3f}'.format(values[0], values[1], math.cos(math.radians(int(values[1])))))

if __name__ == "__main__":
    data = fetch_data()
    print_data(data)



#pytests:

def test_fetch_data():
    assert type(fetch_data()) == bytes
