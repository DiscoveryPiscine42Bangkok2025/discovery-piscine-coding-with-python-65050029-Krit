import sys

if len(sys.argv) != 2:
    print("none")
else:
    str = sys.argv[1]
    z = str.count("z")

    if z == 0:
        print("none")
    else:
        print("z" * z)
