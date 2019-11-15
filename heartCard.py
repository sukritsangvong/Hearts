import random

from heartCard import *
from playable import *
from takeCardFromBoard import *


def generatePlayers():
    players = []
    for i in range(4):
        players.append(player())
    return players
        
    
class player:

    def __init__(self):
        self.hand = []
        self.graveyard = []
        self.score = 0

    def setHand(self, hand):
        self.hand = hand
    
    def getHand(self):
        return self.hand

    def addToHand(self, card):
        self.hand.append(card)

    def addScore(self, score):
        self.score =+ score

    def getScore(self):
        return self.score

    def getGraveyard(self):
        return self.graveyard

    def addGraveyard(self, listOfCollecetedCards):
        self.graveyard += listOfCollecetedCards
        return self.graveyard

    def removeHand2Clubs(self):
        self.getHand()[1].remove(['2', 'clubs'])
    

def createDeck():
 
    #create a deck
    deck = []
    for suits in ['clubs', "diamonds", "hearts", "spades"]:
        for num in ['2', '3','4', '5', '6', '7', '8', '9','10',\
                   'J', 'Q', 'K', 'A']:
            cardAdded = [num, suits]
            #cardAdded = ' '.join(cardAdded)
            deck.append(cardAdded)

    return deck


#This should be a player method
def assignHand(self, deck, numberofCards):

    currentHand = self.getHand()
    
    
    for individualHands in range(numberofCards):
        
        #random one card at a time
        card = random.choice(deck)

        #remove chosen card from the deck
        '''for identical in deck:
            if identical == card:
                deck.remove(identical)'''
        deck.remove(card)

        #add cards to hand
        currentHand.append(card)
        
    return currentHand

      
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
    for i in range(4):
        assignHand(players[i],deck, 13)
    
    '''#listHearts = []
    #listClubs = []
    #listSpades = []
    #listDiamonds = []
    #for eachCard in p1.getHand():

        #if eachCard[5:] == 'hearts':
            #listHearts.append(eachCard)

        if eachCard[5:] == 'clubs':
            listClubs.append(eachCard)

        if eachCard[5:] == 'spades':
            listSpades.append(eachCard)

        if eachCard[5:] == 'diamonds':
            listDiamonds.append(eachCard)

    print(listHearts)'''

    

    
    print("Player 1 : ", players[0].getHand())
    print("-----------")
    print("Player 2 : ", players[1].getHand())
    print("-----------")
    print("Player 3 : ", players[2].getHand())
    print("-----------")
    print("Player 4 : ", players[3].getHand())
    print("-----------")
    print("list of deck:", deck)

def test():

    #--------------------------------------------------------------from heartCard.py
    deck = createDeck()
    players = generatePlayers()
    for player in players:
        assignHand(player,deck, 13)
        makeSortedHand(player)
#--------------------------------------------------------------from heartCard.py
    set = [[['5', 'hearts'], ['J', 'hearts']], [['2', 'clubs'], ['5', 'clubs'], ['9', 'clubs']], [['2', 'diamonds'], ['4', 'diamonds'], ['K', 'diamonds'], ['A', 'diamonds']], [['3', 'spades'], ['7', 'spades'], ['9', 'spades'], ['Q', 'spades']]]
    players[0].setHand(set)
    print("Player 1 : ", players[0].removeHand2Clubs())
    print("Player 1 : ", players[0].getHand())

if __name__ == "__main__":
    test()

