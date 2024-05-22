#!/usr/bin/env python
  
import sys

current_key = None
current_count = 0
results = []

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)
    count = int(count)

    if current_key == key:
        current_count += count
    else:
        if current_key:
            if 'UNKNOWN' not in current_key:
                results.append((current_key, current_count))
        current_key = key
        current_count = count

if current_key == key and 'UNKNOWN' not in current_key:
    results.append((current_key, current_count))

results.sort(key=lambda x: x[1], reverse=True)

for key, count in results[:20]:
    print('%s\t%d' % (key, count))

