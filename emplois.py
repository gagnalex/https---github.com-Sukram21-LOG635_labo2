# -*- coding: utf-8 -*-

import nltk
from nltk import *

with open ("emplois.cfg", "r") as myfile:
    grammaireText=myfile.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)
tokens = "Alice travaille pour Trio".split()


parser = parse.FeatureEarleyChartParser(grammar)
trees = parser.parse(tokens)
for tree in trees:
    print(tree)
    nltk.draw.tree.draw_trees(tree)
    print(tree.label()['SEM'])
