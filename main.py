#Final project for CS 111 with DLN
#PJ Sangvong and Ben Aoki-Sherwood
#Hearts

from heartCard import *
from playable import *
from turnFunction import *
from calculateScore import *
from roundFunction import *
from takeCardFromBoard import *
from botswap import *
from heartsBoard import *

      
def main():
    '''Runs the card game Hearts displayed in a graphics window.'''
    input("Welcome to Hearts! Press ENTER to start.")

    #Create the players and the starting deck
    deck, players = createDeck(), generatePlayers()
    
    #Deal the cards 
    for player in players:
        assignHand(player,deck, 13)
        makeSortedHand(player)

    window = setup()
    player0Hand = players[0].getHand()
    clickZone = slotForCardOnHand(window, player0Hand)


    Tie = False
    roundCount = 1
    #The game continues as long as no one reaches a score of 100. If a player
    #reaches 100 points but there is a tie for the lowest score, play continues
    while (players[0].getScore() < 20 and players[1].getScore() < 20 \
        and players[2].getScore() < 20 and players[3].getScore() < 20) or Tie:

        print("You: ", players[0].getHand())
        print("-----------")
        print("Bot 1: ", players[1].getHand())
        print("-----------")
        print("Bot 2: ", players[2].getHand())
        print("-----------")
        print("Bot 3: ", players[3].getHand())
        print("-----------")
        
        roundCount = roundCount % 4

        displayTextChooseCard(window, roundCount, False)
        
        cardSwap(players,roundCount, clickZone, window)
        giveSwaps(players,roundCount)
        
        displayTextChooseCard(window, roundCount, True)
        
        player0Hand = players[0].getHand()

        clickZone = slotForCardOnHand(window, player0Hand)

        index2ofClubs = find2OfClubs(players)
        #Updates the players and determines who will lead the next trick,
        #as well as whether hearts have been broken yet or not
        players, indexOfNextPlayer, isHeartPlayed, clickZone = \
                 turn(players, index2ofClubs, True, \
                      False, window, clickZone)
        
        if index2ofClubs == 0:
            player0Hand = players[0].getHand()
            clickZone = slotForCardOnHand(window, player0Hand)

        print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x Turn Ended -x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")
        while players[0].getHand() != [[],[],[],[]]:
            players, indexOfNextPlayer, isHeartPlayed, clickZone = \
                     turn(players, indexOfNextPlayer, False, \
                          isHeartPlayed, window, clickZone)
            
            updateScore(players[indexOfNextPlayer])
            players[indexOfNextPlayer].clearGraveyard()
            playerScore = players[indexOfNextPlayer].getScore()
            
            score(window, playerScore, indexOfNextPlayer, False)
            
            
            
            print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x Turn Ended -x-x-x-x-x-x-x-x-x-x-x-x-x-x--x")

        scores = []
        for player in players:
            scores.append(player.getScore())
        #generate new deck
        deck = createDeck()

        players = generatePlayers()

        #give new hands
        for player in players:
            assignHand(player,deck, 13)
            makeSortedHand(player)
            player.setScore(scores[players.index(player)])

        #new round
        roundCount += 1

        #determining if there is a tie at end of round
        winningPlayerIndex = 0
        lowestScore = 20
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
        else:
            Tie = False
       
        player0Hand = players[0].getHand()
        clickZone = slotForCardOnHand(window, player0Hand)
    winner = ''
    if winningPlayerIndex == 0:
        winner = "You win!"
    else:
        winner = "Bot " + str(winningPlayerIndex) + " wins!"
    print("Game Over!", winner)

if __name__ == "__main__":
    main()

