#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" Computing GC Content """

import sys
import re

if len(sys.argv) < 2:
    exit("Please specify file")

file = open(sys.argv[1]).read().replace('\n','')
title = re.findall('Rosalind_[0-9]{4}', file)
dna = re.findall('[ATGC]+', file)
gc_content = [(( x.count('G')+x.count('C') ) * 100.0 / len(x) ) for x in dna]

max_index = gc_content.index(max(gc_content))
print title[max_index]
print gc_content[max_index]
