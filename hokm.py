import random
import cards



class Hokm:
    def __init__(self):
        self.deck = cards.Deck()
        self.deck.shuffle()
        self.palyer1 = cards.player("1"self.give_hand(13))
        self.player2 = cards.player("2",self.give_hand(13))
        self.player3 = cards.player("3",self.give_hand(13))
        self.player4 = cards.player("4", self.give_hand(13))
        self.playerlist = [self.palyer1, self.player2, self.player3, self.player4]
        self.hakem = random.choice(self.playerlist)
        self.score=[]
        self.score=[0]=0
        self.score=[1]=1


        

        c = 1
        for i in self.hakem:
              if c <= 5:
                print(i)
                c += 1

        self.hokm = input("1.diamonds\n 2.hearts\n 3.spades\n 4.clubs\nEnter hokm:")
        cards.Card.trump_suit = self.hokm

    def Run(self):
        while True:
            self.game()

    def game(self,winner):
            temp_n = int(winner.id)
            for i in range(1,4):
                print(self.playerlist[temp_n])
                temp_card=input("Enter your card")
                t = temp_card.split()
                temp=self.playerlist[temp_n].draw(int(t[0]),t[1])
                tmp_dict = {}
                tmp_dict[temp_n]={temp}
                temp_n+=1
                if temp_n%4==0:
                    temp_n=0
            winner_card = max(tmp_dict[1],tmp_dict[2],tmp_dict[3],tmp_dict[4])
            winner(winner_card.id)
    def winner(self,winnercard):
        if winnercard in ["0","2"]:
            self.scores[0] +=1
        if winnercard in ["1","3"]:
            self.scores[1] +=1

            


             
             

    def give_hand(self, n):
        tmp = []
        for i in range(1, n):
            tmp.append(self.deck.pop())
        return tmp


c = Hokm()

