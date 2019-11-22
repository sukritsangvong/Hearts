from heartCard import *
from roundFunction import *
import random

def botPickCard(handWithSameSuit, noMatchingSuit, turnHand, identifyCard):

    chosenCard = ''
        
    if noMatchingSuit: #not going to take the cards on the board

        #see which suit has the least amount of card left
        leastAmount = 13
        leastSuit = ['Suit with the least amount of card']
        for i in range(4):
            if len(turnHand[i]) != 0 and len(turnHand[i]) < leastAmount:
                leastAmount = len(turnHand[i])
                leastSuit[0] = turnHand[i][0][1]

        #to random the suit that bot starts to check
        randomint = random.randint(0, 3)

        if identifyCard == 'no card yet':#if the first player to play
            
            
            #play the small suit that has least number of card
            for card in handWithSameSuit:
                if card[1] == leastSuit[0] and card[0] < '6' and card[0] != '10':
                    return card
        
            #play the small number of card
            for suit in turnHand[randomint:4]:
                for card in suit:
                    if card[0] < '6' and card[0] != '10':
                        return card

            if randomint != 0:
                for suit in turnHand[:randomint]:
                    for card in suit:
                        if card[0] < '6' and card[0] != '10':
                            return card
            
            #play the suit that has least number of card
            for card in handWithSameSuit:
                if card[1] == leastSuit[0]:
                    return card
    
    
        #reverse to descending order
        handWithSameSuit.reverse()

        for card in (handWithSameSuit):
            
            #if have Q of spades, K of spades, or A of spades, play it
            if card[1] == 'spades':
                if card[1] == 'Q':
                    return card
                elif card[1] == 'K' or card[1] == 'A':
                    return card
            
            #if have high hearts
            if card[1] == 'hearts':
                if card[1] > '5' or card[1] == '10':
                    return card
        

        for i in range(4):
            if len(turnHand[i]) == 1: #if have only 1 card of any suits left, play it
                return card
            
        #play suit that has the least amount of cards
        for card in (handWithSameSuit):
            
            if card[1] == leastSuit[0]:
                return card
        
    else:
        #play the smallest number card
        for card in handWithSameSuit:
            return card
                       

