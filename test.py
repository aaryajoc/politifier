"""import csv

input_file = csv.DictReader(open("python2_ANALYZED.csv"))
output_file = open('extremes.csv', 'w')
fieldnames = ['sentence', 'PolitenessConfidence', 'ImpolitenessConfidence']
writer = csv.DictWriter(output_file, fieldnames = fieldnames)
writer.writeheader()
for row in input_file:
	pp = float(row['PolitenessConfidence'])
	if(row['BodyNOHTML']):
		if (pp < 0.7 and pp > 0.30):
			print "no ",
		else:
			writer.writerow({'sentence': row['BodyNOHTML'], 'PolitenessConfidence': row['PolitenessConfidence'], 'ImpolitenessConfidence': row['ImpolitenessConfidence']})

"""
import csv
import json
from dependency_parse import get_parses
data_file = csv.DictReader(open("neutral_sample.csv"))

elem = {}
results = []
f = open("writefileneu.txt", "a")
i = 1
print "starting loop\n\no"
for row in data_file:
	if(i>200):
		break
	text = row['Request']
	str_input = get_parses(text)
	elem = {"text": str_input['text'],
			"sentences": str_input['sentences'],
			"parses": str_input['parses'],
			"score": row['PolitenessConfidence'] }
	results.append(elem)
	print i, ":  ", elem, "\n"
	print >> f, elem
	i += 1

"""
in_file1 = open("writefile.txt", 'r')
in_file2 = open("writefileneu.txt", 'r')
in_file3 = open("writefileimp.txt", 'r')
res = []
res1 = []
res2 = []
res3 = []
for line in in_file1:
	res.append(line)

for line in in_file2:
	res.append(line)

for line in in_file3:
	res.append(line)

# print "POLITE_POSTS = ", res1
# print "NEUTRAL_POSTS = ", res2
# print "IMPOLITE_POSTS = ", res3

print "ALL_DOCS = ", res

"""