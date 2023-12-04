import re


def get_winning_numbers(card):
    get_winning_numbers = re.search(': (.*) \|', card)
    winning_numbers = get_winning_numbers.group(1).split()
    return winning_numbers


def get_played_numbers(card):
    get_played_numbers = re.search('\| (.*)', card)
    played_numbers = get_played_numbers.group(1).split()
    return played_numbers


def sum_winning_cards(card_pack):
    cards_total = 0

    for card in card_pack:
        winning_numbers_dict = {}
        winning_numbers = get_winning_numbers(card)

        for card_number in winning_numbers:
            winning_numbers_dict[card_number] = True

        played_numbers = get_played_numbers(card)

        winning_cards_counter = 0
        single_card_total = 0

        for number in played_numbers:
            if number in winning_numbers_dict:
                winning_cards_counter += 1

                if winning_cards_counter == 1:
                    single_card_total += 1
                else:
                    single_card_total *= 2

        cards_total += single_card_total

    return cards_total


with open('input.txt', 'r') as input_file:
    card_pack = input_file.read().split('\n')

print(sum_winning_cards(card_pack))

