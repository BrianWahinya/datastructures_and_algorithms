import random
import os

def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_unordered_integers(start, end):
    # Generate a list of integers between start and end (inclusive)
    all_integers = list(range(start, end + 1))

    # Shuffle the list to make it unordered
    random.shuffle(all_integers)

    return all_integers

def generate_ordered_integers(start, end):
    return list(range(start, end + 1))

def generate_random_integers(start, end, length):
    return [random.randint(start, end) for _ in range(length)]