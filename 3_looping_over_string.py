# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.

# Challenge:
# Count how many vowels are in the word.
word = input("Pick a word: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowel_counter = 0



for letter in word:
    print(letter)
    if letter in vowels:    
        vowel_counter += 1
        

    
    
print(f"There are {vowel_counter} vowel/vowels.")
