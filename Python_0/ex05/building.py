import sys


def ispunctuation(c):
    """
    Checks if a given character is a punctuation mark.

    Parameters:
    c (str): The character to check.

    Returns:
    int: 1 if the character is a punctuation mark, otherwise 0.
    """
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for p in punc:
        if c == p:
            return 1
    return 0


def main():
    """
    Main function that analyzes the text provided via command line arguments
    or prompts for user input if no argument is provided.

    Features:
    - Checks if more than one argument is provided and displays an error if so.
    - Prompts the user to enter text if no argument is provided.
    - Counts and displays the number of uppercase letters, lowercase letters,
        punctuation marks, spaces, and digits in the text.

    Returns:
    int: 1 if more than one argument is provided, otherwise 0.
    """
    args = sys.argv[1:]
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return 1
    elif len(args) == 0:
        args = [""]
        args[0] = input("What is the text to count?\n")
        args[0] += "\n"
        print("The text contains %d characters:" % len(args[0]))
    print("%s upper letters" % sum(1 for c in args[0] if c.isupper()))
    print("%s lower letters" % sum(1 for c in args[0] if c.islower()))
    print("%s punctuation marks" % sum(1 for c in args[0] if ispunctuation(c)))
    print("%s spaces" % sum(1 for c in args[0] if c.isspace() or c == '\n'))
    print("%s digits" % sum(1 for c in args[0] if c.isdigit()))
    return 0


if __name__ == "__main__":
    main()
