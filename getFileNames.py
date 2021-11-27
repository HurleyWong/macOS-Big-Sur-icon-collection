#!/usr/bin/env python3

import os
import numpy as np

path = '/Users/Hurley/Documents/Projects/MyIconProjects/macOS-Big-Sur-icon-collection/icons/'
dir = sorted(os.listdir(path), key=str.casefold)
fopen = open('/Users/Hurley/Documents/Projects/MyIconProjects/macOS-Big-Sur-icon-collection/icons.txt', 'w')
for d in dir:
	string = '- [x] ' + d[:-5] + '\n'
	fopen.write(string)

fopen.close()