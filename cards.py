import random

class Card:
    trump_suit = None
    current_suit = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __gt__(self, other):
        if not (Card.trump_suit and Card.current_suit):
            if self.suit == other.suit:
                return True if self.rank > other.rank else False
            else: return False

        elif self.suit == Card.trump_suit:
            if other.suit == Card.trump_suit:
                return True if self.rank > other.rank else False
            else:
                return True

        elif self.suit == Card.current_suit:
            if other.suit == Card.trump_suit: return False
            else:
                if other.suit == Card.current_suit:
                    return True if self.rank > other.rank else False
                else: return True
        else: return False

class Deck: 
    def __init__(self):
        self._ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self._suits = ["diamonds", "hearts", "spades", "clubs"]
        self._cards = list()

        for i in self._ranks:
            for j in self._suits:
                self._cards.append(Card(i, j.lower()))

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
    def __init__(self, cards=[]):
        self._cards = cards
    
    def __str__(self):
        self.tmp = ""

        for i in self._cards:
            self.tmp += str(i) + '\n'

        return self.tmp

    def __iter__(self):
        for i in self._cards:
            yield str(i)

    def pop(self, r, s):
        for i in self._cards:
            if (i.rank== r) and (i.suit==s):
                index=self._cards.index(i)
                self.temp=self._cards[index]

        del self._cards[index]
        return self.temp
    
    def add(self,ncard):
        self._cards.append(ncard)
        return 0

if __name__ == "__main__":
    c1 = Card(4, "spades")
    Card.trump_suit = "hearts"
    Card.current_suit = "spades"
    c2 = Card(5, "spades")
    c3 = Card(2, "hearts")
    c4 = Card(7, "clubs")
    print(c2 > c1, "True")
    print(c1 > c2, "False")
    print(c2 > c4, "True")
    print(c4 > c2, "False")
    print(c3 > c2, "True")
    print(c3 > c4, "True")
    
    d=Deck()
    cards1=[]
    for i in range(5):
        cards1.append(d.pop())

    p=Player(cards1)
    print(p)
    print("_____________")
    p.pop(13,"hearts")
    print(p)
    print("_____________")
    p.add(d.pop())
    print(p)

