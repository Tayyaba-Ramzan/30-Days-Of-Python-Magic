# 30-Day Python Coding Challenge: From Basic to Advanced 

# Day 8: Dictionaries
# Question: Create a program that counts the frequency of words in a given string using a dictionary.

# Solution:

def count_word_frequency(text):
    words = text.split()  
    frequency = {}

    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1 

    return frequency

text = "This is a test. This test is simple."
word_count = count_word_frequency(text)
print(word_count)

#                            XXXXXXXXXXXXXXXXXXX