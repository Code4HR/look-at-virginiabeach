import csv
import re

fr = open('reportViewer.csv', 'rb')
reader = csv.reader(fr)

fw = open('appropriation.csv', 'wb')
writer = csv.writer(fw)

for row in reader:
    string1 = row[0]
    if any(c.isdigit() for c in string1) and "Fiscal Year" not in string1:
        fundID = string1[:3]
        fund = string1[3:].strip()
    if any("Appropriation Totals" in s for s in row):
        appropriation = row[8]
        new_data = fundID, fund, appropriation
        writer.writerow(new_data)

fr.close()
fw.close()
