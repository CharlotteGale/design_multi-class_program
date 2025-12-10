import random

def generate_contents(word_count):
    return " ".join(["word"] * word_count)

def generate_uk_mobile():
    number = '07' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return number