from collections import Counter

# Program 1: Read Python.txt file and Print it in Reverse.

# with open('Python.txt', 'r') as file:
#     lines = file.readlines()
#     lines.reverse()
#     for line in lines:
#         print(line.strip())



# Program 2: Read Python.txt file and Print total number of lines and words in it.

# with open('Python.txt', 'r') as file:
#     lines = file.readlines()
#     num_lines = len(lines)
#     num_words = sum(len(line.split()) for line in lines)
#     print(f"Total number of lines: {num_lines}")
#     print(f"Total number of words: {num_words}")


# Program 3: Read Python.txt file and Print unique word with its count.

# with open('Python.txt', 'r') as file:
#     words = file.read().split()
#     word_count = Counter(words)
#     for word, count in word_count.items():
#         print(f"{word}: {count}")

# Program 4: Read Python.txt file and Print largest and smallest word from it.
# with open('Python.txt', 'r') as file:
#     words = file.read().split()
#     largest_word = max(words, key=len)
#     smallest_word = min(words, key=len)
#     print(f"Largest word: {largest_word}")
#     print(f"Smallest word: {smallest_word}")

# Program 5: Read Python.txt file. Convert it into upper case and write into another file "Python_Upper.txt"
with open('Python.txt', 'r') as source_file, open('Python_Upper.txt', 'w') as target_file:
    for line in source_file:
        target_file.write(line.upper())
