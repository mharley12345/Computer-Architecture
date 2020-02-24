#!/usr/bin/env python3

"""Main."""

import sys

from cpu import *

cpu = CPU()
program = []
try:
    with open(sys.argv[1]) as f:

        for line in f:
            comment_split = line.split("#")
            num = comment_split[0].strip()
            if num == '':
                continue
            #convert binary to int
            value = int(num, 2)
            program.append(value)

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)



cpu.load(program)
cpu.run()