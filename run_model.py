import sys
import os
import cPickle
import numpy as np
import csv
import scipy
from scipy.sparse import csr_matrix
import sklearn
import nltk
from features.vectorizer import PolitenessFeatureVectorizer
from dependency_parse import get_parses

MODEL_FILENAME = os.path.join(os.path.split(__file__)[0], 'politeness-svm.p')
clf = cPickle.load(open(MODEL_FILENAME))
vectorizer = PolitenessFeatureVectorizer()

def score_text(request):
	features = vectorizer.features(request)
	fv = [features[f] for f in sorted(features.iterkeys())]
	# Single-row sparse matrix
	X = csr_matrix(np.asarray([fv]))
	probs = clf.predict_proba(X)
	# Massage return format
	probs = {"polite": probs[0][1], "impolite": probs[0][0]}
	return probs

if __name__ == "__main__":
	x = get_parses("Have you found the answer for your question? If yes would you please share it?")
	y = score(x)
	print y
    # input_text = "I use Python 3 as a serverside scripting language, and I want a way to keep users logged into my site. I don't use any framework, since I prefer to hand code pages, so how do I create session variables like in PHP in Python 3? "
    # input_file = csv.DictReader(open("python2_ANALYZED.csv"))
    # output_file = open('New_Model.csv', 'a')
    # fieldnames = ['sentence', 'PolitenessConfidenceModel', 'PolitenessConfidenceNew', 'ImpolitenessConfidenceModel', 'ImpolitenessConfidenceNew']
    # writer = csv.DictWriter(output_file, fieldnames = fieldnames)
    # # writer.writeheader()
    # for i, row in enumerate(input_file):
    # 	if(i>7728):
	   #  	pp = float(row['PolitenessConfidence'])
	   #  	if(row['BodyNOHTML']):
				# pp = float(row['PolitenessConfidence'])
				# input_text = row['BodyNOHTML']
				# if not(pp < 0.7 and pp > 0.30):
				# 	doc = get_parses(input_text)
				# 	probs = score(doc)
				# 	writer.writerow({'sentence': row['BodyNOHTML'], 'PolitenessConfidenceModel': row['PolitenessConfidence'], 'PolitenessConfidenceNew': probs['polite'], 'ImpolitenessConfidenceModel': row['ImpolitenessConfidence'], 'ImpolitenessConfidenceNew': probs['impolite']})




# print "===================="
# print "Text: ", doc['text']
# print "\tP(polite) = %.3f" % probs['polite']
# print "\tP(impolite) = %.3f" % probs['impolite']
# print "\n"