import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.parse.corenlp import CoreNLPDependencyParser

def get_parses(inputs):
	dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
	sentences = sent_tokenize(inputs)
	elem = {}
	parses = []
	for text in sentences:
		token_words = word_tokenize(text)
		parse, = dep_parser.raw_parse(text)
		parse1 = []
		for governor, dep, dependent in parse.triples():
			lst = []
			# print governor, dep, dependent
			try:
				lst.append(dep)
				lst.append("(")
				lst.append(governor[0])
				lst.append("-")
				lst.append(str(token_words.index(governor[0])+1))
				lst.append(", ")
				lst.append(dependent[0])
				lst.append("-")
				lst.append(str(token_words.index(dependent[0])+1))
				lst.append(")")
				parse1.append("".join(lst))
			except:
				continue
		parses.append(parse1)


	elem = {"text": inputs,
			"sentences": sentences,
			"parses": parses }

	return(elem)
