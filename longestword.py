# How to transfer one file to another and finding the longest word in the file.

with open('filename.txt', 'w') as infile:
    infile.write('Those who like me raise your hands and those who does not like me raise your standards')

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('filename.txt'))
