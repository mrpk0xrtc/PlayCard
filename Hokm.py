import main
import random
class Hokm:
    def __init__(self):
        self.deck=main.Deck()
        self.deck.shuffle()
        self._card=self.deck._cards
        self.temp_list=[]
        self.give_hand()
        self.palyer1=main.player(self.temp_list)
        self.give_hand()
        self.player2=main.player(self.temp_list)
        self.give_hand()
        self.player3=main.player(self.temp_list)
        self.give_hand()
        self.player4=main.player(self.temp_list)
        self.hakem=random.randint(1,4)
            if self.hakem %4 ==1:
                   self.hakem=self.player1 
            elif self.hakem %4 ==2:
                    self.hakem=self.player2 
            elif self.hakem %4 ==3:
                    self.hakem=self.player3 
            elif self.hakem %4 ==0:
                    self.hakem=self.player4

    
    def give_hand(self):
        for i in range(1,13):
            self.temp_list=self._card.pop()
    
     
    def game(self):







        