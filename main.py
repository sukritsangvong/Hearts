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
    Tie = False
    roundCount = 1
    while players[0].getScore != 100 or players[1].getScore != 100 \
        or players[2].getScore != 100 or players[3].getScore != 100 or Tie:
        
        roundCount = roundCount % 4
        cardSwap(players,roundCount)
        giveSwaps(players,roundCount)
        
        '''print("Player 1 : ", players[0].getHand())
        print("-----------")
        print("Player 2 : ", players[1].getHand())
        print("-----------")
        print("Player 3 : ", players[2].getHand())
        print("-----------")
        print("Player 4 : ", players[3].getHand())
        print("-----------")'''

        index2ofClubs = find2OfClubs(players)

        players, indexOfNextPlayer, isHeartPlayed = turn(players, index2ofClubs, True, False)

        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x Turn Ended -x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")
        while players[0].getHand() != [[],[],[],[]]:
            players, indexOfNextPlayer, isHeartPlayed = turn(players, indexOfNextPlayer, False, isHeartPlayed)
            updateScore(players[indexOfNextPlayer])
            players[indexOfNextPlayer].clearGraveyard()
            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x Turn Ended -x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")

        #generate new deck
        deck = createDeck()

        #give new hands
        for player in players:
            assignHand(player,deck, 13)
            makeSortedHand(player)

        #new round
        roundCount += 1

        #determining if there is a tie at end of round
        winningPlayerIndex = 0
        lowestScore = 100
        for player in players:  
            if player.getScore() < lowestScore:
                lowestScore = player.getScore()
        lowestScoreCount = 0
        for player in players:
            if player.getScore() == lowestScore:
                lowestScoreCount += 1
                winningPlayerIndex = players.index(player)
        if lowestScoreCount > 1:
            Tie = True
       
            
    print("Game Over! Player", winningPlayerIndex + 1, "wins!")

if __name__ == "__main__":
    main()

