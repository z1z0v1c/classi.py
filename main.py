import sys


def main():
    if (len(sys.argv) != 2):
        print("Specify the path to a single folder")
        sys.exit(1)
    else:
        print(sys.argv[1])


if __name__ == "__main__":
    main()
