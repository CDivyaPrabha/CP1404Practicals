numbers = []
print("Enter 5 numbers")
for i in range(0, 5):
    number = input("Number: ")
    numbers.append(number)
first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average = sum(numbers) / len(numbers)
print("The {} number is {}".format("first", str(first_number)))
print("The {} number is {}".format("last", str(last_number)))
print("The {} number is {}".format("smallest", str(smallest_number)))
print("The {} number is {}".format("largest", str(largest_number)))
print("The average of the numbers is {}".format(str(average)))

