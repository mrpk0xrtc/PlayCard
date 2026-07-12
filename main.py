import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck: 
    def __init__(self):
        self._ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self._suits = ["diamonds", "hearts", "spades", "clubs"]
        self._cards = list()

        for i in self._ranks:
            for j in self._suits:
                self._cards.append(Card(i,j))

    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        for i in self._cards:
            yield str(i)
    
    def shuffle(self):
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

class Player:
    def __init__(self,cards):
        self.cards=cards
    
    def __str__(self):
        return str(self.cards)

    def __iter__(self):
        for i in self.cards:
            yield str(i)

    def select(self, r, s):
        for i in self.cards:
            if (i.rank== r)and(i.suit==s):
                return i

cards = Deck()
# cards.shuffle()
# for i in cards: print(i)

p1_cards=list()
for i in range(5): p1_cards.append(cards.pop())
p = Player(p1_cards)
# for i in p: print(i)
c = p.select(13, "diamonds")
print(c)