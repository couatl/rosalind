#!/usr/bin/env python
# -*- coding: utf8 -*- 

""" Transcribing DNA into RNA """

import sys

if len(sys.argv) < 2:
    exit("Please specify file")

file = open(sys.argv[1]).read()
print file.replace('T', 'U')
