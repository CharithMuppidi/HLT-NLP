# imports
import sys
import nltk
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from random import randint
import operator
import pathlib

# processor for pre processing
def processor(str):
    # get tokens in lowercase raw text
    tokens = word_tokenize(str)
    tokens = [t.lower() for t in tokens]

    # reduce the tokens to only those that are alpha,
    # not in the NLTK stopword list, and have length > 5
    tokens = [t for t in tokens if t.isalpha() and
               t not in stopwords.words('english') and len(t) > 5]

    # lemmatize the tokens
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]

    # get unique lemmas
    unique_lemmas = list(set(lemmas))

    # pos tag the lemmas
    tags = nltk.pos_tag(unique_lemmas)
    print(tags[:20])

    # get the nouns
    nouns = [n[0] for n in tags if n[1] == 'NN' or n[1] == 'NNS' or n[1] == 'NNP' or n[1] == 'NNPS']

    # print number of tokens and nouns and then return them
    print("Number of Tokens: %d \nNumber of Nouns: %d" %(len(tokens), len(nouns)))
    return tokens, nouns

# method for guessing game/hangman
def guess_game(list):
    # print message to indicate start of game
    print("Let's play a word guesing game!")

    # give player five points
    pts = 5
    keep_playing = True

    while keep_playing:

        # randomly choose words
        game_word = list[randint(0, 50)][0]
        # prepare underscore space
        guess_word = '_' * len(game_word)
        # user will now begin scoring
        while pts >= 0:

            # output underscore/current space
            print(guess_word)
            letter = input("Guess a letter:")

            # check if it is one letter
            if len(letter) != 1:
                print("You must put in a letter")
                continue

            # check if the user wants to quit
            if letter == '!':
                print("Game Over! Final Score is %d" % pts)
                keep_playing = False
                break
            correct_guess = False

            # split characters apart
            game_letters = [*game_word]
            guess_letters = [*guess_word]
            # check to see if the letter is in the word
            for i in range(len(game_letters)):
                # if it is, replace the _'s with the letter and indicate correct guess
                if letter == game_letters[i]:
                    guess_letters[i] = letter
                    correct_guess = True

            # update the space
            guess_word = "".join(guess_letters)

            # print output based on guess
            if correct_guess:
                pts += 1
                print("Right! Score is %d" % pts)
                if '_' not in guess_word:
                    print("You solved it! \n\nCurrent Score: %d" % pts)
                    print("Guess another word")
                    break
            else:
                pts -= 1
                # check if the user lost
                if pts < 0:
                    print("Game Over!")
                    print("The word was %s" % game_word)
                    keep_playing = False
                    break
                else:
                    print("Sorry, guess again. Score is %d" % pts)

# main method
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        exit(1)
    # user enters path and program checks if it is correct
    raw_text = ""
    # save file as raw text
    with open(pathlib.Path.cwd().joinpath(sys.argv[1]), 'r') as f:
        raw_text = f.read()

    # print lexical diversity
    tokens1 = word_tokenize(raw_text)
    unique_tokens1 = set(tokens1)
    print("\nLexical diversity: %.2f" % (len(unique_tokens1) / len(tokens1)))

    # process the raw text into tokens
    tokens, nouns = processor(raw_text)

    # make a dictionary of nouns and number of them in list of tokens
    word_dict = {k:tokens.count(k) for k in nouns}
    word_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))
    word_list = list(word_dict.items())

    # same 50 most common words to new list
    game_list = [word_list[i] for i in range(50)]
    # print the 50 words and word counts
    print(game_list)
    # play the game
    guess_game(game_list)

