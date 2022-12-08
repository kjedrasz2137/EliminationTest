import pandas as pd
import spacy
import re


def main():
    
    # ___data/dicts___ #
    nlp = spacy.load("pl_core_news_lg")
    test_data = pd.read_csv("/Users/ben/python_projects/hackathon_gcm_2023/test_data.csv", header=None)
    wulgaryzmy = pd.read_csv("/Users/ben/python_projects/hackathon_gcm_2023/wulgaryzmy.csv", header=None, index_col=[0])
    black_list = ["dziwka", "szmata", "kurwa", "pedał", "chuj", "zjeb", "frajer", "dymać", "pierdolić", "zajebiście"]

    char_to_replace = {
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

    optional_char_to_replace = {
        "om": "ą",
        "l": "ł"
    }



    # ___step_functions___ 
    def lower_case(word):    
        # Step no. 1
        return word.lower()
    
    def remove_special_chars(word):
        # Step no. 2
        pattern = r'[^A-Za-z0-5]+'
        n_word = re.sub(pattern, '', word)
        n_word = re.sub(r"\s+", "", n_word, flags=re.UNICODE)
        return n_word
    
    def replace_chars(word):
        # Step no. 3
        for i in range(len(char_to_replace)):
            word = re.sub(list(char_to_replace.keys())[i], list(char_to_replace.values())[i], word)
        return word
    

    def remove_repeating_chars(word):
        # Step no. 4
        new_word = word[0]
        for i in range(1, len(word)):
            if word[i]!=word[i-1]:
                new_word += word[i]
            else:    
                pass
        return new_word
    
    

    
    # ___main_loop___     
    for word in test_data[0]:
        # Steps no. 1-6
        new_word = lower_case(word)
        new_word = remove_special_chars(new_word)
        new_word = replace_chars(new_word)
        new_word = remove_repeating_chars(new_word)
    
        # Step no. 7-10
        for i in range(len(new_word)):
            
            # Step no. 7
            if i != 0:
               start = new_word[:i]
               middle = new_word[i]
               end = new_word[i+1:]
               prop_word = start+end
            else:
               prop_word = new_word
            
            # Step no. 8
            # (TO DO)
            
            # Step no. 9
            #(TO DO)
            
            # Step no. 10
            prop_word = nlp(prop_word) 
            for words in prop_word:
                prop_word = words.lemma_
            
            # Step no. 11
            #(TO DO)
            
            # Step no. 12
            if (prop_word in black_list) or (prop_word in wulgaryzmy.values.tolist()):
               l = len(word)
               print(l*"*"+f" ({word})")
            else:
               pass





if __name__ == "__main__":
    main()


