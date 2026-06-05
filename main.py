import sys
from cards import Card
from engine import calculate_probabilities

def print_separator():
    print("-" * 60)

def main():
    print_separator()
    print("Welcome to the Basic Poker Probability Engine")
    print("Texas Hold'em - 1 vs 1 against a random opponent")
    print_separator()
    
    try:
        player_input = input("Enter your 2 hole cards (e.g., 'As Kh' for Ace of Spades, King of Hearts): ")
        player_card_strs = player_input.strip().split()
        if len(player_card_strs) != 2:
            print("Error: You must enter exactly 2 hole cards.")
            return
            
        player_cards = [Card(c) for c in player_card_strs]
        
        # Check for duplicates in player hand
        if len(set(player_cards)) != 2:
            print("Error: Duplicate cards detected in hole cards.")
            return
            
        comm_input = input("Enter known community cards, separated by space (press Enter if pre-flop): ")
        comm_card_strs = comm_input.strip().split()
        
        community_cards = []
        if comm_card_strs:
            community_cards = [Card(c) for c in comm_card_strs]
            
        if len(community_cards) not in [0, 3, 4, 5]:
            print(f"Error: Invalid number of community cards ({len(community_cards)}). Valid numbers are 0, 3, 4, or 5.")
            return
            
        all_cards = player_cards + community_cards
        if len(set(all_cards)) != len(all_cards):
            print("Error: Duplicate cards detected between hole cards and community cards.")
            return
            
        print_separator()
        print(f"Player Hand:     {' '.join(str(c) for c in player_cards)}")
        if community_cards:
            print(f"Community Cards: {' '.join(str(c) for c in community_cards)}")
        else:
            print(f"Community Cards: None (Pre-flop)")
            
        print("\nCalculating probabilities... Please wait.")
        
        (wins, ties, losses, total), method = calculate_probabilities(player_cards, community_cards)
        
        win_pct = (wins / total) * 100
        tie_pct = (ties / total) * 100
        loss_pct = (losses / total) * 100
        
        print_separator()
        print("Results:")
        print(f"Method Used:     {method}")
        print(f"Total Scenarios: {total:,}")
        print(f"Wins:            {wins:,} ({win_pct:.2f}%)")
        print(f"Ties:            {ties:,} ({tie_pct:.2f}%)")
        print(f"Losses:          {losses:,} ({loss_pct:.2f}%)")
        print_separator()
        
        print("\nMathematical Reasoning:")
        print(f"The engine evaluated {total:,} possible scenarios.")
        if len(community_cards) == 0:
            print("Since no community cards were provided (pre-flop), an exact exhaustive calculation")
            print("would require evaluating over 2 billion combinations, which is computationally expensive.")
            print("Therefore, Monte Carlo simulation with random sampling was used to approximate the odds.")
        else:
            print("The engine performed an exact combinatorial enumeration by iterating over all")
            remaining_comm = 5 - len(community_cards)
            print(f"possible remaining {remaining_comm} community cards, and all possible 2 hole cards for the opponent.")
            print("For each scenario, the best 5-card subset out of 7 cards was determined and compared.")
        
        print("The final percentages represent the ratio of winning, tying, or losing scenarios")
        print("to the total number of scenarios evaluated.")
        
    except ValueError as e:
        print(f"\nInput Error: {e}")
        print("Please ensure your cards are formatted correctly (e.g. 'As', 'Th', '2c', 'Qd').")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCalculation interrupted by user.")
        sys.exit(0)
