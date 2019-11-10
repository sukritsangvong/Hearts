#change face card to number so can measure / compare
def faceToNum(checkFace):

    if checkFace == 'J':
        return '11'
    elif checkFace == 'Q':
        return '12'
    elif checkFace == 'K':
        return '13'
    elif checkFace == 'A':
        return '14'
    else:
        return checkFace



#this function returns an integer of number of player who
#will take the card on the board
#0 = the first player who plays take the card
#1 = the second player who plays tke the card etc..
def takeCardFromBoard(listOfBoard):
    setSuit = listOfBoard[0][1]
    
    highestNum = faceToNum(listOfBoard[0][0])
    returner = 0
    
    count = 1
    for otherCards in (listOfBoard[1:]):
        if otherCards[1] == setSuit and otherCards[0] > highestNum:
            returner = count
        count += 1

    return returner






def main():
    print(takeCardFromBoard([['8', 'hearts'],['2', 'clubs'],['9', 'hearts'],['5', 'clubs']]))

if __name__ == "__main__":
    main()

