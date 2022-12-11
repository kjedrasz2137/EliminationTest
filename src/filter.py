import pandas as pd
import spacy

from processing import Processing
from helpers import levenshtein


class Filter:
    def __init__(self):
        self.vulgar_words = pd.read_csv("data/vulgar_words.csv", header=None)
        self.black_list = ["dziwka", "szmata", "debil", "kurwa", "pedał", "chuj",
                           "zjeb", "frajer", "dymać", "pierdolić", "zajebiście"]
        self.black_list_lemmatized = []
        self.char_to_replace = {
            "vv": "w",
            "om": "ą",
            "sh": "sz",
            "0": "o",
            "1": "i",
            "2": "z",
            "3": "e",
            "4": "a",
            "5": "s",
            "6": "b",
            "v": "u",
            "q": "k",
            "@": "a",
            "$": "s",
            "€": "e",
            "¥": "y",
            "¢": "c",
            "©": "c",
            "®": "r",
            "°": "o",
            "×": "x",
            "§": "s",
            "•": "o",
        }
        self.nlp = spacy.load("pl_core_news_sm")

        # not lemmatized vulgar words
        for i in range(len(self.vulgar_words)):
            self.vulgar_words[0][i] = self.preprocess(
                self.vulgar_words[0][i])

        # lemmatized vulgar words
        self.vulgar_words_lemmatized = self.vulgar_words[0].apply(
            self.preprocess, lemmatize=True)

        # append lemmatized vulgar words to vulgar words
        self.vulgar_words = self.vulgar_words.append(
            self.vulgar_words_lemmatized, ignore_index=True)
        self.vulgar_words = self.vulgar_words.drop_duplicates()
        self.vulgar_words = self.vulgar_words.reset_index(drop=True)

        # lemmatized black list
        for word in self.black_list:
            self.black_list_lemmatized.append(self.preprocess(word))
            self.black_list_lemmatized.append(
                self.preprocess(word, lemmatize=True))

    # function to preprocess word
    def preprocess(self, word, lemmatize=False):
        processing = Processing()
        word = processing.lower_case(word)
        word = processing.replace_chars(word, self.char_to_replace)
        word = processing.remove_special_chars(word)
        word = processing.remove_repeating_chars(word)
        if lemmatize:
            word = processing.lemmatize(word, self.nlp)
        return word

    # function to check if word is vulgar
    def isVulgar(self, word, lemmatized=False):
        # Preprocess word
        word = self.preprocess(word, lemmatized)
        if lemmatized:
            nlp_word = self.nlp(word)

        # Check similarity against vulgar words
        for i in range(len(self.vulgar_words)):
            if levenshtein(self.vulgar_words[0][i], word) < 2:
                return True
            if self.vulgar_words[0][i] in word:
                return True
            if lemmatized:
                if self.nlp(self.vulgar_words[0][i]).similarity(nlp_word) > 0.95:
                    return True

        # Check similarity against blacklisted words
        for blacklisted_word in self.black_list_lemmatized:
            if levenshtein(blacklisted_word, word) < 2:
                return True
            if blacklisted_word in word:
                return True
            if lemmatized:
                if self.nlp(blacklisted_word).similarity(nlp_word) > 0.95:
                    return True

        # If no match was found, return False
        return False
