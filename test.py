from collections import Counter


def word_letter_count(str):
    word_counts = dict()
    letter_counts = dict()
    words = str.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        letters = word.split()
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    counter = Counter(word_counts)

    counter2 = Counter(letter_counts)
    most_occur = counter.most_common(1)
    most_occur_letter = counter2.most_common(2)
    print(most_occur)
    print(most_occur_letter)
    return word_counts
word_letter_count("Hey Hello Hello Hello Hoe")
