#roundhand.py
#contains functions to make both rounds and hands work

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
        
def cardSwap(players, handCount):
    '''This function will be called at the beginning of every hand (or every 13 rounds)'''       
    if handCount == 1:
        direction = "to the left of"
        playerIndexChange = -1
    elif handCount == 2:
        direction = "to the right of"
        playerIndexChange = 1
    elif handCount == 3:
        direction == "across from"
        playerIndexChange = 2
    #No swap in the 4th round
    inputPrompt = "Choose 3 cards from your hand (by typing only the values " \
                  "and the first letters of the suits of each card separated " \
                  "by commas to give to the player " + direction + " you: "
    for player in players:
        hand = player.getHand()
        if player == players[0]:    #get the card choices from the player
            swapList = ['', '', '']
            while swapList[0] not in hand and swapList[1] not in hand and #Need hand to be only a double list
                  swapList[2] not in hand or len(swapList) != 3:
                print("Current hand: ", hand)
                swapList = input(inputPrompt).split(',')
                for i in range(len(swapList)):
                    swap = swapList[i]
                    print(swap)
                    for suit in hand:
                        for card in suit:
                            #print(card, end="")
                            if len(swap) == 3:
                                #if the card to be swapped is a 10
                                if card[0] == '10' and card[1][0] == str(swap[2]):
                                    print(card)
                                    swapList[i] = card
                                    print(swap)
                            elif len(swap) == 2 and str(swap[0]) == card[0] \
                                                and str(swap[1]) == card[1][0]:
                                swapList[i] = card
                print(swapList)
                print("----------")
        else:                        #get the card choices from the bots
            swapList = botSwap(hand)

        destinationPlayerIndex = players.index(player) + playerIndexChange
        if destinationPlayerIndex > 3:
            destinationPlayerIndex -= 4
        elif destinationPlayerIndex < 0:
            destinationPlayerIndex += 4
        for swap in swapList:
            hand.remove(swap)
            players[destinationPlayerIndex].addtoHand(swap)

           
'''def updateScore(player, graveyard):
    This function will need to run at the end of every round,
        ie, every 4th turn starting on the 4th turn
    score = player.getScore()
    for card in graveyard:
        if card[1][0] == 'h':
            score += 1
        elif card == ['Q', 'spades']:
            score += 13
    player.setScore(score)'''
    
#def round(players):
    #for player in players:
        #run 4 turns then updateScore() for each player, then starts over
        #if it is the first round in a hand, the first turn must play
        #the 2 of clubs



def botSwap(botHand): #TEST
    return [['1', 'clubs'],['1', 'spades'],['1', 'hearts']]

#TEST CODE
def main():
    print("-----------------------")
    players = generatePlayers()
    deck = createDeck()
    for player in players:
        assignHand(player, deck, 13)
        makeSortedHand(player)
    cardSwap(players, 1)
    print(player[0].getHand())
    
    

if __name__ == "__main__":
    main()



        
