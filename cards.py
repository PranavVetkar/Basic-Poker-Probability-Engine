SUITS = ['s', 'h', 'd', 'c']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

RANK_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

class Card:
    def __init__(self, card_str):
        if len(card_str) != 2:
            raise ValueError(f"Invalid card string: '{card_str}'. Expected 2 characters (e.g. 'As').")
        
        self.rank = card_str[0].upper()
        self.suit = card_str[1].lower()
        
        if self.rank not in RANKS:
            raise ValueError(f"Invalid card rank: '{self.rank}' in '{card_str}'. Must be one of {RANKS}.")
        if self.suit not in SUITS:
            raise ValueError(f"Invalid card suit: '{self.suit}' in '{card_str}'. Must be one of {SUITS}.")
            
        self.value = RANK_VALUES[self.rank]
        
    def __str__(self):
        return f"{self.rank}{self.suit}"
        
    def __repr__(self):
        return self.__str__()
        
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
        
    def __hash__(self):
        return hash((self.rank, self.suit))

class Deck:
    def __init__(self):
        self.cards = [Card(f"{r}{s}") for r in RANKS for s in SUITS]
        
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            
    def remove_cards(self, cards):
        for card in cards:
            self.remove(card)
            
    def get_remaining_cards(self):
        return list(self.cards)
