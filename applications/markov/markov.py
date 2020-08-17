import random
import re

"""
Plan:
1. Read the file and split it into words
2. Analyz the text, building up the dataset
3. Choose a random "start word" to begin
4. Loop through
"""

# Read in all the words in one go
with open("input.txt") as f:
    words = re.findall(r"(\w[\w']*[?.!]*)", f.read())

dataset = {}
for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word in dataset:
        dataset[word].append(next_word)
    else:
        dataset[word] = [next_word]

# Make a list of start words
# if first/second character is capitalized, put into list
# Loop over out split_words and put any start word into a list
start_words = []
stop_signs = "?.!"

for key in dataset.keys():
    if key[0].isupper():
        start_words.append(key)

def generate_sentence():
    word = random.choice(start_words)
    string = word

    while word[-1] not in stop_signs:
        following_words = dataset[word]
        word = random.choice(following_words)
        string += " " + word
    
    return string



for _ in range(5):
    print(generate_sentence(),"\n")