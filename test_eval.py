from cards import Card
from evaluator import evaluate_7_cards

def test():
    # Royal Flush
    h1 = [Card('As'), Card('Ks'), Card('Qs'), Card('Js'), Card('Ts'), Card('2c'), Card('3d')]
    # Straight Flush
    h2 = [Card('Ks'), Card('Qs'), Card('Js'), Card('Ts'), Card('9s'), Card('2c'), Card('3d')]
    # Quads
    h3 = [Card('Ac'), Card('Ad'), Card('Ah'), Card('As'), Card('Ks'), Card('2c'), Card('3d')]
    # Full House
    h4 = [Card('Ac'), Card('Ad'), Card('Ah'), Card('Ks'), Card('Kc'), Card('2c'), Card('3d')]
    
    print(evaluate_7_cards(h1))
    print(evaluate_7_cards(h2))
    print(evaluate_7_cards(h3))
    print(evaluate_7_cards(h4))

    assert evaluate_7_cards(h1) > evaluate_7_cards(h2)
    assert evaluate_7_cards(h2) > evaluate_7_cards(h3)
    assert evaluate_7_cards(h3) > evaluate_7_cards(h4)
    print("Tests passed!")

if __name__ == '__main__':
    test()
