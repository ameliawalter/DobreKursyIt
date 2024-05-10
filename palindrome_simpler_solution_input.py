def check_for_palindrome():
    # Get input and convert it to lowercase
    word = input("Type the word to check: ").lower()

    # Compare both words (normal list and reversed list) - they are identical in palindromes
    # Use shorthand if
    print("It is a palindrome :)") if word == word[::-1] else print("It is not a palindrome :(")


check_for_palindrome()

