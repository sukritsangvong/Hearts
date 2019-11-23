from heartCard import *
from roundFunction import *
import random

'''if you have no card lower than the card of matching suit that has been played, should you just
play the highest card of that suit that you have?'''
def botPickCard(handWithSameSuit, noMatchingSuit, turnHand, identifyCard, firstTurn, isHeartPlayed, listOfBoard):
    chosenCard = ''
        
    if noMatchingSuit: #not going to take the cards on the board

        #see which suit has the least amount of card left
        leastAmount = 13
        leastSuit = ['Suit with the least amount of card']
        if isHeartPlayed:
            for i in range(4):
                if len(turnHand[i]) != 0 and len(turnHand[i]) < leastAmount:
                    leastAmount = len(turnHand[i])
                    leastSuit[0] = turnHand[i][0][1]
        else:
            for i in [1,2,3]:
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
                    if card in handWithSameSuit and card[0] != '10' and card[0] < '6':
                        return card

            if randomint != 0:
                for suit in turnHand[:randomint + 1]:
                    for card in suit:
                        if card[0] < '6' and card[0] != '10' and card in handWithSameSuit:
                            return card
            
            for suit in turnHand[randomint:4]:
                for card in suit:
                    if card != []:
                        return card

            if randomint != 0:
                for suit in turnHand[:randomint]:
                    for card in suit:
                        if card != []:
                            return card

            #else:
                #fix playing high cards problem
        #reverse to descending order
        handWithSameSuit.reverse()

        for card in (handWithSameSuit):
            
            #try to give out score!
            #if have Q of spades, K of spades, or A of spades, play it
            if not firstTurn: #don't want to fire score in the first turn
                if card[1] == 'spades':
                    if card[1] == 'Q':
                        handWithSameSuit.reverse()
                        return card
                    elif card[1] == 'K' or card[1] == 'A':
                        handWithSameSuit.reverse()
                        return card
                
                #if have high hearts
                if card[1] == 'hearts':
                    if card[1] > '5' or card[1] == '10':
                        handWithSameSuit.reverse()
                        return card

            #still want to discard K and A even if it is a first Turn
                if card[1] == 'K' or card[1] == 'A':
                    handWithSameSuit.reverse()
                    return card
        
        if isHeartPlayed:
            for i in range(4):
                if len(turnHand[i]) == 1: 
                    handWithSameSuit.reverse()
                    return turnHand[i][0] #if have only 1 card of any suits left, play it if it is a low card

        else: # if heart is not played then player is not allowed to play heart or Qof spades
            for i in [1, 2, 3]:
                if len(turnHand[i]) == 1 and turnHand[i][0] != ['Q', 'spades']: #if have only 1 card of any suits left, play it
                    handWithSameSuit.reverse()
                    return turnHand[i][0]
        
        #play suit that has the least amount of cards
        for card in (handWithSameSuit):
            
            if card[1] == leastSuit[0]:
                handWithSameSuit.reverse()
                return card
        
    else:
        
        #choose the highest card on the hand that is lower than card on the board
        handWithSameSuit.reverse()
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        #find the highiest value of card on board
        highestOnBoard = listOfBoard[0][0]
        for cardOnBoard in listOfBoard:
            if values.index(highestOnBoard) < values.index(cardOnBoard[0]) and cardOnBoard[1] == listOfBoard[0][1]:
                highestOnBoard = cardOnBoard[0]
            
        for card in handWithSameSuit: #checking from the descending order
            if values.index(card[0]) < values.index(highestOnBoard):
                handWithSameSuit.reverse()
                return card

        #reverse back to ascending order
        handWithSameSuit.reverse()
        #if no card on hand is lower than card on the board
        #play the smallest number card
        #Maybe play the largest card IF you are only a certain number of turns in?
        for card in handWithSameSuit:
            return card


