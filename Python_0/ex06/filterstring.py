import sys
import ft_filter


def wordGreater(word, min_len):
    """
wordGreater(word, min_len) --> Boolean

Return a boolean indicating if the word is greater than min_len.

Args:
    word (str): The word to be checked.
    min_len (int): The minimum length to compare against.

Returns:
    bool: True if the word length is greater than min_len, False otherwise.
    """
    if len(word) <= min_len:
        return False
    else:
        return True


def main():
    """
Main function to filter words based on their length.

This function takes command-line arguments to filter a list of words. The
first argument is a string containing words separated by spaces, and the
second argument is an integer representing the minimum length a word must
have to be included in the output.

Usage:
    python script.py "word1 word2 word3" 4

Args:
    None (uses sys.argv for command-line arguments)

Raises:
    AssertionError: If the arguments are not as expected (string and integer).

Returns:
    None
    """
    args = sys.argv[1:]
    if len(args) != 2:
        print("AssertionError: the arguments are bad")
        return
    try:
        i = int(args[1])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return
    if type(args[0]) is not str:
        print("AssertionError: the arguments are bad")
        return
    words = args[0].split()
    print(list(ft_filter.ft_filter(lambda seq: wordGreater(seq, i), words)))


if __name__ == "__main__":
    main()
