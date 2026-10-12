# ------------------------------------------------------
#        Name: Ace Carpenter
#       Peers: NA
#  References: Lecture 10: More About Conditionals and Lecture 12: More Loops Debugging (Specifically the Old McDonald example)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Asks user for string input and checks if dog, Dog, or the secret word is included in the string"""
    dog_l = "dog"
    dog_u = "Dog"
    user_input = input("Give me a sentence: ")
    while secret_word not in user_input and dog_l not in user_input and dog_u not in user_input:
        print("Try again")
        user_input = input("Give me a sentence: ")

    if dog_l in user_input or dog_u in user_input:
        print("You used the word \"dog\" or the word \"Dog\"!")
    else:
        print("You used the secret word!")

# Task 2
def check_greater():
    """Checks two integers to find which one is greater than the other"""
    int_1 = int(input("Give me a first integer: "))
    int_2 = int(input("Give me a second integer: "))
    while int_1 == int_2:
        print("Try again")
        int_1 = int(input("Give me a first integer: "))
        int_2 = int(input("Give me a second integer: "))
    if int_1 > int_2:
        print("First is Greater")
    else:
        print("Second is Greater")


# Task 3
def get_special_numbers():
    """Prints numbers between 1-40 that meet the specified conditions"""
    for int in range(40):
        #Simplified by checking if int is odd, a multiple of 3, and not a multiple of 5
       if int%2==1 and int%5 != 0 and int%3 == 0:
           print(int)

# Task 4.a
def my_for_loop():
    """Asks user for string input, checks if input meets conditions, and prints what letters in the string are vowels or consonants"""
    user_input = input("Give me a string: ")
    letters = len(user_input)
    #Len function converts user_input into an integer of how many letters the string had
    vowels = ("a", "e", "i", "o", "u", "y")
    if 2> letters or letters >5 or " " in user_input:
         print("bad word")
         return
    for let in user_input:
        if let in vowels: 
            print( let + " is a vowel")
        else:
            print( let + " is a consonant")

# Task 4.b
def my_while_loop():
    """Asks user for letter input (a, b, c), checks to see if input meets conditions, and runs different commands depending on the letter chosen
        for selection a: asks for letter input again
        for selection b: prints Goodbye and returns
        for selction c: exits
        """
    user_input = input("Choose one option: a, b, or c: ")
    #Have to use and here since if it was or then every letter would pass the condition
    while user_input != "a" and user_input != "b" and user_input != "c":
        print("try again")
        user_input = input("Choose one option: a, b, or c: ")
    while user_input == "a":
        user_input = input("Choose one option: a, b, or c: ")
    while user_input == "b":
        print("Goodbye")
        return
    while user_input == "c":
        sys.exit()

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
