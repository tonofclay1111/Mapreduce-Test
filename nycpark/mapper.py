#!/usr/bin/env python
  
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    try:
        issue_date = fields[4]
        issue_date = datetime.strptime(issue_date, '%m/%d/%Y')
        day_of_week = issue_date.strftime('%A')
        print('%s\t1' % day_of_week)
    except (IndexError, ValueError):
        continue 

