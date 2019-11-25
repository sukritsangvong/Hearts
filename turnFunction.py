#turnFunction.py
#Runs a single turn of the game
from heartCard import *
from playable import *
from takeCardFromBoard import *
from heartsBoard import *
import time

def turn(players, numOfStartPlayer, firstTurn, isHeartPlayed, window, clickZone):
    '''Function to run each turn of Hearts.'''
    #firstPlayer = index of the first player playing the turn
    firstPlayer = numOfStartPlayer
    listOfBoard = ['no card yet']
    
    turnLeft = 4
    addExtraTurn = 0
    
    #on the first turn, only the 2 of clubs is allowed to play
    #automatically play and remove from the player hand
    if firstTurn:
        players[firstPlayer].removeHand2Clubs()
        listOfBoard = [['2', 'clubs']]
        turnLeft = 3
        addExtraTurn = 1

        drawSlotForCardsOnBoard(window, False, listOfBoard, False)
        time.sleep(0.05)
    
    for i in range(turnLeft):
        
        turnPlayer = firstPlayer + i + addExtraTurn
        
        #put the turnPlayer to a proper number(0,1,2,or 3)
        #that coressponds witht he index of players list
        if turnPlayer > 3:
            turnPlayer = turnPlayer % 4
        
        #show cards
        print('****')
        print('Cards on the Board:', listOfBoard)
        print('****')

        #run playable function to determine the card palyed
        cardPlayed, handLeft, numPlayer = \
                    playable(players, turnPlayer, listOfBoard[0], \
                    firstTurn, isHeartPlayed, listOfBoard, clickZone, window)


        #put card played on the board list
        if listOfBoard[0] == 'no card yet':
            listOfBoard = [cardPlayed]
        else:
            listOfBoard.append(cardPlayed)

        players[numPlayer].setHand(handLeft)

        #redo the graphic for player0 hand
        if numPlayer == 0:
            player0Hand = players[0].getHand()
            clickZone = slotForCardOnHand(window, player0Hand)
        
        #redo the graphic for card on board
        drawSlotForCardsOnBoard(window, False, listOfBoard, False)
        time.sleep(0.55)

    #check whether the heart is played
    for card in listOfBoard:
        if card[1] == 'hearts':
            isHeartPlayed = True

    #print the list of board after the last player plays the card
    print('****')
    print('Cards on the Board:', listOfBoard)
    print('****')

    #redraw an empty slot on the board
    time.sleep(0.50)
    drawSlotForCardsOnBoard(window, True, None, False)
    time.sleep(0.25)
            

    indexFromStartPlayer = takeCardFromBoard(listOfBoard)
    indexOfNextPlayer = (numOfStartPlayer + indexFromStartPlayer) % 4
    players[indexOfNextPlayer].addGraveyard(listOfBoard)

    #return list of player objects, index of the player starting next turn,
    #boolean is heart played and clickZone for new axises on click
    return players, indexOfNextPlayer, isHeartPlayed, clickZone

#TEST CODE  
'''def main():
#------------------------------------------from heartCard.py
    deck = createDeck()
    players = generatePlayers()
    for player in players:
        assignHand(player,deck, 13)
        makeSortedHand(player)
#------------------------------------------from heartCard.py
    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")
    players = turn(players, True, False)
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

