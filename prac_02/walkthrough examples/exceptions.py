"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError occurs when a number does not match its input variable type.
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError occurs when we attempt to divide a number by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes. We could not allow the user to enter zero as the denominator by not processing the code if zero is entered.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if not denominator == 0:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")