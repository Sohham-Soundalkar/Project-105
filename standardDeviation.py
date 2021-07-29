import csv
import math

with open('data.csv', newline='') as d1:
    reader = csv.reader(d1)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    n = len(data)
    total = 0

    for i in data:
        total += int(i)

    mean = total/n
    return mean

squaredList = []
for a in data:
    number = int(a) - mean(data)
    number = number **2
    squaredList.append(number)

sum = 0
for b in squaredList:
    sum = sum + b

result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)