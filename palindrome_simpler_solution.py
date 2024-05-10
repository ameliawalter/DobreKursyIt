def check_for_palindrome(word):
    # Convert the word parameter to lowercase
    word = word.lower()

    # Compare both words (normal list and reversed list) - they are identical in palindromes
    # Use shorthand if
    print("It is a palindrome :)") if word == word[::-1] else print("It is not a palindrome :(")


check_for_palindrome('Omo')

