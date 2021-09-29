# Python program to count vowel(s) and/or consonant(s) of an input string.

def main():
    user_input = input("Enter a string of vowels and consonants: ").lower()
    vowel_list = 'aeiou'
    countVowelsAndConsoants(user_input, vowel_list)


def countVowelsAndConsoants(user_input, vowel_list):
    vowels = len([char for char in user_input if char in vowel_list])
    print('Your input has', vowels, 'vowels.')
    print('Your input has', len(user_input) - vowels, 'consonants.')


main()
