"""
Continue with the deck example and implement the:

__len__ method
__add__ method
__repr__ method
__str__ method
__setitem__ method
__delitem__ method
"""

class Deck:
    def __init__(self, cards):
        self.__cards = cards

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return Deck(self.cards + other.cards)

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'cards in deck: {self.cards}'

    def __setitem__(self, key, value):
        self.__cards[key] = value

    def __delitem__(self, key):
        del(self.__cards[key])