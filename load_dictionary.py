import sys

def load(file):
    """open a text file and return a list of lowercase strings"""
    try:
        with open(file) as f:
            list_words = f.read().strip().split('\n')
            list_words = [x.lower() for x in list_words]

            return list_words
    except IOError as e:
        print(f"{e}\nError opening{file}\nTerminating Program", file = sys.stderr)
        sys.exit(1)