#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" The Genetic Code """

import sys

intab =  ['UUU', 'CUU', 'AUU', 'GUU', 'UUC', 'CUC', 'AUC', 'GUC', 'UUA', 'CUA', 'AUA', 'GUA', 'UUG', 'CUG', 'AUG', 'GUG', 'UCU', 'CCU', 'ACU', 'GCU', 'UCC', 'CCC', 'ACC', 'GCC', 'UCA', 'CCA', 'ACA', 'GCA', 'UCG', 'CCG', 'ACG', 'GCG', 'UAU', 'CAU', 'AAU', 'GAU', 'UAC', 'CAC', 'AAC', 'GAC', 'UAA', 'CAA', 'AAA', 'GAA', 'UAG', 'CAG', 'AAG', 'GAG', 'UGU', 'CGU', 'AGU', 'GGU', 'UGC', 'CGC', 'AGC', 'GGC', 'UGA', 'CGA', 'AGA', 'GGA', 'UGG', 'CGG', 'AGG', 'GGG']
outtab = ['F',   'L',   'I',   'V',   'F',   'L',   'I',   'V',   'L',   'L',   'I',   'V',   'L',   'L',   'M',   'V',   'S',   'P',   'T',   'A',   'S',   'P',   'T',   'A',   'S',   'P',   'T',   'A',   'S',   'P',   'T',   'A',   'Y',   'H',   'N',   'D',   'Y',   'H',   'N',   'D',   '$',   'Q',   'K',   'E',   '$',   'Q',   'K',   'E',   'C',   'R',   'S',   'G',   'C',   'R',   'S',   'G',   '$',   'R',   'R',   'G',   'W',   'R',   'R',   'G']

file = open(sys.argv[1]).read()

outline = ''

for i in range(0, len(file), 3):
  j = intab.index(file[i:i+3])
	if outtab[j] == '$':
		break
	outline += outtab[j]
print outline
