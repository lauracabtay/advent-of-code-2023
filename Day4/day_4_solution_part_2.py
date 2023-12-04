import re


def original_cards_count(card_pack):
    card_count_dict = {}
    for index, card in enumerate(card_pack):
        card_count_dict[index + 1] = 1
    return card_count_dict


def get_winning_numbers(card):
    get_winning_numbers = re.search(': (.*) \|', card)
    winning_numbers = get_winning_numbers.group(1).split()
    return winning_numbers


def get_played_numbers(card):
    get_played_numbers = re.search('\| (.*)', card)
    played_numbers = get_played_numbers.group(1).split()
    return played_numbers


def sum_card_copies_count(card_pack):
    total = 0

    card_count_dict = original_cards_count(card_pack)

    for index, card in enumerate(card_pack):
        counter = 0
        winning_numbers = get_winning_numbers(card)
        played_numbers = get_played_numbers(card)

        for number in played_numbers:
            if number in winning_numbers:
                counter += 1

        for i in range(index + 2, index + 2 + counter):
            if card_count_dict[index + 1] == 1:
                card_count_dict[i] += 1
            else:
                card_count_dict[i] += card_count_dict[index + 1]

    for key, value in card_count_dict.items():
        total += value

    return total


with open('input.txt', 'r') as input_file:
    card_pack = input_file.read().split('\n')

print(sum_card_copies_count(card_pack))
