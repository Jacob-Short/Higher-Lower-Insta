from game_data import data
import random
from ascii_art import logo, vs
import os

clear = lambda: os.system('clear')

def get_random_account():
    '''get data from random account'''
    return random.choice(data)

def format_data(account):
    '''format account into printable format: name, desc, country'''
    name = account['name']
    description = ['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'

def check_answer(guess, a_followers, guess, b_followers):
    '''Checks followers against users and
    returns True if they got it right or 
    false if they got it wrong.    
     '''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


