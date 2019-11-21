#botSwap.py
#bot decision network for picking cards to swap @ beginning of round

from roundFunction import *
from heartCard import *

def swapPick(hand):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    hearts, clubs, diamonds, spades = [],[],[],[]
    for card in hand:
        if card[1] == 'hearts':
            hearts.append(card)
        if card[1] == 'clubs':
            clubs.append(card)
        if card[1] == 'diamonds':
            diamonds.append(card)
        if card[1] == 'spades':
            spades.append(card)
    print(hearts,clubs,diamonds,spades)
    
    if ['Q', 'spades'] in spades:
        return ['Q', 'spades']
    if ['A', 'spades'] in hand:
        return ['A', 'spades']
    if ['K', 'spades'] in hand:
        return ['K', 'spades']
    for card in hearts:
        if values.index(card[0]) > 5:
            return 
    


def botSwap(hand):
    swapList = []
    while len(swapList) <= 3:
        swapList.append(swapPick(hand))
    return swapList

def main():
    players = generatePlayers()
    deck = createDeck()
    for player in players:
        assignHand(player, deck, 13)
        makeSortedHand(player)
    hand = players[1].getHand()
    hand = hand[0] + hand[1] + hand[2] + hand[3]
    print(swapPick(hand))

if __name__ == "__main__":
    main()



        
