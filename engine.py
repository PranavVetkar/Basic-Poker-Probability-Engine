import itertools
import random
from evaluator import evaluate_7_cards
from cards import Deck

def calculate_exact(player_cards, community_cards):
    deck = Deck()
    deck.remove_cards(player_cards)
    deck.remove_cards(community_cards)
    
    remaining_cards = deck.get_remaining_cards()
    
    wins = 0
    ties = 0
    losses = 0
    total = 0
    
    cards_needed = 5 - len(community_cards)
    
    for new_comm_cards in itertools.combinations(remaining_cards, cards_needed):
        current_community = community_cards + list(new_comm_cards)
        
        remaining_for_opp = [c for c in remaining_cards if c not in new_comm_cards]
        
        player_score = evaluate_7_cards(player_cards + current_community)
        
        for opp_cards in itertools.combinations(remaining_for_opp, 2):
            opp_score = evaluate_7_cards(list(opp_cards) + current_community)
            
            if player_score > opp_score:
                wins += 1
            elif player_score < opp_score:
                losses += 1
            else:
                ties += 1
                
            total += 1
            
    return wins, ties, losses, total

def calculate_monte_carlo(player_cards, community_cards, iterations=50000):
    deck = Deck()
    deck.remove_cards(player_cards)
    deck.remove_cards(community_cards)
    
    wins = 0
    ties = 0
    losses = 0
    
    cards_needed = 5 - len(community_cards)
    remaining_cards = deck.get_remaining_cards()
    
    for _ in range(iterations):
        sampled = random.sample(remaining_cards, cards_needed + 2)
        new_comm_cards = sampled[:cards_needed]
        opp_cards = sampled[cards_needed:]
        
        current_community = community_cards + new_comm_cards
        player_score = evaluate_7_cards(player_cards + current_community)
        opp_score = evaluate_7_cards(opp_cards + current_community)
        
        if player_score > opp_score:
            wins += 1
        elif player_score < opp_score:
            losses += 1
        else:
            ties += 1
            
    return wins, ties, losses, iterations

def calculate_probabilities(player_cards, community_cards):
    if len(community_cards) == 0:
        return calculate_monte_carlo(player_cards, community_cards), "Monte Carlo Approximation (50,000 iterations)"
    else:
        return calculate_exact(player_cards, community_cards), "Exact Combinatorial Enumeration"
