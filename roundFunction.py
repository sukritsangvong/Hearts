#round.py

from heartCard import *

#First, collect each suit into a distinct list   
def sortSuits(hand, suit):
    suitList = []
    for card in hand:
        if card[1][0] == suit[0]:
            suitList.append(card)
    return suitList
        
def findMinCard(suitList, i):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
              'J', 'Q', 'K', 'A']
    card = suitList[i]
    if i == len(suitList) - 1:
        return card
    else:
        minCard = values.index(card[0])
        minOfRest = values.index(findMinCard(suitList, i + 1)[0])
        if minCard < minOfRest:
            return card
        if minCard > minOfRest:
            return findMinCard(suitList, i + 1)


players = generatePlayers()
deck = createDeck()
assignHand(players[0], deck, 13)
hand = sortSuits(players[0].getHand(), 'hearts')
print(hand)
print(findMinCard(hand, 0))

        
