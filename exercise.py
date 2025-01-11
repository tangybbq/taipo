#! /usr/bin/env python3

import re
import random

# Constants
NUM_WORDS = 8  # Number of words to generate in the exercise
MIN_LENGTH = 2  # Minimum length of words
MAX_LENGTH = 7  # Maximum length of words
LETTERS = "rsniaote"  # Letters to be used in words
LETTERS = "nitearoslcudpmhgbfywkvxzjq"

# Occasionally insert numbers containing these digits.
DIGITS = "0123456789"
DIGIT_AMOUNT = 1.0 / 20.0
DIGIT_AMOUNT = 1.0 / 10.0

# Make sure to choose words with these letters.
MUST = LETTERS
MUST = "q"

SYMBOLS = '#@$&+*^='

LINES = 10
LINES = 5

# Load the plover word list.
english_words = []
# with open("/home/davidb/linaro/zep/rp-rs/plover/plover/assets/american_english_words.txt") as fd:
# with open("moby-project/moby/mwords/10001fr.equ") as fd:
with open("moby-project/moby/mwords/354984si.ngl") as fd:
    fd.readline()
    fd.readline()
    for line in fd:
        fields = line.split()
        english_words.append(fields[0])

# Sample list of English words for demonstration
# In a real scenario, this could be loaded from a comprehensive dictionary file or API
# ENGLISH_WORDS = [
#     "reason", "note", "stone", "tones", "senior", "stare", "stain", "train", "rain", "neat",
#     "eat", "tea", "aero", "ante", "earn", "near", "rate", "taser", "tenor", "tensor", "toner",
#     "saint", "satin", "stern", "store", "rest", "rose", "site", "tire", "rote", "sane", "rent",
#     "nest", "nose", "not", "seat", "set", "sin", "son", "star", "tar", "tie", "toe", "ton"
# ]

def filter_words(words, letters, min_length, max_length):
    """Filter words by specified letters and length range."""
    pattern = re.compile(f"^[{letters}]+$")
    mpattern = re.compile(f".*[{MUST}].*")
    return [word for word in words
            if pattern.match(word) and mpattern.match(word)
            and min_length <= len(word) <= max_length]

def generate_typing_exercise(num_words, min_length, max_length, letters, lines):
    """Generate a typing exercise with specified parameters."""
    # Filter the word list
    valid_words = filter_words(english_words, letters, min_length, max_length)
    
    exercises = []
    for i in range(lines):
        # Select a random sample of words
        if len(valid_words) < num_words:
            print("Warning: Not enough words to meet the request. Using the maximum available.")
            exercise_words = valid_words
        else:
            exercise_words = random.choices(valid_words, k=num_words)

        exercise = ''
        cap = True
        for word in exercise_words:
            if cap:
                word = word.capitalize()
                cap = False
            if len(exercise) > 0:
                exercise += ' '
            exercise += word

            if random.random() < 0.15:
                exercise += ','
            elif random.random() < 0.1:
                exercise += '.'
                cap = True

            # Periodically insert a number.
            if not cap and random.random() < DIGIT_AMOUNT:
                size = random.randrange(5 - 2 + 1) + 2
                text = ''.join(random.choices(DIGITS, k=size))
                exercise += ' ' + ''.join(random.choices(SYMBOLS, k=1))
                exercise += text
        
        # Create the exercise string
        # exercise = ' '.join(exercise_words)
        exercise = exercise.rstrip(',.')
        exercise += '.'
        exercises.append(exercise)
    return exercises

# Generate the typing exercise
typing_exercise = generate_typing_exercise(NUM_WORDS, MIN_LENGTH, MAX_LENGTH, LETTERS, LINES)
for line in typing_exercise:
    print('>', line)
