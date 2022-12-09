import pandas as pd
import spacy

from processing import Processing
from helpers import levenshtein


class Filter:
    def __init__(self):
        self.test_data = pd.read_csv("test_data.csv", header=None)
        self.vulgar_words = pd.read_csv("vulgar_words.csv", header=None)
        self.black_list = ["dziwka", "szmata", "kurwa", "pedał", "chuj",
                           "zjeb", "frajer", "dymać", "pierdolić", "zajebiście", "politechnika"]
        self.black_list_lemmatized = []
        self.char_to_replace = {
            "0": "o",
            "1": "i",
            "2": "z",
            "3": "e",
            "4": "a",
            "5": "s",
            "v": "u",
            "vv": "w",
            "I": "l",
            "sh": "sz",
        }

        self.optional_char_to_replace = {
            "om": "ą",
            "l": "ł"
        }

        self.nlp = spacy.load("pl_core_news_lg")

        # lemmatize vulgar words
        for i in range(len(self.vulgar_words)):
            self.vulgar_words[0][i] = self.preprocess(
                self.vulgar_words[0][i])

        # lemmatized black list
        for word in self.black_list:
            self.black_list_lemmatized.append(self.preprocess(word))

    def preprocess(self, word):
        processing = Processing()
        word = processing.lower_case(word)
        word = processing.remove_special_chars(word)
        word = processing.replace_chars(word, self.char_to_replace)
        word = processing.remove_repeating_chars(word)
        word = processing.lemmatize(word, self.nlp)
        return word

    def isVulgar(self, word):
        word = self.preprocess(word)
        # check similarity
        for i in range(len(self.vulgar_words)):
            if (levenshtein(self.vulgar_words[0][i], word) < 2) or (levenshtein(self.vulgar_words[0][i], word) == 2 and len(word) > 4):
                return True
            if self.vulgar_words[0][i] in word:
                return True
        for black_list_word in self.black_list_lemmatized:
            if (levenshtein(black_list_word, word) < 2) or (levenshtein(black_list_word, word) == 2 and len(word) > 4):
                return True
            if black_list_word in word:
                return True
        return False
