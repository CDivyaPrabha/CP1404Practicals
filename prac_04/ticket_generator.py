import random
numbers = []
flag = 0
picks = input("How many quick picks do you wish to generate? ")
numbers[0] = random.randint(1, 46)
for i in range(1, int(picks) + 1):
    for x in range(5):
        while flag == 0:
            this_no = random.randint(1, 46)
            if this_no in numbers:
                flag = 0
            else:
                flag = 1
        numbers = numbers.append(this_no)
        flag = 0
    numbers.sort()
    print(numbers)
    numbers = []


