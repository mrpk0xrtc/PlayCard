import random

class deck:
    def __init__(self):
        self.card_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.type=["del","pik","kishniz","hkesht"]
        self.all_cards=list()
        for i in self.card_list:
            for j in self.type:
                self.all_cards.append(card(i,j))
    def __iter__(self):
        for i in self.all_cards:
            yield str(i)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def pop(self):
        return self.all_cards.pop()
class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    


cards=deck()
cards.shuffle()
for i in cards: print(i)
