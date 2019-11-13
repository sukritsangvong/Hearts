#round.py

from heartCard import *
#def findMin(cards, values,minVal):
#    print(cards)
#    for card in cards:
#        checkCard = card[0]
#        if card[0] == '10':
#            checkCard = '0'
#        print(minVal,'minval')
##        print(values.index(checkCard))
#        if values.index(checkCard) <= minVal:
#            minVal = values.index(checkCard)
#        return minVal


#Then organize these suit lists by card value
#def orderSuits(suitList):
#    orderedSuitList = []
#    values = '234567890JQKA'
#    minVal = 12
#
#    while len(suitList) > 0:
#        minVal = findMin(suitList, values, minVal)
#        for card in suitList:
#            print('enter')
#            print(minVal)
#            if card[0] == values[minVal]:
#                orderedSuitList.append(card)
#                suitList.remove(card)
#
#    print(orderedSuitList, 'outside')
#    return orderedSuitList


#First, collect each suit into a distinct list
def sortSuits(hand, suit):
    suitList = []
    for card in hand:
        if card[1][0] == suit[0]:
            suitList.append(card)
        
    return suitList

            #SORT HANDS
def sortHand(player):
    hand = player.getHand()
    sortedHand = []

    for suit in ['h', 'c', 'd', 's']:
        suitList = sortSuits(hand, suit)
        sortedHand.append(suitList)

    return sortedHand



def round(players):
    count = 0

    for player in players:
#        print('enter', count)
        sortedHand = sortHand(player)
        print('ortedHand',sortedHand)
        player.recieveHand(sortedHand)
        print(player.getHand())
    
    return players
    #Identify which player takes the first turn (has 2 of clubs)
    #Prompt user to give three cards to the bots in this order L, R, across, na
def findMin(listOfCard):
    print('listofcard', listOfCard)
    listOrder = []
    checkingCard = listOfCard[0]
    for anotherCard in (listOfCard[1:]):
        if checkingCard[0] < anotherCard[0]:
            check = 'still lower'
        else:
            if len(listOfCard) > 1:
                print('enter')
                newCheckingCard = findMin(listOfCard[1:])
    listOrder.append(checkingCard)
    return listOrder



def sortHand(listOfCard):
    sortedList = []

    if listOfCard == []:
        return sortedList
#
#for card in (listOfCard):





#TEST CODE
def main():
    deck = createDeck()
    players = generatePlayers()
    for player in players:
        assignHand(player, deck, 13)
    
    round(players)



print(findMin([['4', 'hearts'], ['7', 'hearts'], ['2', 'hearts']]))

    
