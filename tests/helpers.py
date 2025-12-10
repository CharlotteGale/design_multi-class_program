import random

def generate_contents(word_count):
    return " ".join(["word"] * word_count)

def generate_numbered_contents(word_count):
    return " ".join([f"word{i}" for i in range(1, word_count + 1)])

def generate_uk_mobile():
    # Generate 9 random digits after the '07'
    number = '07' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return number