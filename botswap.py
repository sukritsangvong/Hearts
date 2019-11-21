#botSwap.py
#bot decision network for picking cards to swap @ beginning of round
#add

from roundFunction import *
from heartCard import *

def orderHand(hand):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    handOrderedByValue = []
    while len(hand) > 0:
        maxVal = 0
        maxCard = []
        for card in hand:
            if values.index(card[0]) >= maxVal:
                maxVal, maxCard = values.index(card[0]), card
        handOrderedByValue.append(maxCard)
        hand.remove(maxCard)
    return handOrderedByValue

def botSwap(hand):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    hearts, clubs, diamonds, spades = [],[],[],[]
    swapList = []
    
    for card in hand:
        if card[1] == 'hearts':
            hearts.append(card)
        if card[1] == 'clubs':
            clubs.append(card)
        if card[1] == 'diamonds':
            diamonds.append(card)
        if card[1] == 'spades':
            spades.append(card)
            
    for suit in [hearts, clubs, diamonds, spades]:
        #The bot will get rid of whole suits if it can
        if len(suit) == 3 and ['2', 'clubs'] not in suit:
            return suit
        elif len(suit) < 3:
            suitIndex = 0
            while len(swapList) + len(suit) < 3 and len(suit) > suitIndex:
                if suit[suitIndex] != ['2', 'clubs']:
                    swapList.append(suit[suitIndex])
                suitIndex += 1
                    
    if ['Q', 'spades'] in spades and len(swapList) < 3:
            swapList.append(['Q', 'spades'])
            spades.remove(['Q', 'spades'])
    if ['A', 'spades'] in spades and len(swapList) < 3:
            swapList.append(['A', 'spades'])
            spades.remove(['A', 'spades'])
    if ['K', 'spades'] in spades and len(swapList) < 3:
            swapList.append(['K', 'spades'])
            spades.remove(['K', 'spades'])

    for card in hearts:
        if values.index(card[0]) > 5 and card not in swapList \
            and len(swapList) < 3:
                swapList.append(card)

    orderedHand = orderHand(hand)
    for card in orderedHand:
        handIndex = 0
        while len(swapList) < 3:
          swapList.append(orderedHand[handIndex])
          handIndex += 1
          
    return swapList

def main():
    players = generatePlayers()
    deck = createDeck()
    for player in players:
        assignHand(player, deck, 13)
        makeSortedHand(player)
    hand = players[1].getHand()
    hand = hand[0] + hand[1] + hand[2] + hand[3]
    print(hand)
    print("------------")
    print(botSwap(hand))
    

if __name__ == "__main__":
    main()



        
