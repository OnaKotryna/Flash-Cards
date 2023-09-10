import pandas as pd
import random
import os


WORDS_TO_LEARN_FILE = "./data/words_to_learn.csv"
ALL_WORDS = "./data/de_1k.csv"

# Get data
try:
    df = pd.read_csv(WORDS_TO_LEARN_FILE)  
except FileNotFoundError:
    df = pd.read_csv(ALL_WORDS)
finally:
    df = df.head(100)
    word_data = df.to_dict(orient="records")


def get_languages():
    '''Get languages from data.'''
    return df.columns.tolist()


def get_word():
    '''Get random word from word list.'''
    try:
        return random.choice(word_data)
    except IndexError:
        return None


def remove_word(word):
    '''Remove the word from data and save updated word list.'''
    global word_data
    word_data.remove(word)
    save_words()


def save_words():
    '''Save updated word list.'''
    global word_data
    if word_data:
        df = pd.DataFrame(word_data)
        df.to_csv(WORDS_TO_LEARN_FILE, index=False)
    else:
        os.remove(WORDS_TO_LEARN_FILE)
