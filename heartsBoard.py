from graphics import *

def drawScoreBoxes(window):
    
    playerBoarderColor = color_rgb(66, 28, 82)
    
    player0 = Polygon(Point(705, 360), Point(775, 360),
                      Point(775, 400), Point(705, 400))
                      
    bot1 = Polygon(Point(780, 145), Point(850, 145),
                   Point(850, 185), Point(780, 185))
                   
    bot2 = Polygon(Point(215, 40), Point(285, 40),
                      Point(285, 80), Point(215, 80))
                      
    bot3 = Polygon(Point(50, 255), Point(120, 255),
                    Point(120, 295), Point(50, 295))

    player0.setOutline(playerBoarderColor)
    bot1.setOutline(playerBoarderColor)
    bot2.setOutline(playerBoarderColor)
    bot3.setOutline(playerBoarderColor)
    
    player0.draw(window)
    bot1.draw(window)
    bot2.draw(window)
    bot3.draw(window)
    
    #------------------type the nameeeee-----------------
    
    nameColor = color_rgb(255, 255, 255)
    
    youCoor = Point(740, 415)
    bot1Coor = Point(815, 200)
    bot2Coor = Point(250, 95)
    bot3Coor = Point(85, 310)
    
    You = Text(youCoor, 'You')
    nameBot1 = Text(bot1Coor, 'Bot 1')
    nameBot2 = Text(bot2Coor, 'Bot 2')
    nameBot3 = Text(bot3Coor, 'Bot 3')
        
    You.setTextColor(nameColor)
    nameBot1.setTextColor(nameColor)
    nameBot2.setTextColor(nameColor)
    nameBot3.setTextColor(nameColor)
        
    You.setSize(20)
    nameBot1.setSize(20)
    nameBot2.setSize(20)
    nameBot3.setSize(20)
        
#    You.setStyle('bold')
#    nameBot1.setStyle('bold')
#    nameBot2.setStyle('bold')
#    nameBot3.setStyle('bold')

    You.draw(window)
    nameBot1.draw(window)
    nameBot2.draw(window)
    nameBot3.draw(window)


def drawSlotForCardsOnBoard(window, setup, cardsOnBoard, cardPlayed):
   
    if setup:
        #reset background
        backgroundColor = color_rgb(0, 102, 35)
        
        backgroundPoly = Polygon(Point(200, 185),
                                 Point(690, 185),
                                 Point(690, 340),
                                 Point(200, 340))
        backgroundPoly.setOutline(backgroundColor)
        backgroundPoly.setFill(backgroundColor)
        backgroundPoly.draw(window)


        slotForCardBoarderColor = color_rgb(66, 28, 82)

        slot1 = Polygon(Point(220, 195), Point(320, 195),
                          Point(320, 335), Point(220, 335))

        slot2 = Polygon(Point(340, 195), Point(440, 195),
                           Point(440, 335), Point(340, 335))

        slot3 = Polygon(Point(460, 195), Point(560, 195),
                            Point(560, 335), Point(460, 335))
                    
        slot4 = Polygon(Point(580, 195), Point(680, 195),
                            Point(680, 335), Point(580, 335))

        slot1.setOutline(slotForCardBoarderColor)
        slot2.setOutline(slotForCardBoarderColor)
        slot3.setOutline(slotForCardBoarderColor)
        slot4.setOutline(slotForCardBoarderColor)
       
        if cardPlayed:
            slots = [slot1, slot2, slot3, slot4]
            
            if cardsOnBoard != ['no card yet']:
                for i in range(len(cardsOnBoard)):
                    slots[i].setFill('white')


        slot1.draw(window)
        slot2.draw(window)
        slot3.draw(window)
        slot4.draw(window)

    else:
        if cardsOnBoard != ['no card yet']:
            # draw boarder
            drawSlotForCardsOnBoard(window, True, cardsOnBoard, True)
            
            #put value in it
            valueOfCard = []
            suitOfCard = []
            nameColor = color_rgb(0, 0, 0)
            valueCoorX = 220 + 12
            valueCoorY = 195 + 17
            suitCoorX = 220 + 27
            suitCoorY = 195 + 17
        
            for card in cardsOnBoard:
                valueOfCard.append(card[0])
                suitOfCard.append(card[1])

            for value in valueOfCard:
                nameV = Text(Point(valueCoorX, valueCoorY), value)
                nameV.setTextColor(nameColor)
                nameV.setSize(13)
                nameV.draw(window)
                nameV.setStyle("bold")
                valueCoorX += 120
        
            for suit in suitOfCard:
                nameS = Text(Point(suitCoorX, suitCoorY), suit[0].upper())
                nameS.setTextColor(nameColor)
                nameS.setSize(13)
                nameS.draw(window)
                nameS.setStyle("bold")
                suitCoorX += 120








