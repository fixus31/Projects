#!/usr/bin/python3

import random

words = []

with open("sowpods.txt", "r") as file:
    line = file.readline().strip()
    while line:
        line = file.readline().strip()
        words.append(line)

rand_index = random.randint(0, len(words))

print("Welcome to Hangman!")
word = words[rand_index]
original_word = list(word)
word = list(word)
word_pattern = "_" * len(word)
word_pattern = list(word_pattern)
guess = []
guesses_left = 6
count = 0
while original_word != guess and guesses_left > 0:
    guessing_char = input("Guess your letter: ")
    guessing_char = guessing_char.upper()
    if guessing_char in word and guessing_char not in guess:
        index = word.index(guessing_char)
        word_pattern[index] = guessing_char
        guess.insert(index, guessing_char)
        word[index] = '_'
        i = 0
        while i < len(original_word):
            if word[i] == guessing_char:
                count += 1
                word[i] == '_'
                guess.insert(i, guessing_char)
                word_pattern.insert(i, guessing_char)
            i += 1
             
    elif guessing_char in guess:
        print("You already typed it")
    else:
        guesses_left -= 1
        print("Incorrect. ",guesses_left, " guesses left" )
        
    for char in range(0, len(word_pattern) - count):
            print(word_pattern[char], " ", end = "")
    
    




