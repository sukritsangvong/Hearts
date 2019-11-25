#roundFunction.py
#This module contains programs for sorting hands, swapping cards between hands,
#finding which player has the 2 of Clubs, and updating the score after a trick

from heartCard import *
from botswap import *
from heartsBoard import *
 
def sortSuits(hand, suit):
    '''Helper function for makeSortedHand. Creates lists of all the cards
        of each suit that are in the hand'''
    suitList = []
    for card in hand:
        if card[1][0] == suit[0]:
            suitList.append(card)
    return suitList

        
def findMinCard(suitList, i):
    '''Finds the smallest value card in a list of cards. Aces are high.'''
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
    '''Sorts a list by value from least to greatest'''
    orderedSuit = []
    for i in range(len(suitList)):
        minCard = findMinCard(suitList, 0)
        orderedSuit.append(minCard)
        suitList.remove(minCard)
    return orderedSuit

def makeSortedHand(player):
    '''Sorts a hand by suit and by value'''
    hand = player.getHand()
    sortedHand = []
    for suit in ['h', 'c', 'd', 's']:
        suitList = sortSuits(hand, suit)
        orderedSuit = sortByMin(suitList)
        sortedHand.append(orderedSuit)
    player.setHand(sortedHand)
    #return player

def find2OfClubs(players):
    '''Finds the player who has the 2 of clubs'''
    for player in players:
        hand = player.getHand()
        if hand[1] != []:
            if hand[1][0] == ['2', 'clubs']:
                return players.index(player)
        
def cardSwap(players, handCount, clickZone, window):       
    '''Chooses three cards for the player to pass to another player
    depending on which round it is. The player's chosen cards are displayed
    as a list in the terminal during the swap phase.'''
    if handCount == 1:
        direction = "to the left of"
    elif handCount == 2:
        direction = "to the right of"
    elif handCount == 3:
        direction = "across from"
    elif handCount == 0:
        return players
    inputPrompt = "Choose 3 cards from your hand " \
                  "to give to the player " + direction + " you: \n" \
                  "(and click them again if you want to remove them)"
    for player in players:
        hand = player.getHand()
        if player == players[0]:    #get the card choices from the player
            swapList = []
            print(inputPrompt)
            while len(swapList) < 3:
                chosenCard = getCardName(selectCard(clickZone, window), hand)
                if chosenCard not in swapList:
                    swapList.append(chosenCard)
                    print("Current swaps:", swapList)
                elif chosenCard in swapList:
                    swapList.remove(chosenCard)
                    print("Current swaps:", swapList)
            hand = hand[0] + hand[1] + hand[2] + hand[3]
        else:                       #get the card choices from the bots
            hand = hand[0] + hand[1] + hand[2] + hand[3]
            swapList = botSwap(hand)

        for swap in swapList:
            hand.remove(swap)
        player.setHand(hand)
        player.setSwaps(swapList)
    return players

def giveSwaps(players, handCount):
    '''Give the chosen cards to be swapped to the target player.
    CAN ONLY BE USED AFTER cardSwap IS RUN!'''
    if handCount == 1:
        playerIndexChange = -1
    elif handCount == 2:
        playerIndexChange = 1
    elif handCount == 3:
        playerIndexChange = 2
    elif handCount == 0:
        return players
    for player in players:
        destinationPlayerIndex = players.index(player) + playerIndexChange
        destinationPlayerIndex = destinationPlayerIndex % 4
        destPlayer = players[destinationPlayerIndex]
        for swap in player.getSwaps():
            destPlayer.appendHand(swap)
        makeSortedHand(destPlayer)
    return players    

           
def updateScore(player):
    '''Counts the cards in the player's graveyard and calculates their score
    to be added.'''
    score = 0
    graveyard = player.getGraveyard()
    for card in graveyard:
        if card[1] == 'hearts':
            score += 1
        elif card == ['Q', 'spades']:
            score += 13
    player.addScore(score)
    return player
    


#TEST CODE
'''def main():
    
    print("-----------------------")
    players = generatePlayers()
    deck = createDeck()
    for player in players:
        assignHand(player, deck, 13)
        makeSortedHand(player)
    
    print("----BEFOREEEEEEEEEEEEEEE------")
    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")

    cardSwap(players,2)
    giveSwaps(players,2)

   
    print("----AFTERRRRRRRRRRRR------")
    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")
    
if __name__ == "__main__":
    main()'''



        
