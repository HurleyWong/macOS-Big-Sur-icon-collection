#!/usr/bin/env python3

import os
import numpy as np

path = '/Users/hurley/BigSurIcons/icons/'
dir = sorted(os.listdir(path), key=str.casefold)
fopen = open('/Users/hurley/BigSurIcons/icons.txt', 'w')
for d in dir:
	string = '- [x] ' + d[:-5] + '\n'
	fopen.write(string)

fopen.close()