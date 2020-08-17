# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re

with open("ciphertext.txt") as f:
    encoded = f.read()

counter = {}

for char in encoded:
    if re.match(r'[a-zA-Z]', char):
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

counter = {k: v for k,v in sorted(counter.items(), key=lambda x: x[1], reverse=True)}
normal = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
mapped = {a: b for a,b in zip(counter.keys(), normal)}

decoded = ""

for char in encoded:
    if re.match(r'[a-zA-Z]', char):
        decoded += mapped[char]
    else:
        decoded += char

print(decoded)