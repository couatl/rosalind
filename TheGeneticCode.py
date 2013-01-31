#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" The Genetic Code """

import sys

keys =   ['UUU', 'CUU', 'AUU', 'GUU', 'UUC', 'CUC', 'AUC', 'GUC', 'UUA', 'CUA', 'AUA', 'GUA', 'UUG', 'CUG', 'AUG', 'GUG', 'UCU', 'CCU', 'ACU', 'GCU', 'UCC', 'CCC', 'ACC', 'GCC', 'UCA', 'CCA', 'ACA', 'GCA', 'UCG', 'CCG', 'ACG', 'GCG', 'UAU', 'CAU', 'AAU', 'GAU', 'UAC', 'CAC', 'AAC', 'GAC', 'UAA', 'CAA', 'AAA', 'GAA', 'UAG', 'CAG', 'AAG', 'GAG', 'UGU', 'CGU', 'AGU', 'GGU', 'UGC', 'CGC', 'AGC', 'GGC', 'UGA', 'CGA', 'AGA', 'GGA', 'UGG', 'CGG', 'AGG', 'GGG']
values = ['F',   'L',   'I',   'V',   'F',   'L',   'I',   'V',   'L',   'L',   'I',   'V',   'L',   'L',   'M',   'V',   'S',   'P',   'T',   'A',   'S',   'P',   'T',   'A',   'S',   'P',   'T',   'A',   'S',   'P',   'T',   'A',   'Y',   'H',   'N',   'D',   'Y',   'H',   'N',   'D',   '$',   'Q',   'K',   'E',   '$',   'Q',   'K',   'E',   'C',   'R',   'S',   'G',   'C',   'R',   'S',   'G',   '$',   'R',   'R',   'G',   'W',   'R',   'R',   'G']
dictionary = dict(zip(keys, values))

file = open(sys.argv[1]).read()
outline = ''

for i in range(0, len(file), 3):
	if dictionary[file[i:i+3]] == '$':
		break
	outline += dictionary[file[i:i+3]]
print outline
