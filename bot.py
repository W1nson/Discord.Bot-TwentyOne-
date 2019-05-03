import discord
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
        
            

client = discord.Client()

@client.event
async def on_message(message):
    #id = client.get_guild(573036626570117121)
    channels = ["commands"]
    game = {'games'}
    print(message.content)
        
    if str(message.channel) in channels:
        if message.content =='!help':
            await message.channel.send('Here are some commands you can play with: \n!help: for commands\n!hello: for greetings\n!play: just to play\n!What\'s up: cheeking up on you'.format(message))

        elif message.content == '!hello':
            await message.channel.send('Hello {0.author.mention}'.format(message))

        elif message.content =='!play':
            await message.channel.send('Starting Twenty One with{0.author.mention}'.format(message))

        elif message.content =='!what\'s up':
            await message.channel.send('I\'m doing goot. HBU?'.format(message))



        
    if str(message.channel) in game:
        deck = Deck()

        if message.content == '!help':
            await message.channel.send('Welcome to TwentyOne Game!!!\nThis is how you play this game.\n!start'.format(message))
            
        elif message.content == '!start':
            await message.channel.send('The deck has created!!\nType !shuffle to shuffle the card'.format(message))
            
        elif message.content == '!shuffle':
            await message.channel.send('The deck has been shuffled\nNow Type !deal to deal the card'.format(message))
            
        elif message.content == '!deal':
            deck.shuffle()
            await message.channel.send('This is your card\n'.format(message))
            await message.channel.send(deck.pop())
            
            
                
        elif message.content == '!cardleft':
            
            await message.channel.send('# of cards left\n'.format(message))
            await message.channel.send(deck.cardcount())












      
client.run('NTczMDM2Nzc2NjMzOTI1NjMz.XMlBNA.AacK0FbxkIJ84gIYSa3tloF__40')
