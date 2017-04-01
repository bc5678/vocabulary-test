# -*- codec: utf-8 -*-
import random

f = open('my_vocabulary.txt', 'r')
vocabulary_list = []

for line in f.readlines():
	vocabulary_list.append(line.rstrip().split('\t'))

f.close()

while (True):
	r = random.choice(range(len(vocabulary_list)))
	print(vocabulary_list[r][0])
	ans = input('Your answer: ')
	if ans in vocabulary_list[r][1]:
		print('***** Correct! *****\t', vocabulary_list[r][1])
	else:
		print('***** Wrong! *****')
		print(vocabulary_list[r])
	print('-'*20)
