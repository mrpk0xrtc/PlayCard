import random
import cards



class Hokm:
    def __init__(self):
        self.deck = cards.Deck()
        self.deck.shuffle()
        self.palyer1 = cards.Player("1",self.give_hand(13))
        self.player2 = cards.Player("2",self.give_hand(13))
        self.player3 = cards.Player("3",self.give_hand(13))
        self.player4 = cards.Player("4", self.give_hand(13))
        self.playerlist = [self.palyer1, self.player2, self.player3, self.player4]
        self.hakem = random.choice(self.playerlist)
        self.raundscore=[0,0]
        self.gamescore=[0,0]
        self.teamwinner=str()

        self.hokm = input("1.diamonds\n 2.hearts\n 3.spades\n 4.clubs\nEnter hokm:")
        cards.Card.trump_suit = self.hokm

    def Run(self):
        while True:
            self.game(self.hakem)
            if self.raundscore[0]==7:
                self.gamescore[0]+=1
                self.raundscore[0]=0
                self.raundscore[1]=0
                tmp_n=int(input("if do you to countinue enter '1' else enter '2':"))
                if tmp_n==2 :
                    if self.gamescore[0]>self.gamescore[1]:
                        print("winter team is team 1")
                    elif self.gamescore[1]>self.gamescore[0]:
                        print("winter team is team 2")
                    break
            elif self.roundscore[1]==7:
                self.gamescore[1]+=1
                self.raundscore[0]=0
                self.raundscore[1]=0
                tmp_n=int(input("if do you to countinue enter '1' else enter '2':"))
                if tmp_n==2:
                    if self.gamescore[0]>self.gamescore[1]:
                        print("winter team is team 1")
                    elif self.gamescore[1]>self.gamescore[0]:
                        print("winter team is team 2")
                    break

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
        if winnercard in ["1","3"]:
            self.roundscores[0] +=1
            if self.hakem in [self.palyer1,self.player3]:
                pass
            else :
                self.hakem=random.choice([self.palyer1,self.player3])

        if winnercard in ["2","4"]:
            self.roundscores[1] +=1
            if self.hakem in [self.player2,self.player4]:
                pass
            else :
                self.hakem=random.choice([self.player2,self.player4])

            


             
             

    def give_hand(self, n):
        tmp = []
        for i in range(1, n):
            tmp.append(self.deck.pop())
        return tmp


c = Hokm()

