#!/usr/bin/env python
  
import sys

current_street = None
current_count = 0
results = []

for line in sys.stdin:
    line = line.strip()
    street, count = line.split('\t', 1)
    count = int(count)

    if current_street == street:
        current_count += count
    else:
        if current_street:
            results.append((current_street, current_count))
        current_street = street
        current_count = count

if current_street == street:
    results.append((current_street, current_count))

results.sort(key=lambda x: x[1], reverse=True)

for street, count in results[:20]:
    print('%s\t%d' % (street, count))

