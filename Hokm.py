import main
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
    
    def give_hand(self):
        for i in range(1,13):
            self.temp_list=self._card.pop()

    def game(self):







        