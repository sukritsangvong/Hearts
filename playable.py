from heartCard import *
from roundFunction import *
from botPickCard import *

# might make this function to make code look a bit shorter later
def askForCard(handWithSameSuit, playCard, suitOfPlayCard, suitOrNot):

    for checkCard in handWithSameSuit:
        
        if suitOrNot:
            if checkCard[1][0] == suitOfPlayCard and checkCard[0] == playCard:
                checkPlayCard = "match"
                chosenCard = checkCard
                return chosenCard, checkPlayCard
        
        else:
            if checkCard[0] == playCard:
                checkPlayCard = "match"
                chosenCard = checkCard
                return chosenCard, checkPlayCard

    checkPlayCard = "not match"
    chosenCard = ''
    return chosenCard, checkPlayCard
    


def playable(players, numPlayer, identifyCard):
    #players = list of class of players
    #numPlayer = # of player that is currently playing (int)
    #identifyCard = card that the first player plays (list) ex. ['9', 'clubs']

#    print(players[numPlayer].getHand()[1][1][0])

    turnHand = players[numPlayer].getHand()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #for testing before having organized list
    #turnHand = [[['8', 'hearts'],['9', 'hearts']],[['2', 'clubs'],['5', 'clubs'],['10', 'clubs'],['J', 'clubs']],[['4', 'diamonds'], ['K', 'diamonds']], []]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    noMatchingSuit = False
    identifysuit = ''
    
    if identifyCard == 'no card yet':
        handWithSameSuit = turnHand[0] + turnHand[1] + turnHand[2] + turnHand[3]
        noMatchingSuit = True
    
    else:
        identifysuit = identifyCard[1]
    
    #identify which suit can be played
    if identifysuit == "hearts":
        handWithSameSuit = turnHand[0]

    if identifysuit == "clubs":
        handWithSameSuit = turnHand[1]

    if identifysuit == "diamonds":
        handWithSameSuit = turnHand[2]
    
    if identifysuit == "spades":
        handWithSameSuit = turnHand[3]

    
    #if no cards on hand match the suit on the board
    if handWithSameSuit == []:
            for listOfSuits in turnHand:
                if listOfSuits != []:
                    handWithSameSuit = handWithSameSuit + listOfSuits

                    noMatchingSuit = True




#--------------------------------choose card to play part----------------------------
    if numPlayer == 0:
        
        print("---------------------------------------------------\n")
        print("Your Score: ", players[numPlayer].getScore(), '\n')
        print("---------------------------------------------------\n")
        print("Your hand: ", turnHand, '\n')
        print("---------------------------------------------------\n")
        print("The card(s) that you can play: ",handWithSameSuit, '\n')
        print("---------------------------------------------------\n")
        
        checkPlayCard = "not match"

        chosenCard = ''

        while checkPlayCard != "match":
            
            if noMatchingSuit:
                suitOfPlayCard = ''
                while not suitOfPlayCard in [ 'h', 'c', 'd', 's']:
                    suitOfPlayCard = str(input("Type in the first letter(h,c,d,s) of suit that you want to play: "))

                playCard = ''
                while not playCard in [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                    playCard = str(input("Type in the number(or J, Q, K) of card that you want to play: "))
            
                chosenCard, checkPlayCard = askForCard(handWithSameSuit, playCard, suitOfPlayCard, True)
                if checkPlayCard != "match":
                    print("Found no matched card \nTry Again!")


            else:
                
                playCard = ''
                while not playCard in [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                    playCard = str(input("Type in the number(or J, Q, K) of card that you want to play: "))
                
                chosenCard, checkPlayCard = askForCard(handWithSameSuit, playCard, identifysuit, False)
                if checkPlayCard != "match":
                    print("Found no matched card \nTry Again!")
    

    else:
        chosenCard = botPickCard(handWithSameSuit, noMatchingSuit, turnHand)


    #remove played card from hand
    count = 0
    for listOfSuits in turnHand:
        if chosenCard in listOfSuits:
            listOfSuits.remove(chosenCard)



    return chosenCard, turnHand, numPlayer





def main():
#--------------------------------------------------------------from heartCard.py
    #generate deck
    deck = createDeck()

    #generate players
    players = generatePlayers()
    
        
    #hand out the starting cards --> mutate the list of cards
    for i in range(4):
        assignHand(players[i],deck, 13)
        makeSortedHand(players[i])
#--------------------------------------------------------------from heartCard.py
    #test
    print(playable(players, 1, ['8', 'hearts']))


if __name__ == "__main__":
    main()
