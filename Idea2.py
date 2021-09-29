# Python program to count vowel(s) and/or consonant(s) of an input string.

# Define all vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']

# Input a string and transform it to lower case
str = input("Enter a string: ").lower()

# Define counter variable for both vowels and consonants
v_ctr = 0
c_ctr = 0

# Iterate through the characters of the input string
for x in str:
    # If character is in the vowel list,
    # Update the vowel counter otherwise update consonant counter
    if x in vowels:
        v_ctr += 1
    else:
        c_ctr += 1

# Output the values of the counters
print("Vowels: ", v_ctr)
print("Consonants: ", c_ctr)
