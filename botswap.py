#botSwap.py
#bot decision network for picking cards to swap @ beginning of round

def swapPick(hand):
    unSuitedHand = hand[0] + hand[1] + hand[2] + hand[3]
    for suit in hand:
        if len(suit) <= 3:
           suit.remove(suit[0])
           return suit[0]
    if ['Q', 'spades'] in hand:
        return ['Q', 'spades']
    if ['A', 'spades'] in hand:
        return ['A', 'spades']
    if ['K', 'spades'] in hand:
        return ['K', 'spades']
    


def botSwap(hand):
    swapList = []
    while len(swapList) <= 3:
        swapPick(hand)
    return swapList


hand = [['Q', 'spades'],['K', 'spades'],['A', 'spades'], ['1', 'spades']]
print(swapPick(hand))

        
