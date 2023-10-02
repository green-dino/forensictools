from __future__ import division
import nltk
from prettytable import PrettyTable
from nltk.corpus import gutenberg
from nltk.book import *


print((type(text1)))
print(len(text1))
print((len)(set(text1)))
print(text1[:10])
print(text2[:10])
      
table = PrettyTable()
PrettyTable.attributes 

#add columns
table.field_names = ['Description', 'Value']

table.add_row(['Type of text', str(type(text1))])
table.add_row(['Length of text', len(text1)])
table.add_row(['Length of set(text1)', len(set(text1)) ])
table.add_row(['First 10 elements of text1', text1[:10]])
table.add_row(['First 10 elements of Text 2',text2[:10]])
table.add_row(['fileids',gutenberg.fileids()])
table.add_row(['Concordance',text1.concordance('passion')])

hamlet_sentences = gutenberg.sents('shakespeare-hamlet.txt')

print(('length of hamlet senteces:'),len(hamlet_sentences))

print(('the count of the word horse:'), text1.count('horse'))
print(table)

vocab = nltk.FreqDist(text1)
print(('length of vocab:'),len(vocab))
print(('vocab most common:', (vocab.most_common(20))))



