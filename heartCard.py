import random 

def generatePlayers():
    players = []
    for i in range(4):
        players.append(player())
    return players
        
    
class player:

    def __init__(self):
        self.hand = []

    def recieveHand(self, cards):
        self.hand = cards
        return self.hand
    
    def addHand(self, card):
        self.hand.append(card)
        return self.hand

    def getHand(self):
        return self.hand
    

def createDeck():
 
    #create a deck
    deck = []
    for suits in ['clubs', "diamonds", "hearts", "spades"]:
        for num in ['2', '3','4', '5', '6', '7', '8', '9','10',\
                   'J', 'Q', 'K', 'A']:
            cardAdded = [num, suits]
            #cardAdded = ' '.join(cardAdded)
            deck.append(cardAdded)

    return deck



def assignHand(self, deck, numberofCards):

    listofCards = []
    
    for individualHands in range(numberofCards):
        
        #random one card at a time
        card = random.choice(deck)

        #remove chosen card from the deck
        for identical in deck:
            if identical == card:
                deck.remove(identical)

        #adding card to the hand of self(class)
        self.addHand(card)


    return listofCards

      
def main():
    
    #craete class of players
    #p1 = players[1]
    #p2 = players[2]
    #p3 = players[3]
    #p4 = players[4]
    
    #generate deck
    deck = createDeck()

    #generate players
    players = generatePlayers()
    print(players)

    #hand out the starting cards --> mutate the list of cards
    for i in range(4):
        assignHand(players[i],deck, 13)
    
    '''#listHearts = []
    #listClubs = []
    #listSpades = []
    #listDiamonds = []
    #for eachCard in p1.getHand():

        #if eachCard[5:] == 'hearts':
            #listHearts.append(eachCard)

        if eachCard[5:] == 'clubs':
            listClubs.append(eachCard)

        if eachCard[5:] == 'spades':
            listSpades.append(eachCard)

        if eachCard[5:] == 'diamonds':
            listDiamonds.append(eachCard)

    print(listHearts)'''

    

    
    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")
    print("list of deck:", deck)

if __name__ == "__main__":
    main()

