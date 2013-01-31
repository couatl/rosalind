#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" Counting DNA Nucleotides """

import sys

if len(sys.argv) < 2:
    exit("Please specify file")

file = open(sys.argv[1]).read()
for c in ('A','C','G','T'):
  print file.count(c)
