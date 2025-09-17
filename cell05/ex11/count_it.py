import sys

Word =  sys.argv[1:]

NumWord = len(Word)

if NumWord == 0:
    print("none")
else:
    print(f"parameters: {NumWord}")
    for parameter in Word:
        print(f"{parameter}: {len(parameter)}")
    