import random

def generate_deck():
    ranks=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    suits=["diamonds", "hearts", "spades", "clubs"]

    deck = []

    for i in range(4):
        for j in range(13):
            deck.append((ranks[j],suits[i]))

    return random.sample(deck,len(deck))


def sort_hand_by_rank(hand):
    ranks=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for i in range(5):
        for j in range(i+1,5):
            posi=0
            posj=0
            for pos in range(len(ranks)):
                if(ranks[pos]==hand[j][0]):
                    posj=pos
                if(ranks[pos]==hand[i][0]):
                    posi=pos
            if(posi>posj):
                temp=hand[i]
                hand[i]=hand[j]
                hand[j]=temp
    return hand


def isStraight(hand):
    hand=sort_hand_by_rank(hand)
    ranks=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    sign=0
    for i in range(9):
        if(hand[0][0]==ranks[i]):
            sign=1
            for j in range(5):
                if hand[j][0]!=ranks[i+j] and not(j==4 and hand[j-1][0]=="5" and hand[j][0]=="A"):
                    return 0
    return sign


def isFlush(hand):
    suit=hand[0][1]
    for i in range(1,5):
        if suit != hand[i][1]:
            return 0
    return 1


def classify_hand(hand):

    counter = {hand[0][0]:0}

    for i in range(1,5):
        temp = 1
        for j in counter:
            if j == hand[i][0]:
                temp = 0 
        if temp:
            counter[hand[i][0]]=0

    for i in counter:
        for j in range(5):
            if hand[j][0]== i:
                counter[i]+=1

    max=2
    c=0
    for i in counter:
        if counter[i]>=max:
            max=counter[i]
        if counter[i]>1:
            c+=1;


    if(isStraight(hand)):
        if(isFlush(hand)):
            return ("Straight flush")
        else:
            return("Straight")
    else:
        if(isFlush(hand)):
            return("Flush")
        else:
            if(c==0):
                return("High card")

            if(c==1):
                if(max==2):
                    return("One pair")
                if(max==3):
                    return("Three of a kind")
                if(max==4):
                    return("Four of a kind")

            if(c==2):
                if(max==2):
                    return("Two pair")
                if(max==3):
                    return("Full house")
        
samples = 100000


results = {
    "High card": 0,
    "One pair": 0,
    "Two pair": 0,
    "Three of a kind": 0,
    "Straight": 0,
    "Flush": 0,
    "Full house": 0,
    "Four of a kind": 0,
    "Straight flush": 0
}

for x in range(samples):

    deck=generate_deck()
    hand = deck[:5]

    result = classify_hand(hand)
    results[result] += 1

for z in results:
    results[z]/=samples

print("Estimated probabilities:")
for h in results:
    print(h, results[h])







