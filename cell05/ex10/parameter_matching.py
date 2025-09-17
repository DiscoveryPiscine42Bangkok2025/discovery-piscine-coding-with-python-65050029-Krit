import sys

if len(sys.argv) == 2:
    Word = sys.argv[1]

    input = input("What was the parameter? ")

    if input == Word:
        print("Good job!")
    else :
        print("Nope, sorry...")
else:
    print("none")