import csv
import urllib.request
import math

url =  'http://rapid-hub.org/data/angles_UCI_CS.csv'
accessible = False
try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
    accessible = True
except:
    print("url: " + url + " currently unreachable")

if accessible:
    data = data.decode('utf-8')
    lines = data.split('\r\n')
    first = lines[0].split(',')
    print(first[0].strip() + '\t' + first[1].strip() + '\t' + "cosine_values")
    for line in lines[1:]:
        values = line.split(',')
        if len(values) != 2:
            break
        print('{}\t\t{}\t\t{:.3f}'.format(values[0], values[1], math.cos(math.radians(int(values[1])))))
