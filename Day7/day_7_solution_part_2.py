import numpy as np
from collections import Counter

card_value_from_high_to_low = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def custom_sort_key(item):
    return [card_value_from_high_to_low.index(char) for char in item]


def sort_array(hands):
    return sorted(hands, key=custom_sort_key, reverse=True)


def is_five_of_a_kind(counter):
    return len(counter) == 1 or (len(counter) == 2 and 'J' in counter.keys())


def is_four_of_a_kind(counter):
    return (
            len(counter) == 2 and max(counter.values()) == 4
    ) or (
            len(counter) == 3 and counter['J'] == 2
    ) or (
            len(counter) == 3 and 'J' in counter.keys() and max(counter.values()) == 3
    )


def is_full_house(counter):
    return len(counter) == 2 or (
            len(counter) == 3 and 'J' in counter.keys() and max(counter.values()) == 2
    )


def is_three_of_a_kind(counter):
    return (
            len(counter) == 3 and max(counter.values()) == 3
    ) or (
            len(counter) == 4 and 'J' in counter.keys() and max(counter.values()) == 2
    )


def is_two_pair(counter):
    return len(counter) == 3


def is_one_pair(counter):
    return len(counter) == 4 or (
            len(counter) == 5 and 'J' in counter.keys()
    )

def is_high_card(counter):
    return len(counter) == 5 and not 'J' in counter.keys()


with open('input.txt', 'r') as input_file:
    file = input_file.read().split('\n')
    hands = [x.split(' ')[0] for x in file]
    bids = [x.split(' ')[1] for x in file]

    games = []

    hand_types = {
        "five_of_a_kind": [],
        "four_of_a_kind": [],
        "full_house": [],
        "three_of_a_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": [],
    }

    for hand, bid in zip(hands, bids):
        player = {hand: int(bid)}

        games.append(player)
        counter = Counter(hand)

        if is_five_of_a_kind(counter):
            hand_types["five_of_a_kind"].append(hand)
        elif is_four_of_a_kind(counter):
            hand_types["four_of_a_kind"].append(hand)
        elif is_full_house(counter):
            hand_types["full_house"].append(hand)
        elif is_three_of_a_kind(counter):
            hand_types["three_of_a_kind"].append(hand)
        elif is_two_pair(counter):
            hand_types["two_pair"].append(hand)
        elif is_one_pair(counter):
            hand_types["one_pair"].append(hand)
        elif is_high_card(counter):
            hand_types["high_card"].append(hand)

    sorted_hands = {}

    for hand_type, hands in hand_types.items():
        sorted_hands[hand_type] = sort_array(hands)

    new_array = np.concatenate(
        (
            sorted_hands['high_card'],
            sorted_hands['one_pair'],
            sorted_hands['two_pair'],
            sorted_hands['three_of_a_kind'],
            sorted_hands['full_house'],
            sorted_hands['four_of_a_kind'],
            sorted_hands['five_of_a_kind'],
        )
    )

    total_winnings = 0

    for index, card in enumerate(new_array):
        for game in games:
            if card in game:
                card_value = game[card]
                total_winnings += card_value * (index + 1)
                break

    print(total_winnings)
