from heartCard import *
from playable import *
from turnFunction import *
from calculateScore import *
from roundFunction import *
from takeCardFromBoard import *
from botswap import *


      
def main():
    
    #craete class of players
    #p1 = players[1]
    #p2 = players[2]
    #p3 = players[3]
    #p4 = players[4]
    
    #generate deck
    deck = createDeck()

    #generate players
    players = generatePlayers()


    #hand out the starting cards --> mutate the list of cards
    for player in players:
        assignHand(player,deck, 13)
        makeSortedHand(player)



    #test
#    players[0].setHand([[['9', 'hearts']],[['2', 'clubs'],['A', 'clubs']],[], []])
#    players[1].setHand([[['A', 'hearts'],['5', 'hearts'],['K', 'hearts']],[],[], []])
#    players[2].setHand([[['2', 'hearts']],[['7', 'clubs'],['Q', 'clubs']],[], []])
#    players[3].setHand([[['6', 'hearts']],[['8', 'clubs'],['J', 'clubs']],[], []])

    roundCount = 1
    while players[0].getScore != 100 or players[1].getScore != 100 \
        or players[2].getScore != 100 or players[3].getScore != 100:
        
        roundCount = roundCount % 4
        cardSwap(players,roundCount)
        giveSwaps(players,roundCount)
        
        print("Player 1 : ", players[0].getHand())
        print("-----------")
        print("Player 2 : ", players[1].getHand())
        print("-----------")
        print("Player 3 : ", players[2].getHand())
        print("-----------")
        print("Player 4 : ", players[3].getHand())
        print("-----------")

        index2ofClubs = find2OfClubs(players)

        players, indexOfNextPlayer, isHeartPlayed = turn(players, index2ofClubs, True, False)

        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x Turn Ended -x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")
        while players[0].getHand() != [[],[],[],[]]:
            players, indexOfNextPlayer, isHeartPlayed = turn(players, indexOfNextPlayer, False, isHeartPlayed)
            updateScore = updateScore(players[indexOfNextPlayer])
            players[indexOfNextPlayer].addScore(updateScore)

            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x Turn Ended -x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")
        
        #generate deck
        deck = createDeck()

        #generate players
        players = generatePlayers()
    
    
        #hand out the starting cards --> mutate the list of cards
        for player in players:
            assignHand(player,deck, 13)
            makeSortedHand(player)

        roundCount += 1



if __name__ == "__main__":
    main()

