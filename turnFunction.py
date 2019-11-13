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
    
    if firstTurn:
        firstPlayer = find2OfClubs(players)
        #firstPlayer = function finding 2 of clubs
        listOfBoard = [['2', 'clubs']]
        turnLeft = 3
    
    for i in range(turnLeft):
        
        turnPlayer = firstPlayer + i
        
        if turnPlayer > 3:
            turnPlayer = 4 - turnPlayer
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
    
    turn(players, True)


if __name__ == "__main__":
    main()

