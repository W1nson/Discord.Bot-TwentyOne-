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
    def value(self):
        if self.face > 10:
            return 10
        elif self.face == 1:
            one = int(input("What do you want this value be: (1 or 11)"))
            return one
        else:
            return self.face

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


class TwentyOne:
    def playerTotal(self):
        return 


#Main

#Creating the object of decks 
deck = Deck()
deck.shuffle()

#Creating the dealer's hand and Player's hand with 2 cards dealed initially 
comp = []
compTotal = 0
player = []
playerTotal = 0 
for i in range(2):
    comp.append(deck.pop())
    compTotal += comp[i].value()
    player.append(deck.pop())
    playerTotal += player[i].value()
    deck.shuffle()
#printing how many cards left 
print("Number of cards left:",deck.cardcount())

#printing out the total of both dealer's and player's hand
print("Computer total:", compTotal)
print("Your total is:", playerTotal)

#Asking if the player wants to hit
while True: 
    hit = str(input("Do you want to hit?"))
    if hit != "y" and hit != "Y":
         break
    player.append(deck.pop())
    print(player[len(player)-1], player[len(player)-1].value())
    playerTotal += player[len(player)-1].value()
    print("Your total is:", playerTotal)
    deck.shuffle()
    



#Winning condition 

"""
player.append(deck.pop())

print(deck.cardcount())
deck.shuffle()

comp.append(deck.pop())

print(deck.cardcount())
deck.shuffle()

player.append(deck.pop())

print(deck.cardcount())
deck.shuffle()
for x in range(len(comp)):
        
    print(comp[x], comp[x].value())
"""







                       










