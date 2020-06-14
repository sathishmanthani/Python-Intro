import csv

with open('accounts.csv','r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

with open('accounts_2.csv', mode='w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([1,'Sam',2000])
    writer.writerow ([2, 'Matt', 5000])
    writer.writerow ([3, 'Tina', 6000])

with open('accounts.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        print(line)

