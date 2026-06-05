import itertools
from collections import Counter

def evaluate_5_cards(cards):
    """
    Evaluates exactly 5 cards and returns a score tuple.
    Score format: (RankClass, Tiebreaker1, Tiebreaker2, ...)
    Higher tuple means a stronger hand.
    """
    values = sorted([c.value for c in cards], reverse=True)
    suits = [c.suit for c in cards]
    
    is_flush = len(set(suits)) == 1
    
    # Check for straight
    is_straight = False
    straight_high = 0
    if values == [14, 5, 4, 3, 2]: # Low Ace Straight (A, 5, 4, 3, 2)
        is_straight = True
        straight_high = 5
    elif len(set(values)) == 5 and values[0] - values[-1] == 4:
        is_straight = True
        straight_high = values[0]
        
    value_counts = Counter(values)
    counts = sorted(value_counts.values(), reverse=True)
    
    if is_flush and is_straight:
        return (9, straight_high)
        
    if counts == [4, 1]:
        quad_val = [k for k, v in value_counts.items() if v == 4][0]
        kicker = [k for k, v in value_counts.items() if v == 1][0]
        return (8, quad_val, kicker)
        
    if counts == [3, 2]:
        trip_val = [k for k, v in value_counts.items() if v == 3][0]
        pair_val = [k for k, v in value_counts.items() if v == 2][0]
        return (7, trip_val, pair_val)
        
    if is_flush:
        return (6, *values)
        
    if is_straight:
        return (5, straight_high)
        
    if counts == [3, 1, 1]:
        trip_val = [k for k, v in value_counts.items() if v == 3][0]
        kickers = sorted([k for k, v in value_counts.items() if v == 1], reverse=True)
        return (4, trip_val, *kickers)
        
    if counts == [2, 2, 1]:
        pairs = sorted([k for k, v in value_counts.items() if v == 2], reverse=True)
        kicker = [k for k, v in value_counts.items() if v == 1][0]
        return (3, *pairs, kicker)
        
    if counts == [2, 1, 1, 1]:
        pair_val = [k for k, v in value_counts.items() if v == 2][0]
        kickers = sorted([k for k, v in value_counts.items() if v == 1], reverse=True)
        return (2, pair_val, *kickers)
        
    return (1, *values)

def evaluate_7_cards(cards):
    best_score = (-1,)
    for combo in itertools.combinations(cards, 5):
        score = evaluate_5_cards(combo)
        if score > best_score:
            best_score = score
    return best_score
