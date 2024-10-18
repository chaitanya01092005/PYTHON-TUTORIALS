# Function to check if a word is a palindrome
def is_palindrome(word):
    # Convert the word to lowercase for uniformity
    word = word.lower()
    # Compare the word to its reverse
    return word == word[::-1]

# Input: Word to check
input_word = input("Enter a word: ")

# Check if the input word is a palindrome
if is_palindrome(input_word):
    print(f'"{input_word}" is a palindrome.')
else:
    print(f'"{input_word}" is not a palindrome.')
