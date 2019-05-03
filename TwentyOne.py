import random

class Card:
    Faces = ['Zero', 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    Suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, suit = 0, face = 0):
        self.face = face
        self.suit = suit

    #set and get methods are not necessarily 
    def setFace(self, face):
        self.face = face
        
    def setSuit(self, suit):
        self.suit = suit
        
    def getFace(self):
        return self.face
    
    def getSuit(self):
        return self.suit

    def value(self):
        if self.face > 10:
            return 10
        elif self.face == 1:
            one = int(input("What do you want this value be: (1 or 11)"))
            print(self.Faces[self.face] + ' of ' + self.Suits[self.suit], one)
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

    #This mehtod is not necessarily        
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


class Hand:
    
    def __init__(self, deck = Deck()):
        self.deck = deck
        self.hand = []
        
    def addCard(self):
        self.deck.shuffle()
        self.hand.append(self.deck.pop())
        
    def Total(self):
        total = 0
        for items in self.hand:
            total += items.value()
        return total
    def hit(self):
        while True: 
            yes = str(input("Do you want to hit?"))
            if yes != "y" and yes != "Y":
                break
            player.addCard()
            print(player.printlast())
            print("Your new total is:", player.Total())
            print("Number of cards left:",deck.cardcount())

        
    def print(self):
        for i in range(len(self.hand)):
            print(self.hand[i], self.hand[i].value())

    def printlast(self):
        print(self.hand[len(self.hand)-1], self.hand[len(self.hand)-1].value())
    
#Main

#Creating the object of decks 
deck = Deck()

#Creating the dealer's hand and Player's hand with 2 cards dealed initially 
comp = Hand(deck)
player = Hand(deck)

for i in range(2):
    comp.addCard()
    player.addCard()
    deck.shuffle()

#printing how many cards left 
print("Number of cards left:",deck.cardcount())
print('computer:')
print(comp.print())
print('player:')
print(player.print())
player.hit()
#printing out the total of both dealer's and player's hand
print("Computer total:", comp.Total())
print("Your total is:", player.Total())

#Asking if the player wants to hit
"""
while True: 
    hit = str(input("Do you want to hit?"))
    if hit != "y" and hit != "Y":
         break
    player.addCard()
    print(player.printlast())
    print("Your new total is:", player.Total())
    deck.shuffle()
    print("Number of cards left:",deck.cardcount())
"""  
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







                       










