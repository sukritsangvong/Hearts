from heartCard import *
from playable import *
from turnFunction import *
from calculateScore import *
from roundFunction import *
from takeCardFromBoard import *


      
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
    print(players)

    #hand out the starting cards --> mutate the list of cards
    for player in players:
        assignHand(player,deck, 13)
        makeSortedHand(player)

    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")
    print("list of deck:", deck)

    #test
    players[0].setHand([[['9', 'hearts']],[['2', 'clubs']],[], []])
    players[1].setHand([[['A', 'hearts']],[['5', 'clubs']],[], []])
    players[2].setHand([[['2', 'hearts']],[['7', 'clubs']],[], []])
    players[3].setHand([[['6', 'hearts']],[['8', 'clubs']],[], []])

    index2ofClubs = find2OfClubs(players)
    players, indexOfNextPlayer = turn(players, index2ofClubs, True)
    while players[0].getHand() != [[],[],[],[]]:
        players, indexOfNextPlayer = turn(players, indexOfNextPlayer, False)
      
    print('done')

if __name__ == "__main__":
    main()

