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

def sortByMin(suitList):
    orderedSuit = []
    for i in range(len(suitList)):
        minCard = findMinCard(suitList, 0)
        orderedSuit.append(minCard)
        suitList.remove(minCard)
    return orderedSuit

def makeSortedHand(player):
    hand = player.getHand()
    sortedHand = []
    for suit in ['h', 'c', 'd', 's']:
        suitList = sortSuits(hand, suit)
        orderedSuit = sortByMin(suitList)
        sortedHand.append(orderedSuit)
    player.setHand(sortedHand)

def find2OfClubs(players):
    for player in players:
        hand = player.getHand()
        if hand[1] != []:
            if hand[1][0] == ['2', 'clubs']:
                return players.index(player)
        
        

def main():
#TEST CODE
    print("-----------------------")
    players = generatePlayers()
    deck = createDeck()
    for player in players:
        assignHand(player, deck, 13)
        makeSortedHand(player)
        print(player.getHand())
        print("-----------------")
    print(find2OfClubs(players))

if __name__ == "__main__":
    main()



        
