# Let user create anagrams phrases from desired word

import sys
from collections import Counter
from load_dictionary import load

dict_file = load(r"C:\Users\Admin\Searches\Regular Expressions practice problems\Book_Project3\dic.txt")
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

initial_name = input("Enter a name: ")


#_________________________________________________________________________________________________________________________________________________________________________
def find_anagrams(name, wordlist):
    """ Extract list of words which can be constructed from the letters in name"""

    #create a dictionary with letters as keys and count as values
    name_letter_map = Counter(name)
    #create an empty list of subset words
    anagrams = []

    #iterate over list of words
    for word in wordlist:
        
        test = ""
        word_letter_map = Counter(word)
        for letter in word:
            if word_letter_map[letter] <= name_letter_map.get(letter, 0):
                test += letter

        if Counter(test) == word_letter_map:
            anagrams.append(word)

    print("Available words: ")
    print(*anagrams, sep="\n")
    print("Letters left =", name)
    print("Number of letters left =", len(name))






#________________________________________________________________________________________________________________________________________________________________________
def process_choice(name):
    """ask for users choice, check validity and return leftover letters and name"""

    while True:
        choice = input('Make a valid choice, else press enter to start over or # to quit: ')
        
        if choice == "":
            main()
        elif choice == '#':
            sys.exit(1)
        else:
            
            candidate = "".join(choice.lower().split())
            leftover_letters = list(name)

            for letter in candidate:
                if letter in leftover_letters:
                    leftover_letters.remove(letter)

            if len(name) - len(leftover_letters) == len(candidate):
                break
            else:
                print("Sorry! Won't work. Try another choice")

    return choice, name

    


#_______________________________________________________________________________________________________________________________________________________________________
def main():
    """pass"""
    #remove white spaces
    name = "".join(initial_name.split())
    #remove hyphens
    name = name.replace("-", "")

    limit = len(name)
    phrase = ""
    running = True

    while running:

        temp_phrase = phrase.replace(" ", "")

        if len(temp_phrase) < limit:

            print("Current phrase: ", phrase)

            find_anagrams(name, dict_file)

            choice, name = process_choice(name)
            phrase += choice + " "
            print("Current phrase: ", phrase)

        elif len(temp_phrase) == limit:
            print("*************FINISHED*************")
            print('Anagram phrase: ', phrase)

            try_again = input("Enter to go again, x to exit: ")
            
            if try_again.lower() == "x":
                running = False
                sys.exit()

            elif  try_again == "":
                main()





if __name__ == "__main__":
    main()
