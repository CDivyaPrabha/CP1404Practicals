name = input('Enter name: ')
print('(H)ello\n(G)oodbye\n(Q)uit')
choice = input('>>> ')
while not choice == 'Q':
    if choice == 'H':
        print('Hello', name)
    elif choice =='G':
        print('Goodbye', name)
    else:
        print('Invalid message')
    print('(H)ello\n(G)oodbye\n(Q)uit')
    choice = input('>>> ')
print('Finished')



