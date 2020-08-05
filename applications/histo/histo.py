from functools import cmp_to_key
import re

with open("robin.txt") as f:
    words = re.split(r'\s\W*|\W*\s|\W*$|^\W*', f.read())

counter = {}
max_len = 0
for word in words:
        if word:
            word = word.lower()
            if len(word) > max_len:
                max_len = len(word)
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1

def compare_strings(a,b):
    if a[0] == b[0]:
        if len(a) > 1 and len(b) > 1:
            return compare_strings(a[1:], b[1:])
    return ord(b[0]) - ord(a[0])

def compare(a,b):
    if a[1] == b[1]:
        return compare_strings(a[0], b[0])
    else:
        return a[1] - b[1]

counter = {k: v for k,v in sorted(counter.items(), key=cmp_to_key(compare), reverse=True)}

for k,v in counter.items():
    k = k + (max_len - len(k) + 2) * " "
    v = v * "#"
    print(k, v)