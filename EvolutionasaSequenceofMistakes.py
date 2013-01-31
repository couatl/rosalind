#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" Evolution as a Sequence of Mistakes """

import sys
import re

def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

if len(sys.argv) < 2:
    exit("Please specify file")

file = open(sys.argv[1])
line1 = file.readline().rstrip('\n')
line2 = file.readline().rstrip('\n')

print hamming_distance(line1,line2)
