import pandas as pd
import spacy
import re




def main():
    nlp = spacy.load("pl_core_news_sm")
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


    
    for word in test_data[0]:
        # Step no. 1
        n_word = word.lower()
        
        # Steop no. 2
        pattern = r'[^A-Za-z0-5]+'
        n_word = re.sub(pattern, '', n_word)
        n_word = re.sub(r"\s+", "", n_word, flags=re.UNICODE)
       
        # Step no. 3
        for i in range(len(char_to_replace)):
            n_word = re.sub(list(char_to_replace.keys())[i], list(char_to_replace.values())[i], n_word)
        
        # Step no. 4
        new_word = n_word[0]
        for i in range(1, len(n_word)):
            if n_word[i]!=n_word[i-1]:
                new_word += n_word[i]
            else:
                pass
  
        # Step no. 5
        new_word = nlp(new_word) 
        for words in new_word:
            new_word = words.lemma_
       
        # Step no. 6+7
        if new_word in black_list or new_word in wulgaryzmy.values:
            l = len(word)
            print(l*"*"+f" ({word})")
        else:
            print(word)
            
if __name__ == "__main__":
    main()


