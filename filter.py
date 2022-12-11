import pandas as pd
import spacy

from gensim.models import KeyedVectors
from processing import Processing
from helpers import levenshtein


class Filter:
    def __init__(self):
        self.vulgar_words = pd.read_csv("vulgar_words.csv", header=None)
        self.black_list = ["dziwka", "szmata", "kurwa", "pedał", "chuj",
                           "zjeb", "frajer", "dymać", "pierdolić", "zajebiście"]
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

        self.word2vec  = KeyedVectors.load("fasttext/fasttext_100_3_polish.bin")
        self.nlp = spacy.load("pl_core_news_lg")

    def preprocess(self, word):
        processing = Processing()
        word = processing.lower_case(word)
        word = processing.remove_special_chars(word)
        word = processing.replace_chars(word, self.char_to_replace)
        word = processing.remove_repeating_chars(word)
        return word
    
    def isVulgar(self, word):
        word = self.preprocess(word)
        # check similarity
        for i in range(len(self.vulgar_words)):
            if (((levenshtein(self.vulgar_words[0][i], word) < 2) or (levenshtein(self.vulgar_words[0][i], word) == 2 and len(word) > 4)) and
            (self.word2vec.wv.similarity(self.vulgar_words[0][i], word) > 0.7)):
                return True
            if self.vulgar_words[0][i] in word:
                return True
            if self.word2vec.wv.similarity(self.vulgar_words[0][i], word) > 0.76:
                return True
        for black_list_word in self.black_list:
            if (((levenshtein(black_list_word, word) < 2) or (levenshtein(black_list_word, word) == 2 and len(word) > 4)) and
            (self.word2vec.wv.similarity(black_list_word, word) > 0.7)):
                return True
            if black_list_word in word:
                return True
            if self.word2vec.wv.similarity(black_list_word, word) > 0.76:
                return True
        return False
    
    
