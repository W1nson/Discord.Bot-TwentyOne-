import discord
import random
import TwentyOne as TO



client = discord.Client()

deck = TO.Deck()
player = TO.Hand(deck)
dealer = TO.Hand(deck)


@client.event
async def on_message(message):
    id = client.get_guild(573036626570117121)
    channels = ["commands"]
    game = {'blackjack'}
    #print(message.content)
        
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
        if message.content == '!help':
            await message.channel.send('!deal: To start the game.\n!reset: To reset the game.\n!stop: To exit the game.\n')
        elif message.content == '!start':
            await message.channel.send('Welcome to TwentyOne Game!!!\nType \'!deal\' to start playing!\nType \'resest\' to Reset.\n\n')
            
        elif message.content == '!deal':
            await message.channel.send('Now is dealing the cards to dealer and {0.author.mention}'.format(message))
            player.delete()
            dealer.delete()
            print(deck.cardcount())
            for i in range(2):
                player.addCard()
                dealer.addCard()

                     
            await message.channel.send('The Dealer has:\n' + dealer.printlast())
            await message.channel.send('You have:\n' + player.print())
            await message.channel.send('Do you want to [h]it, [s]tand, or [q]uit:')

            
        elif message.content == 'h':
            player.hit()
            await message.channel.send(player.print())
            await message.channel.send('Do you want to [h]it, [s]tand, or [q]uit:')

            '''while dealer.Total() < 17:
                  dealer.hit()
            #await message.channel.send(player.compare(dealer))
            #await message.channel.send("Enter !deal to start again")
            #deck.build()
                '''
        elif message.content == 's':
            while dealer.Total() < 17:
                dealer.hit()
            await message.channel.send(player.compare(dealer))
            await message.channel.send("Enter !deal to start again")
            deck.build()
            
            
        elif message.content == 'q':
            await message.channel.send("Enter !deal to start again")
            deck.build()

        elif message.content == 'reset':
            await message.channel.send("Type !deal to start playing!")
            deck.build()

        elif message.content == '!stop':
            await message.channel.send("Now Exiting the game.")





            

        
                       
            

client.run('NTczMDM2Nzc2NjMzOTI1NjMz.XMlBNA.AacK0FbxkIJ84gIYSa3tloF__40')
