import re
from collections import Counter
import mathplotlib.pyplot as plt

# Zad 2
def count_letters(text):
    letters = re.findall(r'[a-z]', text, re.I)
    return Counter(letters)

# Zad 3
def calculate_histogram(letters_counter):
    plt.bar(letters_counter.keys(), letters_counter.values())
    plt.show()

# Zad 4
def deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

# Zad 5
def shuffle_deck(deck):
    from random import shuffle
    shuffle(deck)
    return deck

# Zad 6
import random

def deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    suits = ['c', 'd', 'h', 's']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)
    return shuffled_deck

def deal(deck, n):
    random.shuffle(deck)  # Mieszamy talię przed rozdaniem
    hands = []
    cards_per_hand = 5
    for _ in range(n):
        hand = [deck.pop() for _ in range(cards_per_hand)]
        hands.append(hand)
    return hands

# Przykładowe użycie:
deck_of_cards = deck()
shuffled_deck = shuffle_deck(deck_of_cards)
hands = deal(shuffled_deck, 4)  # Rozdaj karty 4 graczom
print(hands)
