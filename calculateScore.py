def calculateScore(listOfGraveyard):
    pointList = []
    QofSpades = False
    
    for card in listOfGraveyard:
        
        #calculate score
        if card[1] == 'hearts':
            pointList += card
        if card[1] == 'spades' and card[0] == 'Q':
            QofSpades = True

    points = int(len(pointList)/2) #the len of pointList counts 2 points per card
                                    #(len['8', 'hearts']) = 2
    if QofSpades:
        points += 13

    return points





def main():
    print(calculateScore([['8', 'hearts'],['2', 'clubs'],['9', 'hearts'],['5', 'clubs'],['Q', 'spades']]))


if __name__ == "__main__":
    main()

