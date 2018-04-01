"""Divya Prabha Chandrasekaran"""
flag = 0
while flag == 0:
    name = input("Enter your name: ")
    for char in name:
        if char.isupper() or char.islower():
            flag = 1
            break
    if flag == 0:
        print("Incorrect input")
print(name[0:len(name):2])