# Python program to count vowel(s) and/or consonant(s) of an input string using a function.

def main():
    user_input = input("Please enter a string of your choice: ").lower()
    vowel_list = 'aeiou'
    countVowels(user_input, vowel_list)
    countConsonants(user_input, vowel_list)


def countVowels(user_input, vowel_list):
    vowels = len([char for char in user_input if char in vowel_list])
    print('Your input has', vowels, 'vowels.')


def countConsonants(user_input, vowel_list):
    vowels = len([char for char in user_input if char in vowel_list])
    print('Your input has', len(user_input) - vowels, 'consonants.')


main()
