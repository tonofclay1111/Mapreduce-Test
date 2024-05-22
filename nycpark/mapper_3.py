#!/usr/bin/env python
  
import sys

color_mapping = {
    'BLK': 'BLACK',
    'BK': 'BLACK',
    'WH': 'WHITE',
    'GY': 'GRAY',
    'GRY': 'GRAY',
    'BLU': 'BLUE',
    'GREY': 'GRAY',
    'BL': 'BLACK',
    'RD': 'RED',
    'SL': 'SILVE',
    'WHT': 'WHITE',
    'GR': 'GRAY'
}

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    try:
        vehicle_color = fields[33]

        
        vehicle_color = color_mapping.get(vehicle_color, vehicle_color).upper()

        if vehicle_color:
            print('%s\t1' % vehicle_color)
    except IndexError:
        continue  

