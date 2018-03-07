import csv 

with open('file_name', 'rb') as f:
	reader = csv.reader(f, delimite='\t')
	for row in reader:
		data = row[0]
		symbol = row[1]
		closing_price = float(row[2])
		process(data, sumbol, closing_price)
