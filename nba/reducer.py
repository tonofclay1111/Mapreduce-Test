#!/usr/bin/env python

import sys

# Initialize variables to hold player-defender hit rates
player_defender_hit_rates = {}

# Process input from stdin
for line in sys.stdin:
    # Parse the input
    shooter, defender, shot_result = line.strip().split('\t')
    shot_result = int(shot_result)

    # Update hit rates
    if (shooter, defender) not in player_defender_hit_rates:
        player_defender_hit_rates[(shooter, defender)] = [0, 0]

    player_defender_hit_rates[(shooter, defender)][0] += shot_result
    player_defender_hit_rates[(shooter, defender)][1] += 1

# Calculate fear scores and find best defender for each player
for shooter in sorted(set(player for player, _ in player_defender_hit_rates.keys())):
    min_fear_score = float('inf')
    best_defender = None
    best_defender_total_shots = 0

    for defender in sorted(set(defender for _, defender in player_defender_hit_rates.keys())):
        hits, total = player_defender_hit_rates.get((shooter, defender), [0, 0])
        # Calculate fear score
        if total > 0:
            hits = int(hits)
            total = int(total)
            fear_score = float(hits) / total
        else:
            fear_score = 0.0

        if total > 5:
            if fear_score < min_fear_score or (fear_score == min_fear_score and total > best_defender_total_shots):
                min_fear_score = fear_score
                best_defender = defender
                best_defender_total_shots = total
                best_hits = hits

    # Print shooter, best defender, hits, fear score, and total shots attempted
    print("%s\t%s\t%d\t%.4f\t%d" % (shooter, best_defender, best_hits, min_fear_score, best_defender_total_shots))

