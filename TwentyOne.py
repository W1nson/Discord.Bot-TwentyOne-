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
        
    def getValue(self):
        if self.face > 10:
            return 10
        return self.face
    
    def __str__(self):
        return (self.Faces[self.face] + ' of ' + self.Suits[self.suit])


    

class Deck:
    #creates a deck of 52 cards 
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
                
    #prints out 52 cards 
    def print_deck(self):
        for card in self.cards:
            print (card)
   
    #shuffles the deck into random order
    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    #removes all card from the deck 
    def build(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        
    #removes the card and return the card 
    def pop(self):
        return self.cards.pop()

    #returns # of cards left in the deck
    def cardcount(self):
        return len(self.cards)

    #turn it to string
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s

class Hand:

    #initialize the hand with the deck 
    def __init__(self, deck = Deck()):
        self.deck = deck
        self.hand = []

    #adds a card from the deck to the hand
    def addCard(self):
        self.deck.shuffle()
        self.hand.append(self.deck.pop())

    #calculates the total value of on the hand
    def Total(self):
        total = 0
        for card in self.hand:
            if card.face > 10:
                total+= 10
            elif card == 1:
                if total >= 11:
                    total+= 1
                else:
                    total+= 11
            else:
                total+= card.getValue()
        return total
    
    #This method is asking the user to hit if they want to add more cards 
    def hit(self):
            self.addCard()

            
    #prints out cards in hands and the total value
    def print(self):
        string = ""
        for i in range(len(self.hand)):
            string += str(self.hand[i])+ " " + str(self.hand[i].getValue()) + "\n"
        string = string + str(self.Total()) + "\n"
        return string

    #deletes the whole hand
    def delete(self):
        self.hand = []
    
    
    #prints out the last card of the hand
    def printlast(self):
        last = str(self.hand[len(self.hand)-1]) +" " + str(self.hand[len(self.hand)-1].getValue()) + "\n"
        return last

    def compare(self, hand):
        result = "YOU: \n" + self.print() + "\nDealer:\n" + hand.print()
        
        if self.Total() == 21:
            result += "\nCongratulations! You got a Blackjack!\n"    	
        elif hand.Total() == 21:		
            result += "\nSorry, you lose. The dealer got a blackjack.\n"
        elif self.Total() > 21:
            result += "\nSorry. You busted. You lose.\n"
        elif hand.Total() > 21:			   
            result += "\nDealer busts. You win!\n"
        elif self.Total() < hand.Total():
            result += "\nSorry. Your score isn't higher than the dealer. You lose.\n"
        elif self.Total() > hand.Total():			   
            result += "\nCongratulations. Your score is higher than the dealer. You win\n"
        return result 
#Main
"""
def main():
    while True:
        choice = 0
        deck = Deck()
        player = Hand(deck)
        dealer = Hand(deck)
        
        for i in range(2):
            player.addCard()
            dealer.addCard()

        while choice != "q":
            print("The Dealer has:")
            dealer.printlast()
            print()
            print("You have:")
            player.print()
            print()
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            if choice == "h":
                player.hit()
                while dealer.Total() < 17:
                    dealer.hit()
                player.compare(dealer)
                break
            elif choice == "s":
                while dealer.Total() < 17:
                    dealer.hit()
                player.compare(dealer)
                break
            elif choice == "q":
                break 
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == 'n':
            break


if __name__== "__main__":
    main()


"""


                       










