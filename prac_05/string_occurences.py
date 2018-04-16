words_frequency = {}
user_string = input("Enter a string: ")
words = user_string.split()
longest_length = 0
for word in words:
    if word in words_frequency:
        words_frequency[word] += 1
    else:
        words_frequency[word] = 1
        if len(word) > longest_length:
            longest_length = len(word)
for key, value in sorted(words_frequency.items()):
    print("{:{}} : {}".format(key, longest_length, value))