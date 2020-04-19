from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['krishna','madhusudan','nrsimha']

def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise(InvalidWordException)
    return(list_of_words[randint(0, len(list_of_words))])

def _mask_word(word):
    if len(word) == 0:
        raise(InvalidWordException)
    return('*'* len(word))

def _uncover_word(answer_word, masked_word, character):
    if len(answer_word)== 0 and len(masked_word) == 0:
        raise(InvalidWordException)
    elif len(masked_word) > 1:
        raise(InvalidGuessedLetterException)
    elif len(masked_word) > len(answer_word):
        raise(InvalidWordException)
    else:    
        index = [i for i,x in enumerate(list(answer_word)) if x==uppercase(character) or x==lowercase(character)]
        for a in index:
            masked_word[index] = character
    
    return(masked_word)

def guess_letter(game, letter):
    
    if game['masked_word'] == answer_word:
        raise(GameFinishedException)
    else:
        prev_word = game['masked_word']
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'],letter)
        game['previous_guess'] = game['previous_guess'].append(letter)
        
        if game['masked_word'] == prev_word:
            game['remaining_misses'] = game['remaining_misses'] - 1
        
        if game['masked_word'] == answer_word:
            raise(GameWonException)
        elif remaining_misses <= 0:
            raise(GameLostException)
     
    return(game)

def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
