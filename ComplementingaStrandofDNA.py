#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" Complementing a Strand of DNA """

import sys
from string import maketrans   # Required to call maketrans function.

if len(sys.argv) < 2:
    exit("Please specify file")

intab = "ATCG"
outtab = "TAGC"
trantab = maketrans(intab, outtab)
file = open(sys.argv[1]).read()
print file.translate(trantab)[::-1]
