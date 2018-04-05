import random


def main():
    picks = input("How many quick picks do you wish to generate? ")
    numbers = []
    for i in range(1, int(picks) + 1):
        numbers = get_unique_list()
        numbers.sort()
        print(numbers)


def get_unique_list():
    numbers = []
    numbers.append(random.randint(1, 46))
    for x in range(5):
        this_no = random.randint(1, 46)
        while this_no in numbers:
            this_no = random.randint(1, 46)
        numbers.append(this_no)
    return numbers


main()
