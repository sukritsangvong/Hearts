import random 

class player:

    def __init__(self):
        self.hand = []

    def reciveHand(self, cards):
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
            cardAdded = [num, "of",  suits]
            cardAdded = ' '.join(cardAdded)
            deck.append(cardAdded)

    return deck



def assignHand(deck, numberofCards):

    listofCards = []
    
    for individualHands in range(numberofCards):
        
        #random one card at a time
        card = random.choice(deck)

        #remove chosen card from the deck
        for identical in deck:
            if identical == card:
                deck.remove(identical)

        #adding card to the hand of self(class)
        listofCards.append(card)


    return listofCards

      
def main():
    
    #craete class of players
    p1 = player()
    p2 = player()
    p3 = player()
    p4 = player()
    
    #activate createDeck function
    deck = createDeck()
    
    #hand out the starting cards --> mutate the list of cards
    p1.reciveHand(assignHand(deck, 13))
    p2.reciveHand(assignHand(deck, 13))
    p3.reciveHand(assignHand(deck, 13))
    p4.reciveHand(assignHand(deck, 13))


    #test
    print("Player 1 : ", p1.getHand())
    print("-----------")
    print("Player 2 : ", p2.getHand())
    print("-----------")
    print("Player 3 : ", p3.getHand())
    print("-----------")
    print("Player 4 : ", p4.getHand())
    print("-----------")
    print("list of deck:", deck)
#
if __name__ == "__main__":
    main()

