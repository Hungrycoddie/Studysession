import random

def shuffle_cards(cards):
    random.shuffle(cards)
    return cards

def main():
    cards = [i for i in range(1,53)]
    print(shuffle_cards(cards))

if __name__ == '__main__':
    main()