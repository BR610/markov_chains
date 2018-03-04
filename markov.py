"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file():

    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_path = sys.argv[1]
    #print file_path
    file_data = open(file_path, 'r')
    gettysburg = file_data.read()

    return gettysburg


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    gettysburg = open_and_read_file()
    word_list = gettysburg.split()

    #iterating through length of word_list
    for item in range(0, len(word_list) - n):
        key_list = []
        #spefical case, last items
        # if item == len(word_list) - 3:
        #     chains[(word_list[item + 1], word_list[item + 2])] = [None]
        #iterating to find tuple_keys until n
        for count in range(item, n + item):

            key_list.append(word_list[count])
            #print key_list
        tuple_key = tuple(key_list)

        #print tuple_key

        if tuple_key not in chains:

            chains[tuple_key] = [word_list[item + n]]
        else:
            chains[tuple_key].append(word_list[item + n])

    # print word_list

    return chains

    # your code goes here

    #print chains


def make_text(chains):
    """Return text from chains.
    """
    for keys, values in chains.items():
        print keys, values
    print
    words = []

    #1 create a link, which is a tuple from chains dic
    #2 extend tuple key into word list
    #3 get random word from list of words, list is value of key
    #4 make a new key out of the second word from link[1] and the random that was
    #selected in previous step
    #5 check/look up to see if new key which is currently link to see if it is in
    #the dic, if yes, repheat ste 4
    #if no, you are done! return words list joined as string

    #advanced logic loop
    # link_key = choice(chains.keys())
    # words.extend(link_key)

    # while link_key in chains:
    #     random_word = choice(chains[link_key])
    #     words.append(random_word)
    #     link_key = (link_key[1], random_word)

    link_key = choice(chains.keys())
    words.extend(link_key)
    random_word = choice(chains[link_key])
    words.append(random_word)
    while True:

        link_key = (link_key[1], random_word)

        if link_key in chains:
            random_word = choice(chains[link_key])
            words.append(random_word)
        else:
            break

    print " ".join(words)
    return " ".join(words)


#input_path = "getstysburg.txt"'''

#Open the file and turn it into one long string
input_text = open_and_read_file()

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains)
