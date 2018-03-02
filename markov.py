"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path, 'r') as f:
        green_eggs = f.read()

    return green_eggs


def make_chains(text_string):
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

    green_eggs = open_and_read_file(input_path)
    word_list = green_eggs.split()
    for item in range(0, len(word_list) - 2):
        if item == len(word_list) - 3:
            chains[(word_list[item + 1], word_list[item + 2])] = [None]
        tup = (word_list[item], word_list[item + 1])
        if tup not in chains:
            chains[tup] = [word_list[item + 2]]
        else:
            chains[tup].append(word_list[item + 2])

    # print word_list
    return chains

    # your code goes here

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    for keys, values in chains:
        words.append(keys)
        value = choice([values])
        words.append(value)

        #keys = words[keys]
    # your code goes here
    print " ".join(words)
    #return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
