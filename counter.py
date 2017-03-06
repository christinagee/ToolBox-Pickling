""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import os.path
import sys
from pickle import dump, load
import pickle
import requests


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    #if the file exist, read its counter value in pickle
    if exists(file_name):
        counter = load(open(file_name, 'rb+'))
    #if file exists but we want to reset it, bring the counter value back to 0
        if reset == True:
            counter = 0
        counter += 1
        dump(counter, open(file_name, 'wb'))  # Dump the counter back into the pickle

    #if the file does not exist, set counter to 1 and store it in pickle, then have it loop to existing file
    else:
        counter = 1
        dump(counter, open(file_name, 'wb'))
    return counter



if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod(verbose = True)
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
