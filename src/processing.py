import re


class Processing:
    def __init__(self):
        pass

    # function to lower case word
    def lower_case(self, word):
        return word.lower()

    # function to remove special characters from word, but keep polish characters
    def remove_special_chars(self, word):
        return re.sub(r"[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]", "", word)

    # function to replace characters in word with characters from dictionary, like "vv" to "w"
    def replace_chars(self, word, char_to_replace):
        for key, value in char_to_replace.items():
            word = word.replace(key, value)
        return word

    # funtion to remove repeating characters that are next to each other, like "oooo" to "o"
    def remove_repeating_chars(self, word):
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1", word)

    # function to lemmatize single word, like "koty" to "kot" or "kotów" to "kot"
    def lemmatize(self, word, nlp):
        word = nlp(word)
        for words in word:
            word = words.lemma_
        return word
