# ------------
# Version 1 - plain code

# f = open('lorem_ipsum.txt', mode='rt', encoding='utf-8')
# file_words = []
# for line in f:
#     line_words = line.split()
#     for word in line_words:
#         file_words.append(word)
# f.close()
# for word in file_words:
#     print(word)


# ------------
# Version 2 - organized into functions

# def fetch_words():
#     f = open('lorem_ipsum.txt', mode='rt', encoding='utf-8')
#     file_words = []
#     for line in f:
#         line_words = line.split()
#         for word in line_words:
#             file_words.append(word)
#     f.close()
#     for word in file_words:
#         print(word)

# ------------
# Version 3 - add __name__

# def fetch_words():
#     f = open('lorem_ipsum.txt', mode='rt', encoding='utf-8')
#     file_words = []
#     for line in f:
#         line_words = line.split()
#         for word in line_words:
#             file_words.append(word)
#     f.close()
#     for word in file_words:
#         print(word)


# print(__name__)


# ------------
# Version 4 - make runnable as cript and importable as module

# def fetch_words():
#     f = open('lorem_ipsum.txt', mode='rt', encoding='utf-8')
#     file_words = []
#     for line in f:
#         line_words = line.split()
#         for word in line_words:
#             file_words.append(word)
#     f.close()
#     for word in file_words:
#         print(word)


# if __name__ == '__main__':
#     fetch_words()

# ------------
# Version 5 - add print_words() and main()

# def fetch_words():
#     f = open('lorem_ipsum.txt', mode='rt', encoding='utf-8')
#     file_words = []
#     for line in f:
#         line_words = line.split()
#         for word in line_words:
#             file_words.append(word)
#     f.close()
#     return file_words


# def print_words(words):
#     for word in words:
#         print(word)


# def main():
#     words = fetch_words()
#     print_words(words)


# if __name__ == '__main__':
#     main()

# ------------
# Version 6

# import sys

# def fetch_words(filename):

#     f = open(filename, mode='rt', encoding='utf-8')
#     file_words = []
#     for line in f:
#         line_words = line.split()
#         for word in line_words:
#             file_words.append(word)
#     f.close()
#     return file_words


# def print_items(items):
#     for item in items:
#         print(item)


# def main(filename):
#     words = fetch_words(filename)
#     print_items(words)


# if __name__ == '__main__':
#     filename = sys.argv[1]
#     main(filename)

# ------------
# Version 7 - include docstrings

"""Retreive and print words from file.

Usage:
    python words.py <filename>
"""

import sys


def fetch_words(filename):
    """Fetch list of words from file.

    Args:
        filename : file to fetch words from

    Returns:
        A list of strings containing the words from file
    """

    f = open(filename, mode='rt', encoding='utf-8')
    file_words = []
    for line in f:
        line_words = line.split()
        for word in line_words:
            file_words.append(word)
    f.close()
    return file_words


def print_items(items):
    """Print items one per line.

    Args:
        An iterable serie of printable items
    """
    for item in items:
        print(item)


def main(filename):
    """Print each word from a text document from a file.

    Args:
        filename: Name of a text file in UTF-8 encoding
    """
    words = fetch_words(filename)
    print_items(words)


if __name__ == '__main__':
    filename = sys.argv[1] # The 0th argument is the module filename.
    main(filename)
