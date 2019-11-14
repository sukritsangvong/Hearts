#turn turn
from heartCard import *
from playable import *
from takeCardFromBoard import *

def turn(players, firstTurn):
    
    #firstPlayer = function to determine the first player
    firstPlayer = find2OfClubs(players)
    print(firstPlayer)
    listOfBoard = ['no card yet']
    
    turnLeft = 4
    addExtraTurn = 0
    
    if firstTurn:
        firstPlayer = find2OfClubs(players)
        #firstPlayer = function finding 2 of clubs
        players[firstPlayer].removeHand2Clubs()
        listOfBoard = [['2', 'clubs']]
        turnLeft = 3
        addExtraTurn = 1
    
    print("Player : ", players[firstPlayer].getHand())
    
    for i in range(turnLeft):
        
        turnPlayer = firstPlayer + i + addExtraTurn
        
        if turnPlayer > 3:
            turnPlayer = turnPlayer % 4
        print('****')
        print('Cards on the Board:', listOfBoard)
        print('****')
        
        cardPlayed, handLeft, numPlayer = playable(players, turnPlayer, listOfBoard[0])
        
        if listOfBoard[0] == 'no card yet':
            listOfBoard = [cardPlayed]
        else:
            listOfBoard.append(cardPlayed)


        players[numPlayer].setHand(handLeft)
        print(listOfBoard)

    return players
    
#Note: need to add graveyard list after identifing who is taking the cards

def main():
#--------------------------------------------------------------from heartCard.py
    deck = createDeck()
    players = generatePlayers()
    for player in players:
        assignHand(player,deck, 13)
        makeSortedHand(player)
#--------------------------------------------------------------from heartCard.py
    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")
    players = turn(players, True)
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

