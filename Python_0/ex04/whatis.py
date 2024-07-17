import sys

if len(sys.argv) == 1:
    sys.exit()
if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()

txt = sys.argv[1]
if sys.argv[1][0] == '-' or sys.argv[1][0] == '+':
    txt = sys.argv[1][1:]

if txt.isdigit():
    i = int(txt)
    if i % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    print("AssertionError: argument is not an integer")
    sys.exit()