# All the functions are defined.  Now start doing stuff.
def slotForCardOnHand(window, turnHand):
    #_______set background_________

    backgroundColor = color_rgb(0, 102, 35)
    
    backgroundPoly = Polygon(Point(0, 429),
                             Point(899, 429),
                             Point(899, 499),
                             Point(0,499))
    backgroundPoly.setOutline(backgroundColor)
    backgroundPoly.setFill(backgroundColor)
    backgroundPoly.draw(window)

    #______draw card boarder______
    slotForCardBoarderColor = color_rgb(66, 28, 82)
    
    #put all cards on hand in one list
    hand = turnHand[0] + turnHand[1] + turnHand[2] + turnHand[3]

    if len(hand) != 0:
        amountHand = len(hand)
        amountOfHalfCard = len(hand) - 1
        amountFrom13 = 13 - len(hand)
        
        slotOfCard = []
        firstCornerX, firstCornerY = 100 + 25 * (amountFrom13) , 429
        secondCornerX, secondCornerY = firstCornerX + 50, 499
        
        rememberFirstCornerX = firstCornerX
        
        
        
        for i in range(amountOfHalfCard):
        
            cardShow = Polygon(Point(firstCornerX, firstCornerY),
                               Point(secondCornerX, firstCornerY),
                               Point(secondCornerX, secondCornerY),
                               Point(firstCornerX, secondCornerY))
                               
            slotOfCard.append(cardShow)
            
            firstCornerX += 50
            secondCornerX = firstCornerX + 50

        lastCardShow = Polygon(Point(firstCornerX, firstCornerY),
                               Point(secondCornerX + 50, firstCornerY),
                               Point(secondCornerX + 50, secondCornerY),
                               Point(firstCornerX, secondCornerY))
                               
        slotOfCard.append(lastCardShow)


        for card in slotOfCard:
            card.setFill("white")
            card.setOutline(slotForCardBoarderColor)
            card.draw(window)

    #--------------------- putting values on cards -----------------------
        valueOfCard = []
        suitOfCard = []
        nameColor = color_rgb(0, 0, 0)
        valueCoorX = rememberFirstCornerX + 12
        valueCoorY = firstCornerY + 17
        suitCoorX = rememberFirstCornerX + 27
        suitCoorY = firstCornerY + 17

        for card in hand:
            valueOfCard.append(card[0])
            suitOfCard.append(card[1])

        for value in valueOfCard:
            nameV = Text(Point(valueCoorX, valueCoorY), value)
            nameV.setTextColor(nameColor)
            nameV.setSize(13)
            nameV.draw(window)
            nameV.setStyle("bold")
            valueCoorX += 50

        for suit in suitOfCard:
            nameS = Text(Point(suitCoorX, suitCoorY), suit[0].upper())
            nameS.setTextColor(nameColor)
            nameS.setSize(13)
            nameS.draw(window)
            nameS.setStyle("bold")
            suitCoorX += 50

        return slotOfCard


def selectCard(slotOfCard, window):
    click = window.getMouse()
    for card in slotOfCard:
        x1 = card.getPoints()[0].getX()
        x2 = card.getPoints()[1].getX()
        y1 = card.getPoints()[0].getY()
        y2 = card.getPoints()[2].getY()
        if click.getX() > x1 and click.getX() < x2 and \
           click.getY() > y1 and click.getY() < y2:
            return slotOfCard.index(card)
    return selectCard(slotOfCard, window)

def getCardName(cardClickIndex, hand):
    '''given the index of the card that was clicked on in the window, returns
    that card'''
    values = []
    suits = []
    hand = hand[0] + hand[1] + hand[2] + hand[3]
    for card in hand:
        values.append(card[0])
        suits.append(card[1])
    value = values[cardClickIndex]
    suit = suits[cardClickIndex]
    for card in hand:
        if card[0] == value and card[1] == suit:
            return card
            
        
    
    






