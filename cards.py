import random

class Card:
    trump_suit = None
    trump_suit2 = True

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __gt__(self, other):
        if not (trump_suit and trump_suit2):
            if self.rank > other.rank: return True
            else: return False
        else:
            are_same = (self.suit == other.suit)
            one_is_trump = (self.suit == trump_suit)
            two_is_trump = (other.suit == trump_suit)
            if are_same:
                if self.rank > other.rank: return True
                else: return False
            elif one_is_trump: return True
            elif two_is_trump: return False

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
    def __init__(self, cards):
        self._cards = cards
    
    def __str__(self):
        self.tmp = ""

        for i in self._cards:
            self.tmp += str(i) + '\n'

        return self.tmp

    def __iter__(self):
        for i in self.cards:
            yield str(i)

    def pop(self, r, s):
        for i in self._cards:
            if (i.rank== r) and (i.suit==s):
                index=self._cards.index(i)
                self.temp=self._cards[index]

        del self._cards[index]
        return self.temp
    
if __name__ == "__main__": pass

d=Deck()
cards1=[]
for i in range(5):
    cards1.append(d.pop())

p=Player(cards1)
print(p)
print("_____________")
p.pop(13,"hearts")
print(p)

