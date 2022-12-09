import re


class Processing:
    def __init__(self):
        pass

    def lower_case(self, word):
        return word.lower()

    def remove_special_chars(self, word):
        pattern = r'[^A-Za-z0-5]+'
        word = re.sub(pattern, '', word)
        word = re.sub(r"\s+", "", word, flags=re.UNICODE)
        return word

    def replace_chars(self, word, char_to_replace):
        for i in range(len(char_to_replace)):
            word = re.sub(list(char_to_replace.keys())[i], list(
                char_to_replace.values())[i], word)
        return word

    def remove_repeating_chars(self, word):
        new_word = word[0]
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                new_word += word[i]
            else:
                pass
        return new_word

    def remove_optional_chars(self, word):
        optional_char_to_replace = {
            "om": "ą",
            "l": "ł"
        }

        for i in range(len(optional_char_to_replace)):
            word = re.sub(list(optional_char_to_replace.keys())[i], list(
                optional_char_to_replace.values())[i], word)
        return word

    def lemmatize(self, word, nlp):
        word = nlp(word)
        for words in word:
            word = words.lemma_
        return word