def score(window, score, numPlayer, setup):

    scoreColor = color_rgb(255, 255, 255)
 
 
    player0 = Polygon(Point(705, 360), Point(775, 360),
                   Point(775, 400), Point(705, 400))
     
    bot1 = Polygon(Point(780, 145), Point(850, 145),
                    Point(850, 185), Point(780, 185))
         
    bot2 = Polygon(Point(215, 40), Point(285, 40),
                    Point(285, 80), Point(215, 80))
                        
    bot3 = Polygon(Point(50, 255), Point(120, 255),
                    Point(120, 295), Point(50, 295))

 
    score1Coor = Point(740, 380)
    score2Coor = Point(815, 165)
    score3Coor = Point(250, 60)
    score4Coor = Point(85, 275)

    
    if setup:
    
        score1 = Text(score1Coor, '0')
        score2 = Text(score2Coor, '0')
        score3 = Text(score3Coor, '0')
        score4 = Text(score4Coor, '0')
        
        score1.setTextColor(scoreColor)
        score2.setTextColor(scoreColor)
        score3.setTextColor(scoreColor)
        score4.setTextColor(scoreColor)
        
        score1.setSize(28)
        score2.setSize(28)
        score3.setSize(28)
        score4.setSize(28)
        
        score1.setStyle('bold')
        score2.setStyle('bold')
        score3.setStyle('bold')
        score4.setStyle('bold')
        
        score1.draw(window)
        score2.draw(window)
        score3.draw(window)
        score4.draw(window)

    else:

        scoreCoorIndex = [score1Coor, score2Coor, score3Coor, score4Coor]
        playerCoorIndex = [player0, bot1, bot2, bot3]
        backgroundColor = color_rgb(0, 102, 35)
        playerBoarderColor = color_rgb(66, 28, 82)
        
        playerCoorIndex[numPlayer].setOutline(playerBoarderColor)
        playerCoorIndex[numPlayer].setFill(backgroundColor)
        playerCoorIndex[numPlayer].draw(window)

        setScoreCoor = scoreCoorIndex[numPlayer]
        setScore = Text(setScoreCoor, str(score))
        setScore.setSize(28)
        setScore.setStyle('bold')
        setScore.setTextColor(scoreColor)
        setScore.draw(window)


def setup():

    windowWidth = 900
    windowHeight  = 500
    window = GraphWin('Hearts Board', windowWidth, windowHeight)
    backgroundColor = color_rgb(0, 102, 35)
    window.setBackground(backgroundColor)
    
    score(window, True, True, True)

    drawScoreBoxes(window)
    drawSlotForCardsOnBoard(window, True, None, False)
        
    return window


def main():
    # Open the window
    windowWidth = 900
    windowHeight  = 500
    window = GraphWin('Hearts Board', windowWidth, windowHeight)
    backgroundColor = color_rgb(0, 102, 35)
    window.setBackground(backgroundColor)
    

    # Draw some things
    #drawSomeCircles(window, 100)
    #sayHello(window, 100, windowHeight - 100)
    #sayHelloAgain(window, windowWidth - 250, windowHeight - 100)
    turnHand = [[['10', 'hearts'],['A', 'hearts']], [['4', 'clubs'], ['9', 'clubs'], ['10', 'clubs'], ['A', 'clubs']], [['9', 'diamonds']], [['2', 'spades'], ['4', 'spades'], ['7', 'spades'], ['8', 'spades'], ['J', 'spades'], ['A', 'spades']]]
    drawScoreBoxes(window)
    drawSlotForCardsOnBoard(window, True, [['10', 'hearts']], False)
    s = input('Hit Enter to quit')
    drawSlotForCardsOnBoard(window, False, [['10', 'hearts']], False)
    s = input('Hit Enter to quit')
    drawSlotForCardsOnBoard(window, False, [['10', 'hearts'],['A', 'hearts']], False)
    s = input('Hit Enter to quit')
    drawSlotForCardsOnBoard(window, False, [['10', 'hearts'],['A', 'hearts'], ['K', 'hearts']], False)
    s = input('Hit Enter to quit')
    drawSlotForCardsOnBoard(window, False, [['10', 'hearts'],['A', 'hearts'], ['K', 'hearts'], ['4', 'spade']], False)
    score(window, True, True, True)

    s = input('Hit Enter to quit')
    turnHand = [[], [['4', 'clubs'], ['9', 'clubs'], ['10', 'clubs'], ['A', 'clubs']], [['9', 'diamonds']], [['2', 'spades'], ['8', 'spades'], ['J', 'spades'], ['A', 'spades']]]
    cardIndex = selectCard(slotForCardOnHand(window, turnHand), window)
    print(getCardName(cardIndex, turnHand))
    # Wait for user input.
    s = input('Hit Enter to quit')
    

if __name__ == "__main__":
    main()
