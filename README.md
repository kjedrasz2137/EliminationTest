# EliminationTest

This repository contains the solution to the first task of the Elimination Test - the first stage of BEST Coding Marathon 2023.

## Problem description

In the internet age, we increasingly encounter filtering of comments or chat in terms of offensive content. In the case of many websites, this is due to the need to maintain a certain level of culture, due to the requirements of advertisers who do not want their brand to be associated with "inappropriate environments". Nevertheless, the filters currently in use still do not work perfectly - their creators, in order to limit the number of "false positives", often settle for limited solutions. Furthermore, internet users who want to bypass censorship make matters more difficult by using tricks such as replacing certain letters in words with similarly looking signs, or writing in a not entirely grammatically correct way. As a result, the initially trivial problem of removing offensive content becomes significantly more difficult (for example, a chat filter introduced some time ago in one of the popular games did not allow the use of the word night because of the alleged similarity to a very unpleasant word).

## Task

The goal of the task is to implement a filter that replaces letters of Polish swear words with asterisks (*).

## Solution

As our input is a sentence, we first need to split it into words by using the `split()` method. Then, we can apply some preprocessing on the words.

### Preprocessing

We apply the following preprocessing steps in given order:
1. Turn all letters into lowercase, i.e. `KuRwA` -> `kurwa`
2. Replace sequences of characters with their equivalents, i.e `kurvva` -> `kurwa`, `shmata` -> `szmata`, `jebanom` -> `jebaną`
3. Replace characters with their equivalents, i.e `qvrw@` -> `kurwa`, `d21wk4` -> `dziwka`, `$pi3®dal@©` -> `spierdalac`
4. Remove all non-alphabetic characters, i.e. `kurwa!` -> `kurwa`, `d.z,i.w^k.#a??` -> `dziwka`, `&spier%%dal;ac` -> `spierdalac`
5. Remove repeated characters, i.e. `kurwwwwwwwwwwa` -> `kurwa`, `dziiiwkkaaaa` -> `dziwka`, `spieeerdaalac` -> `spierdalac`
6. Lemmatize the words to their base form so that inflections are removed, i.e. `kurwami` -> `kurwa`, `dziwce` -> `dziwka`, `hujowi` -> `huj`, `spierdalając` -> `spierdalać`

### Filtering

After preprocessing, we can check if the word is a swear word. 

Algorithm for checking if a word is a swear word:

For every blacklisted word:
1. If the Levenshtein distance between the word and the blacklisted word is less than 2, the word is a swear word.
2. If the blacklisted word is a substring of the word, the word is a swear word.
3. If similarity between the word and the blacklisted word is greater than 0.95, the word is a swear word.

If the word is a swear word, we replace all letters with asterisks. Otherwise, we leave the word unchanged.

Explantions:
The Levenshtein distance is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. We use `similarity` function from spaCy library that returns a number between 0 and 1, where 1 means that the words are identical. We set the threshold to 0.95, because we want to avoid false positives.

### Postprocessing

After filtering, we need to join the words back into a sentence. We do this by joining the words with a space character.

## How to run

1. Clone the repository with `git clone https://github.com/kjedrasz2137/EliminationTest.git` or download the zip file
2. Install dependencies with `pip install -r requirements.txt`
3. Run the program with `python src/main.py`

## How to test

Type your text in the input field and click the button. The result will be displayed in the output field.
Please be aware that this can take a while, depending on the length of the text.
Additionally, you can add your own words to the list of swear words by appending them to the black list field.
Please note that the words must be separated by a comma.

## Example video

[![Example video](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Team `*FutureTeamName*`

* [Krzysztof Jędraszek](https://github.com/kjedrasz2137)
* [Filip Erni](https://github.com/filiperni)
* [Beniamin Sereda](https://github.com/ujo142)
* [Jakub Pilarski](https://github.com/limmesi)
