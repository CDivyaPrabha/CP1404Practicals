#First program
name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()


#Second Program
in_file = open('name.txt', 'r')
name = in_file.read().strip()
print('Your name is', name)
in_file.close()


#Third program
in_file = open('numbers.rtf', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()


#Third program extended
in_file = open('numbers.rtf', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()





