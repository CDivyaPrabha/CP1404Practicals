def main():
    """Divya Prabha Chandrasekaran"""
    name = get_name()
    number = int(input('Enter a number: '))
    print_letters(name, number)


def print_letters(name, number):
    for i in range(number-1, len(name), number):
        print(name[i])


def get_name():
    flag = 0
    while flag == 0:
        name = input("Enter your name: ")
        for char in name:
            if char.isupper() or char.islower():
                flag = 1
                break
        if flag == 0:
            print("Incorrect input")
    return name


main()