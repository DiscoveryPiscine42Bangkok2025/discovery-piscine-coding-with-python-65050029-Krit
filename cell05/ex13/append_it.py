import sys

Word = sys.argv[1:]

if not Word:
    print("none")
else:
    for W in Word:
        match W.endswith("ism"):
            case True:
                pass
            case False:
                print(f"{W}ism")