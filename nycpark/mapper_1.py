#!/usr/bin/env python
  
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    try:
        vehicle_make = fields[7]
        vehicle_year = fields[35]

        
        if vehicle_year.isdigit() and int(vehicle_year) > 0:
            key = '%s-%s' % (vehicle_make, vehicle_year)
        else:
            key = '%s-UNKNOWN' % vehicle_make

        print('%s\t1' % key)
    except IndexError:
        continue

