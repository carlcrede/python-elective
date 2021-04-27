import random as r
import string
import time as t

def time(func):
    def wrapper(*args, **kwargs):
        start = t.time()
        value = func(*args, **kwargs)
        end = t.time()
        print(f'Time to execute function: {end - start}')
        return value
    return wrapper

"""
Each card has a letter on one face, and a number on the other face.
Claim: If a card shows a vowel on one face, then its opposite face is an even number.
Question: Which card or cards must be turned over to test if this claim is true or false?
"""

def generate_set_of_cards(card_count = 4):
    alphabet = list(string.ascii_uppercase)
    cards = []
    for i in range(card_count):
        card = { 'letter': r.choice(alphabet), 'number': r.randrange(0, 10) }
        cards.append(card)
    return cards

def make_card_sets(num):
    return [ generate_set_of_cards() for i in range(num) ]

@time
def check_claim(cards):
    vowels = ['A', 'E', 'I', 'O', 'U']
    valid_sets = []
    invalid_sets = []
    for set in cards:
        valid = True
        for card in set:
            if card.get('letter') in vowels and card.get('number') % 2 != 0:
                valid = False
                break
        if valid:
            valid_sets.append(set)
        else:
            invalid_sets.append(set)
    
    return { 'passed': len(valid_sets), 'failed': len(cards)-len(valid_sets), 'failed_sets': invalid_sets }

   

                


