import random
import cards

class Hokm:
    def __init__(self):
        self.deck = cards.Deck()
        self.deck.shuffle()
        self.palyer1 = cards.player(give_hand(13))
        self.player2 = cards.player(give_hand(13))
        self.player3 = cards.player(give_hand(13))
        self.player4 = cards.player(give_hand(13))
        self.playerlist = [self.palyer1, self.player2, self.player3, self.player4]
        self.hakem = random.choice(self.playerlist)

        if self.hakem % 4 == 1: self.hakem = self.player1
        elif self.hakem % 4 == 2: self.hakem = self.player2
        elif self.hakem % 4 == 3: self.hakem = self.player3 
        elif self.hakem % 4 == 0: self.hakem = self.player4

        c = 1
        for i in self.hakem:
              if c <= 5:
                print(i)
                c += 1

        self.hokm = input("1.diamonds\n 2.hearts\n 3.spades\n 4.clubs\nEnter hokm:")

    def game(self,winner):
         while True:
             temp_n=0
             for i in self.playerlist:
                 if winner==i: break
                 temp_n+=1
             for i in range(1,4):
                  self.playerlist[temp_n].pop()
                  temp_n+=1
                  if temp_n%4==0:
                       temp_n=0

    def give_hand(self, n):
        tmp = []
        for i in range(1, n):
            tmp.append(self.deck.pop())
        return tmp


c = Hokm()

