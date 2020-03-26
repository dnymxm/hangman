import json
import random


def get_word():
    with open("word_list.json", "r") as f:
        word = random.choice(json.load(f))
        return word
