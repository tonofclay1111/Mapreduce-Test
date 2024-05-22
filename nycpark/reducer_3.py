#!/usr/bin/env python
  
import sys

current_color = None
current_count = 0
top_colors = []

def add_to_top_colors(color, count):
    top_colors.append((color, count))
    top_colors.sort(key=lambda x: x[1], reverse=True)
    if len(top_colors) > 10:
        top_colors.pop()

for line in sys.stdin:
    line = line.strip()
    color, count = line.split('\t', 1)
    count = int(count)

    if current_color == color:
        current_count += count
    else:
        if current_color:
            add_to_top_colors(current_color, current_count)
        current_color = color
        current_count = count

if current_color == color:
    add_to_top_colors(current_color, current_count)

for color, count in top_colors:
    print('%s\t%d' % (color, count))

