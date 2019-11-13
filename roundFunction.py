#round.py

from heartCard import *

def round(players):

    #SORT HANDS
    def sortHand(player):
        hand = player.getHand()
        sortedHand = []        

        #First, collect each suit into a distinct list   
        def sortSuits(hand, suit):
            suitList = []
            for card in hand:
                if card[1][0] == suit[0]:
                    suitList.append(card)
            return suitList
        
        #Then organize these suit lists by card value
        def orderSuits(suitList):
            orderedSuitList = []
            values = '23456789JQKA'
            minVal = 0
            for i in range(len(suitList)):
                for card in suitList:
                    if values.index(card[0]) <= minVal:
                        minVal = values.index(card[0])
                for card in suitList:
                    if values.index(card[0]):
                        orderedSuitList.append(card)
                        suitList.remove(card)
            return orderedSuitList

        for suit in ['h', 'c', 'd', 's']:
            suitList = sortSuits(hand, suit)
            orderedList = orderSuits(suitList)
            for i in range(len(orderedList)):
                sortedHand.append(orderedList[i])   
    
        return sortedHand

    for player in players:
        sortedHand = sortHand(player)
        player.setHand(sortedHand)
        print(player.getHand())
    #Identify which player takes the first turn (has 2 of clubs)
    #Prompt user to give three cards to the bots in this order L, R, across, na

    



#TEST CODE
def main():
    deck = createDeck()
    players = generatePlayers()
        for player in players:
            assignHand(player, deck, 13)

round(players)

main()
            
    
