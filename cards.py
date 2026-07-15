import random

suits = ["diamonds", "hearts", "spades", "clubs"]
all_suits = suits + ["joker"]

class Card:
    trump_suit = None
    current_suit = None

    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def __hash__(self):
        return hash(str(self.rank) + self.suit)

    def __eq__(self, other):
        return True if self.rank == other.rank and self.suit == other.suit else False

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
    
    @property
    def rank(self) -> int:
        return self._rank

    @rank.setter
    def rank(self, rank):
        if 1 <= rank <= 13: self._rank = rank
        else: raise ValueError("Card rank must be between 1 and 13")

    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit):
        suit = suit.lower()
        if suit == "joker": self._rank = 1
        if suit in all_suits: self._suit = suit
        else: raise ValueError("Card suit must be spades, clubs, diamonds, hearts or joker")

class Deck: 
    def __init__(self, cards: list = []):
        self._cards = cards

    def gen_cards(self, rank_range: int = 13, suits: list = suits):
        for i in range(1, rank_range + 1):
            for j in suits:
                self._cards.append(Card(i, j.lower()))

    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        for i in self._cards:
            yield str(i)
    
    def shuffle(self):
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()

class Player:
    def __init__(self, cards: list = []):
        self._cards = cards
    
    def __str__(self):
        tmp = ""
        for i in self._cards:
            tmp += str(i) + '\n'
        return tmp

    def __iter__(self):
        for i in self._cards:
            yield str(i)

    def draw(self, r: int, s: str) -> Card:
        for i in self._cards:
            if (i.rank == r) and (i.suit ==s):
                index = self._cards.index(i)
                self.temp = self._cards[index]

        del self._cards[index]
        return self.temp
    
    def add(self, card: Card):
        self._cards.append(card)
        return 0

if __name__ == "__main__":
    c1 = Card(4, "spades")
    Card.trump_suit = "hearts"
    Card.current_suit = "spades"
    c2 = Card(5, "spades")
    c3 = Card(2, "hearts")
    c4 = Card(7, "clubs")
    c5 = Card(7, "clubs")
    print(c2 > c1, "True")
    print(c1 > c2, "False")
    print(c2 > c4, "True")
    print(c4 > c2, "False")
    print(c3 > c2, "True")
    print(c3 > c4, "True")
    print(c4 == c5, "True")
    print(c3 < c4, "False")
    print(hash(c4), hash(c5))
    
    d=Deck()
    d.gen_cards()
    cards1=[]
    for i in range(5):
        cards1.append(d.pop())

    p=Player(cards1)
    print(p)
    print("_____________")
    p.draw(13,"hearts")
    print(p)
    print("_____________")
    p.add(d.pop())
    print(p)

