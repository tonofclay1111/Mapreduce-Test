#!/usr/bin/env python
import sys

current_day = None
current_count = 0
day = None

for line in sys.stdin:
    line = line.strip()
    day, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_day == day:
        current_count += count
    else:
        if current_day:
            print('%s\t%d' % (current_day, current_count))
        current_day = day
        current_count = count

if current_day == day:
    print('%s\t%d' % (current_day, current_count))