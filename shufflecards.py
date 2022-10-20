import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(suit, rank))
    
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"
        return s
    
    def shuffle(self):
        rng = random.Random()
        rng.shuffle(self.cards)
    
    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
    def popCard(self):
        return self.cards.pop()
    
    def isEmpty(self):
        return (len(self.cards) == 0)
    
    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.isEmpty():
                break
            card = self.popCard()
            hand = hands[i % num_hands]
            hand.addCard(card)

class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name
    def addCard(self, card):
        self.cards.append(card)
    def __str__(self):
        s = "Hand " + self.name
        if self.isEmpty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):
    def removeMatches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count
class OldMaidGame(CardGame):
    def play(self, names):
        # remove Queen of Clubs
        self.deck.removeCard(Card(0, 12))
          # make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
            # deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.printHands()
        # remove initial matches
        matches = self.removeAllMatches()
        print("---------- Matches discarded, play begins")
        self.printHands()
        # play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.playOneTurn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.printHands()
    def removeAllMatches(self):
        count = 0
        for hand in self.hands:
            count += hand.removeMatches()
        return count
    
    def playOneTurn(self, i):
        if self.hands[i].isEmpty():
            return 0
        neighbor = self.findNeighbor(i)
        pickedCard = self.hands[neighbor].popCard()
        self.hands[i].addCard(pickedCard)
        print("Hand", self.hands[i].name, "picked", pickedCard)
        count = self.hands[i].removeMatches()
        self.hands[i].shuffle()
        return count
    
    def findNeighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].isEmpty():
                return neighbor
            
    def printHands(self):
        for hand in self.hands:
            print(hand)

game = OldMaidGame()
game.play(["Arun", "Aruna", "Mum"])