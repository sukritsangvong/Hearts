from heartCard import *
from roundFunction import *

def botPickCard(handWithSameSuit, noMatchingSuit, turnHand):

    chosenCard = ''
        
    if noMatchingSuit: #not going to take the cards on the board
        #reverse to descending order
        handWithSameSuit.reverse()
        for card in (handWithSameSuit):
            print('this is cardddd', card)
            
            #if have Q of spades, K of spades, or A of spades, play it
            if card[1] == 'spades':
                if card[1] == 'Q':
                    return card
                elif card[1] == 'K' or card[1] == 'A':
                    return card
            
            #if have high hearts
            if card[1] == 'hearts':
                if card[1] > '5':
                    return card
        
        #see which suit has the least amount of card left
        leastAmount = 13
        leastSuit = ['Suit with the least amount of card']
        for i in range(4):
            if len(turnHand[i]) != 0 and len(turnHand[i]) < leastAmount:
                leastSuit[0] = turnHand[i][0][1]
                print(leastSuit[0],'this is suiitttt')
            if len(turnHand[i]) == 1: #if have only 1 card of any suits left, play it
                return card
            
        #play suit that has the least amount of cards
        for card in (handWithSameSuit):
            print('enter and this is card', card)
            
            if card[1] == leastSuit[0]:
                return card
        
    else:
        #play the smallest number card
        for card in handWithSameSuit:
            return card
                       
