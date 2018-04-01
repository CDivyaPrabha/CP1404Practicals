import string


def count_letters(word):
    count = 0
    for char in word:
        if char.lower() in string.ascii_lowercase:
            count += 1
    return count


statement = input ("Enter a string: ")
alphabets = count_letters(statement)
print(alphabets)


