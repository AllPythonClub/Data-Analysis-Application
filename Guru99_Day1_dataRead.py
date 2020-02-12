#import necessary modules
#'''
import csv

reader = csv.DictReader(open("Emissions.csv"))
for raw in reader:
    print(raw)
#'''

import pandas
result = pandas.read_csv('Emissions.csv')
print(result)