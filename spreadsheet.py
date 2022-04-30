import sys
import csv

if len(sys.argv) < 2:
    print('You need to include the path to the CSV file')
    sys.exit()

pathtocsv = sys.argv[1]

print(pathtocsv)
houses = []

with open(pathtocsv, encoding = 'latin-1') as housefile:
    reader_obj = csv.reader(housefile)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue  #skip first header row
        houses.append(row)
        print("row number: " + str(reader_obj.line_num))

for i in range(10):
    print(houses[i])