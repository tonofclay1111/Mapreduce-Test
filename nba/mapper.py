#!/usr/bin/env python

import sys
import csv

# Define the constant for indicating shot made
SHOT_MADE = 1

# Parse input from stdin
reader = csv.reader(sys.stdin)
next(reader)  # Skip header row
for row in reader:
    # Extract relevant columns
    shooter = row[-2]
    defender = row[14]  # Using column 14 instead of 15 for defender's player name
    shot_result = int(row[17])

    # Emit key-value pair for each player with their defender and shot result
    print("%s\t%s\t%s" % (shooter, defender, shot_result))
