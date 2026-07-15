import random

suits = ["diamonds", "hearts", "spades", "clubs"]
all_suits = suits + ["joker"]

class Game:
    def __init__(self, name: str, players: list = [], trump_suit: str = '', current_suit: str = ''):
        self.name = name
        self.players = players
        self.trump_suit = trump_suit
        self.current_suit = current_suit

class Card:
    def __init__(self, rank: int, suit: str, owner: int = 0, game: Game = None):
        self.rank = rank
        self.suit = suit
        self.owner = owner
        self.game = game

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def __hash__(self):
        return hash(str(self.rank) + self.suit)

    def __eq__(self, other):
        return True if self.rank == other.rank and self.suit == other.suit else False

    def __gt__(self, other):
        if not (self.game.trump_suit and self.game.current_suit):
            if self.suit == other.suit:
                return True if self.rank > other.rank else False
            else: return False

        elif self.suit == self.game.trump_suit:
            if other.suit == Card.trump_suit:
                return True if self.rank > other.rank else False
            else:
                return True

        elif self.suit == self.game.current_suit:
            if other.suit == self.game.trump_suit: return False
            else:
                if other.suit == self.game.current_suit:
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
    def __init__(self, id: int, cards: list = [], game: Game = None, name: str = ''):
        self.id = id
        self.name = name
        self.cards = cards
        self.game = game
    
    def __str__(self):
        tmp = ""
        for i in self._cards:
            tmp += str(i) + '\n'
        return tmp

    def __iter__(self) -> Card:
        for i in self._cards:
            yield str(i)

    @property
    def cards(self) -> list:
        return self._cards

    @cards.setter
    def cards(self, cards):
        for card in cards:
            card.owner = self
        self._cards = cards

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    d=Deck()
    d.gen_cards()
    cards1=[]
    for i in range(5):
        cards1.append(d.pop())

    p=Player("Player 1", cards1)
    g=Game("Game 1", [p])
    c1 = Card(4, "spades")
    g.trump_suit = "hearts"
    g.current_suit = "spades"
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
    print(max(c2, c1))
    print(hash(c4), hash(c5))
    
    print(p)
    print("_____________")
    c = p.draw(13,"hearts")
    print(p)
    print(c.owner)
    print("_____________")
    p.add(d.pop())
    print(p)

