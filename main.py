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

    index2ofClubs = find2OfClubs(players))
    players = turn(players, indexofClubs, True)
    while players[0].getHand != [[],[],[],[]]:
        players = turn(players, indexofClubs, False)


if __name__ == "__main__":
    main()

