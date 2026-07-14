import cards
import random

class Hokm:
    def __init__(self):
        self.deck = cards.Deck()
        self.deck.shuffle()
        self.temp_list = []
        self.hokm=str()
        self.give_hand()
        self.palyer1=cards.player(self.temp_list)
        self.give_hand()
        self.player2=cards.player(self.temp_list)
        self.give_hand()
        self.player3=cards.player(self.temp_list)
        self.give_hand()
        self.player4=cards.player(self.temp_list)
        self.hakem=random.randint(1,4)

        if self.hakem %4 ==1:
              self.hakem=self.player1 
        elif self.hakem %4 ==2:
              self.hakem=self.player2 
        elif self.hakem %4 ==3:
              self.hakem=self.player3 
        elif self.hakem %4 ==0:
              self.hakem=self.player4

        c = 1
        for i in self.hakem:
              if c > 5:   
                  temp_n=int(input("1.diamonds\n 2.hearts\n 3.spades\n 4.clubs\nEnter hokm:"))
                  if temp_n==1:
                      self.hokm="diamonds"
                  elif temp_n==2:
                      self.hokm="hearts"
                  elif temp_n==3:
                      self.hokm="spades"
                  elif temp_n==4:
                      self.hokm="clubs"
                  break
              print(i)
              c += 1
       
        self.playerlist=[self.palyer1,self.player2,self.player3,self.player4]
        
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
        for i in range(1, n):
            self.temp_list=self.deck.pop()

