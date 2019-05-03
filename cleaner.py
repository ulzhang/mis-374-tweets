from collections import Counter
import csv

with open('unclean.csv','r') as in_file, open('cleaned.csv','w') as out_file:

    lines = Counter(in_file.readlines())

    for itm in lines:
        out_file.write(itm)

with open('cleaned.csv','r') as in_file, open('clean.csv','w') as out_file:

    reader = csv.reader(in_file)

    inputm = []

    for itm in reader:
        inputm.append(itm)
        if len(inputm) != 4:
            pass
        else:
            myList = ','.join(map(str, inputm))
            out_file.write(myList)