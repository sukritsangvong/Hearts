#roundFunction.py
#contains functions to make both rounds and hands work

from heartCard import *
from botswap import *

#First, collect each suit into a distinct list   
def sortSuits(hand, suit):
    '''Helper function for makeSortedHand. Creates a list of all the cards
        of a given suit that are in the hand'''
    suitList = []
    for card in hand:
        if card[1][0] == suit[0]:
            suitList.append(card)
    return suitList

        
def findMinCard(suitList, i):
    '''Helper for sorting. Finds the smallest value card in a list of cards'''
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

def find2OfClubs(players):
    '''Finds the player who has the 2 of clubs'''
    for player in players:
        hand = player.getHand()
        if hand[1] != []:
            if hand[1][0] == ['2', 'clubs']:
                return players.index(player)
        
def cardSwap(players, handCount):       
    #Choose the cards that you want to pass to another player
    #Doesn't swap any cards every 4th round
    if handCount == 1:
        direction = "to the left of"
    elif handCount == 2:
        direction = "to the right of"
    elif handCount == 3:
        direction = "across from"
    elif handCount == 4:
        return players
    inputPrompt = "Choose 3 cards from your hand (by typing only the values " \
                  "and the first letters of the suits of each card separated " \
                  "by spaces) to give to the player " + direction + " you: "
    for player in players:
        hand = player.getHand()
        hand = hand[0] + hand[1] + hand[2] + hand[3]
        if player == players[0]:    #get the card choices from the player
            swapList = ['', '', '']
            while swapList[0] not in hand or swapList[1] not in hand or \
                swapList[2] not in hand or len(swapList) != 3:
                print("Current hand: ", hand)
                swapList = input(inputPrompt).split(' ')
                for i in range(len(swapList)):
                    swap = swapList[i]
                    if swap in swapList[:i] or swap in swapList[i+1:]:
                        swapList = ['', '', '']
                    for card in hand:
                        if len(swap) == 3:    #if the card to be swapped is a 10
                            if card[0] == '10' and card[1][0] == str(swap[2]):
                                swapList[i] = card
                        elif len(swap) == 2 and str(swap[0]) == card[0] \
                                            and str(swap[1]) == card[1][0]:
                            swapList[i] = card   
        else:                       #get the card choices from the bots
            swapList = botSwap(hand)
#        print("SWAPLIST:", swapList)
#        print("HAND:", hand)
        for swap in swapList:
            hand.remove(swap)
        player.setHand(hand)
        player.setSwaps(swapList)
    return players

def giveSwaps(players, handCount):
    #Give swapped cards to the target player
    #CAN ONLY BE USED AFTER cardSwap is RUN!
    if handCount == 1:
        playerIndexChange = -1
    elif handCount == 2:
        playerIndexChange = 1
    elif handCount == 3:
        playerIndexChange = 2
    elif handCount == 4:
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
    #This function will need to run at the end of every round,
    #ie, every 4th turn starting on the 4th turn
    score = player.getScore()
    graveyard = player.getGraveyard()
    for card in graveyard:
        if card[1][0] == 'h':
            score += 1
        elif card == ['Q', 'spades']:
            score += 13
    player.setScore(score)
    return player
    


#TEST CODE
def main():
    
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

    cardSwap(players,1)
    giveSwaps(players,1)

   
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
    main()



        
