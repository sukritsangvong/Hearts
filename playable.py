from heartCard import *

#def askForCard(handWithSameSuit):
#
#    checkPlayCard = "not match"
#    chosenCard = ''
#
#    playCard = str(input("Type in the number(or J, Q, K) of card that you want to play: "))
#    for checkCard in handWithSameSuit:
#        if checkCard[0] == playCard:
#            checkPlayCard = "match"
#            chosenCard = checkCard
#        if checkPlayCard != "match":
#            print("Found no matched card \nTry Again!")
#
#    return chosenCard

def playable(players, numPlayer, identifyCard):
    #players = list of class of players
    #numPlayer = # of player that is currently playing (int)
    #identifyCard = card that the first player plays (list) ex. ['9', 'clubs']

#    print(players[numPlayer].getHand()[1][1][0])

    turnHand = players[numPlayer].getHand()
    identifysuit = identifyCard[1]
    
   
   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #for testing before having organized list
    turnHand = [[['8', 'hearts'],['9', 'hearts']],[['2', 'clubs'],['5', 'clubs'],['10', 'clubs'],['J', 'clubs']],[['4', 'diamonds'], ['K', 'diamonds']], []]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    #identify which suit can be played
    if identifysuit == "hearts":
        handWithSameSuit = turnHand[0]

    if identifysuit == "clubs":
        handWithSameSuit = turnHand[1]

    if identifysuit == "diamonds":
        handWithSameSuit = turnHand[2]
    
    if identifysuit == "spades":
        handWithSameSuit = turnHand[3]


    noMatchingSuit = False

    #if no cards on hand match the suit on the board
    if handWithSameSuit == []:
            for listOfSuits in turnHand:
                if listOfSuits != []:
                    handWithSameSuit = handWithSameSuit + listOfSuits

                    noMatchingSuit = True

    
    print("---------------------------------------------------")
    print("Your hand: ", turnHand)
    print("---------------------------------------------------")
    print("The card(s) that you can play: ",handWithSameSuit)
    print("---------------------------------------------------")

#--------------------------------choose card to play part----------------------------
    checkPlayCard = "not match"

    chosenCard = ''

    while checkPlayCard != "match":
        
        if noMatchingSuit:
            suitOfPlayCard = str(input("Type in the first letter(h,c,d,s) of suit that you want to play: "))


        else:
            playCard = str(input("Type in the number(or J, Q, K) of card that you want to play: "))
            for checkCard in handWithSameSuit:
                if checkCard[0] == playCard:
                    checkPlayCard = "match"
                    chosenCard = checkCard
                if checkPlayCard != "match":
                    print("Found no matched card \nTry Again!")
            


        playCard = str(input("Type in the number(or J, Q, K) of card that you want to play: "))
        for checkCard in handWithSameSuit:
            if checkCard[1][0] == suitOfPlayCard and checkCard[0] == playCard:
                print("entered")
                checkPlayCard = "match"
                chosenCard = checkCard
        if checkPlayCard != "match":
                print("Found no matched card \nTry Again!")


    #remove played card from hand
    count = 0
    for listOfSuits in turnHand:
        if chosenCard in listOfSuits:
            listOfSuits.remove(chosenCard)

    turnHand.remove([]) #the function turnHand somehow has empty list in it, so remove it before returning

    return chosenCard, turnHand





def main():
#--------------------------------------------------------------from heartCard.py
    #generate deck
    deck = createDeck()

    #generate players
    players = generatePlayers()
    
        
    #hand out the starting cards --> mutate the list of cards
    for i in range(4):
        assignHand(players[i],deck, 13)
#--------------------------------------------------------------from heartCard.py
    #test
    print(playable(players, 0, ['9', 'spades']))


if __name__ == "__main__":
    main()
