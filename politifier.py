# from test_documents import TEST_DOCUMENTS
import json
from nltk import word_tokenize, sent_tokenize
from features.vectorizer import PolitenessFeatureVectorizer
from dependency_parse import get_parses
import pprint
from run_model import score_text


vectorizer = PolitenessFeatureVectorizer()
TEST_DOCUMENTS = []
TEST_DOCUMENTS.append(get_parses("Have you found the answer for your question? If yes would you please share it?"))
TEST_DOCUMENTS.append(get_parses("So you think this is correct. Are you sure?"))
TEST_DOCUMENTS.append(get_parses("Sorry :) I dont want to hack the system!! :) is there another way?"))
TEST_DOCUMENTS.append(get_parses("What are you trying to do?  Why can't you just store the \"Range\"?"))
TEST_DOCUMENTS.append(get_parses("That is weird.  Why can't you just store the \"Range\"?"))
TEST_DOCUMENTS.append(get_parses("This was supposed to have been moved to &lt;url&gt; per the cfd. why wasn't it moved?"))
TEST_DOCUMENTS.append(get_parses("You are wrong. But the approach is correct"))

# TEST_DOCUMENTS.append(get_parses(""))


pp = pprint.PrettyPrinter(indent=4)

fks = False
for each in TEST_DOCUMENTS:
	# print each['sentences']
	# print
	fs = vectorizer.features(each)
	for feature,score in fs.items():
		if score == 1:
			if (feature.startswith('feature_politeness')):
				# print feature
				if ('==Direct_question==' in feature):
					each['sentences'][0] = "Sorry but " + each['sentences'][0]
				# if ('==2nd_person==' in feature):
				# 	li = []
				# 	for i in each['sentences'][0].split(" "):
				# 		y = 'we' if i.lower() == 'you' else i
				# 		li.append(y)
				# 	each['sentences'] = sent_tokenize(' '.join(li))
				if ('==Direct_start==' in feature):
					li = each['sentences'][0].split(" ")
					li[0] = 'Do'
					each['sentences'][0] = ' '.join(li)
				if ('==2nd_person_start==' in feature):
					li = each['sentences'][0].split(" ")
					li[0] = 'This'
					each['sentences'][0] = ' '.join(li)
				if('==Direct_question==' in feature):
					li = each['sentences'][1].split(" ")
					li.pop(0)
					each['sentences'][1] = ' '.join(li)


# pp.pprint(TEST_DOCUMENTS)
for each in TEST_DOCUMENTS:
	print "\nINPUTS\t:\t", each['text']
	print "FEAINP\t:\t",
	fs = vectorizer.features(get_parses(each['text']))
	infeatures = []
	for feature,score in fs.items():
		if score != 0:
			if (feature.startswith('feature_politeness')):
				infeatures.append(feature)
	print infeatures
	print 'ISCORE\t:\t', score_text(get_parses(each['text']))
	
	print "\nOUTPUT\t:\t", ' '.join(each['sentences'])
	print "FEAOUT\t:\t",
	fs = vectorizer.features(get_parses(' '.join(each['sentences'])))
	outfeatures = []
	for feature,score in fs.items():
		if score != 0:
			if (feature.startswith('feature_politeness')):
				outfeatures.append(feature)
	print outfeatures
	# print (list(set(infeatures) - set(outfeatures)))
	print "OSCORE\t:\t", score_text(get_parses(' '.join(each['sentences'])))
	print '-'*80 
	print

