import csv
airp = open('./data/airport.csv','r',encoding='utf-8')
ap = csv.reader(airp,delimiter=",")
airport = {}
for col in ap:
    airport[col[4]] = list(col)
print(airport.get('WLS'))