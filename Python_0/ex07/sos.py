import sys
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def main():
    """
Main function to convert a given alphanumeric string to Morse code.

This function takes a single command-line argument, which is a string
containing alphanumeric characters and spaces. It converts the string to
Morse code using the predefined NESTED_MORSE dictionary.

Usage:
    python script.py "your string here"

Args:
    None (uses sys.argv for command-line arguments)

Raises:
    AssertionError: If the arguments are not as expected (single non-empty
    alphanumeric string).

Returns:
    None
    """
    args = sys.argv[1:]
    if len(args) != 1:
        print("AssertionError: the arguments are bad")
        return
    if all(c.isalnum() or c.isspace() for c in args[0]) is False:
        print("AssertionError: the arguments are bad")
        return
    if args[0] == '':
        return
    args[0] = args[0].upper()
    [print(NESTED_MORSE[letter], end="") for letter in args[0][:-1]]
    print(NESTED_MORSE[args[0][-1]][:-1])


if __name__ == "__main__":
    main()
