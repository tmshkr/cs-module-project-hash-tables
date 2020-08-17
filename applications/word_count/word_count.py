import re

def word_count(s):
    counter = {}
    words = re.split(r'\s\W*|\W*\s|\W*$|^\W*', s)
    
    for word in words:
        if word:
            word = word.lower()
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    
    return counter



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))