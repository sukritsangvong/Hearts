from graphics import *
import time

def drawScoreBoxe(window):
    




def main():
    # Open the window
    windowWidth = 900
    windowHeight  = 500
    window = GraphWin('Score Board', windowWidth, windowHeight)
    backgroundColor = color_rgb(169, 169, 169)
    window.setBackground(backgroundColor)
    

    drawScoreBoxes(window)
    drawSlotForCardsOnBoard(window, True, [['10', 'hearts']], False)
    s = input('Hit Enter to quit')
#    drawSlotForCardsOnBoard(window, False, [['10', 'hearts']], False)
#    s = input('Hit Enter to quit')
#    drawSlotForCardsOnBoard(window, False, [['10', 'hearts'],['A', 'hearts']], False)
#    s = input('Hit Enter to quit')
#    drawSlotForCardsOnBoard(window, False, [['10', 'hearts'],['A', 'hearts'], ['K', 'hearts']], False)
#    s = input('Hit Enter to quit')
#    drawSlotForCardsOnBoard(window, False, [['10', 'hearts'],['A', 'hearts'], ['K', 'hearts'], ['4', 'spade']], False)
    score(window, True, True, True)
    
    displayTextChooseCard(window, 0)

#    s = input('Hit Enter to quit')
    displayTextChooseCard(window, 1)
    
#    s = input('Hit Enter to quit')
    displayTextChooseCard(window, 2)
            
#    s = input('Hit Enter to quit')
    displayTextChooseCard(window, 3)
                    
#    s = input('Hit Enter to quit')
    turnHand = [[], [['4', 'clubs'], ['9', 'clubs'], ['10', 'clubs'], ['A', 'clubs']], [['9', 'diamonds']], [['2', 'spades'], ['8', 'spades'], ['J', 'spades'], ['A', 'spades']]]
    cardIndex = selectCard(slotForCardOnHand(window, turnHand), window)
    print(getCardName(cardIndex, turnHand))
    # Wait for user input.
    s = input('Hit Enter to quit')
    

if __name__ == "__main__":
    main()
