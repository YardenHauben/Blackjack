import random
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']
hand = []
dealer = []
bust = True
i = 0
total = 0
card = random.choice(deck)
hand.append(card)
deck.remove(card)
card = random.choice(deck)
dealer.append(card)
deck.remove(card)
card = random.choice(deck)
hand.append(card)
deck.remove(card)
card = random.choice(deck)
dealer.append(card)
deck.remove(card)
print("Player: " + str(hand))
if dealer[i] in ['J', 'Q', 'K', 'A']:
    print("Dealer: " + "['" + str(dealer[i]) + "', ?]")
else:
    print("Dealer: " + "[" + str(dealer[i]) + ", ?]")
def calculateTotal(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total
playerTotal = calculateTotal(hand)
move = input('Hit or stand? ')
while move == 'hit':
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    print("Player: " + str(hand))
    playerTotal = calculateTotal(hand)
    if playerTotal < 21:
        move = input('Hit or stand? ')
    elif playerTotal == 21:
        break
    else:
        print('You Bust')
        bust = False
        break
def dealerHand():
    dealerTotal = calculateTotal(dealer)
    while dealerTotal < 17:
        print("Dealer: " + str(dealer))
        card = random.choice(deck)
        dealer.append(card)
        deck.remove(card)
        dealerTotal = calculateTotal(dealer)
    print("Dealer: " + str(dealer))
    if dealerTotal > 21:
        print("Dealer Bust")
    elif dealerTotal == 21 and playerTotal == 2 and len(hand) == 2 and len(dealer) == 2:
        print("Blackjack")
        print("Tie")
    elif playerTotal == 21 and len(hand) == 2:
        print("You Blackjack")
        print("You win")
    elif dealerTotal == 21 and len(dealer) == 2:
        print("Dealer Blackjack")
        print("You lose")
    elif playerTotal == dealerTotal:
        print("Tie")
    elif playerTotal > dealerTotal:
        print("You win")
    elif playerTotal < dealerTotal:
        print("You lose")
if bust:
    dealerHand() 
