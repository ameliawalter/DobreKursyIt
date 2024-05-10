def check_for_palindrome():
    # Get input from the user, convert it to lowercase and convert string into a list
    word = input("Type the word to check: ").lower()
    word_list = list(word)
    print(word_list)

    # Reverse the word
    reversed_word = []
    for i in reversed(word_list):
        reversed_word.append(i)
    print(reversed_word)

    # Compare both words (normal list and reversed list) - they are identical in palindromes
    if word_list == reversed_word:
        print("It is a palindrome :)")
    else:
        print("It is not a palindrome :(")


check_for_palindrome()

