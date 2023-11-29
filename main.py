import os
import sys


def main():
    if (len(sys.argv) != 2):
        print("Specify the path to a single folder")
        sys.exit(1)
    else:
        try:
            folder_path = sys.argv[1]
            os.chdir(folder_path)
            print(f"Changed working directory to: {folder_path}")
        except FileNotFoundError:
            print(f"The folder '{folder_path}' does not exist.")


if __name__ == "__main__":
    main()
