import random

class Card:
    Faces = ['zero', 'ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    Suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self, suit = 0, face = 0):
        self.face = face
        self.suit = suit

    def setFace(self, face):
        self.face = face
        
    def setSuit(self, suit):
        self.suit = suit
        
    def getFace(self):
        return self.face
    
    def getSuit(self):
        return self.suit

    def equals(self, card2):
        if self.getSuit() == card2.getSuit() :
            if self.getFace() == card2.getFace():
               return 1
    def __str__(self):
        return (self.Faces[self.face] + ' of ' + self.Suits[self.suit])

    

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    
    def print_deck(self):
        for card in self.cards:
            print (card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
    def pop(self):
        return self.cards.pop()
    
    def cardcount(self):
        return len(self.cards)

    
card1 = Card(1, 11)
print (card1)



deck = Deck()
deck.shuffle()

comp = []
player = []
comp.append(deck.pop())
print(deck.cardcount())

player.append(deck.pop())



print(deck.cardcount())
#print (deck)





                       










