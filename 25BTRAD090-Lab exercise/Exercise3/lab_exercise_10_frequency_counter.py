# Lab Exercise 10: Frequency Counter Using Dictionaries
# Student: Rithik Roshan | USN: 25BTRAD090
#Word Frequency counter
sentence = input("Enter a sentence: ")

# Make everything lowercase so "Python" and "python" count together
sentence = sentence.lower()

# Split the sentence into individual words
words = sentence.split()

word_counts = {}

# Count each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


print("\nWord counts:")

for word, count in word_counts.items():
    print(f"{word}: {count}")
