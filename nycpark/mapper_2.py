#!/usr/bin/env python
  
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    try:
        street_name = fields[24]

        if street_name:
            print('%s\t1' % street_name)
    except IndexError:
        continue

