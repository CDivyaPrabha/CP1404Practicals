x = input('Enter first number: ')
y = input('Enter second number: ')
print('Menu:\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y')
print('3. Show the squares from x to y\n4. Exit the program')
choice = input('Enter the number of your choice: ')
while not choice == 4:
    if choice == 1:
        for i in range (x, y+1, 1):
            if i % 2 == 0:
                print(i)
    elif choice == 2:
        for i in range (x, y+1, 1):
            if i % 2 == 1:
                print(i)
    elif choice == 3:
        for i in range (x, y+1, 1):
            print(i * i)
    else:
        print('Invalid choice')
    print('Menu:\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y')
    print('3. Show the squares from x to y\n4. Exit the program')
    choice = input('Enter the number of your choice: ')
print('Finished')






