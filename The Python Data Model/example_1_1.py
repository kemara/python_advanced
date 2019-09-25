import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 12)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


one_card = Card('7', 'diamonds')
deck = FrenchDeck()
print(len(deck))
print("Print last deck card: {}".format(deck[-1]))
print("Print first deck card: {}".format(deck[0]))

from random import choice
print("Print random deck card using random.choice: {}".format(choice(deck)))

print("Print only aces: {}".format(deck[12::13]))

print("Print using iteration:")
for card in deck[1::7]:
    print(card)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


sorted_deck = sorted(deck, key=spades_high)

print("Printing part of sorted deck:")
for card in sorted_deck[:5]:
    print(card)
