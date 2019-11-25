import random

from heartCard import *
from playable import *
from takeCardFromBoard import *


def generatePlayers():
    '''Makes a list containing the 4 player objects.'''
    players = []
    for i in range(4):
        players.append(player())
    return players
        
    
class player:
    '''An object that has a hand, a score, and a graveyard. Can be controlled
    by either a human or by code.'''
    def __init__(self):
        self.hand = []
        self.graveyard = []
        self.score = 0
        self.swaps = []

    def setHand(self, hand):
        self.hand = hand
    
    def getHand(self):
        return self.hand

    def appendHand(self,card):
        self.hand.append(card)

    def setSwaps(self,swapList):
        for swap in swapList:
            self.swaps.append(swap)
    def getSwaps(self):
        return self.swaps

    def addScore(self, score):
        self.score += score

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def getGraveyard(self):
        return self.graveyard

    def addGraveyard(self, listOfCollecetedCards):
        self.graveyard += listOfCollecetedCards
        return self.graveyard

    def clearGraveyard(self):
        self.graveyard = []

    def removeHand2Clubs(self):
        self.getHand()[1].remove(['2', 'clubs'])
    

def createDeck():
    '''Creates a standard deck of 52 cards. Aces are high.'''
    deck = []
    for suits in ["clubs", "diamonds", "hearts", "spades"]:
        for num in ['2', '3','4', '5', '6', '7', '8', '9','10',\
                   'J', 'Q', 'K', 'A']:
            cardAdded = [num, suits]
            deck.append(cardAdded)

    return deck

def assignHand(player, deck, numberofCards):
    '''Deals a random hand of cards to the player.'''
    currentHand = player.getHand()
    
    for cards in range(numberofCards):

        #random one card at a time
        card = random.choice(deck)

        #remove chosen card from the deck
        deck.remove(card)

        #add card to hand
        currentHand.append(card)
        
    #return currentHand
    player.setHand(currentHand)
    return player

      
