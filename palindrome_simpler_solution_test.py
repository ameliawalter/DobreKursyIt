def check_for_palindrome(word):
    # Convert the input to lowercase and remove non-alphanumeric characters
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())

    # Reverse the cleaned word
    reversed_word = cleaned_word[::-1]

    # Check if the cleaned word is the same when reversed
    is_palindrome = cleaned_word == reversed_word
    message = "It is a palindrome :)" if is_palindrome else "It is not a palindrome :("

    return is_palindrome, message

result, message = check_for_palindrome("A man, a plan, a canal, Panama!")
print(result)  # True
print(message)  # "It is a palindrome :)"

import pytest

def test_check_for_palindrome():
    assert check_for_palindrome("racecar") == (True, "It is a palindrome :)")
    assert check_for_palindrome("hello") == (False, "It is not a palindrome :(")
    assert check_for_palindrome("A man, a plan, a canal, Panama!") == (True, "It is a palindrome :)")
    assert check_for_palindrome("") == (True, "It is a palindrome :)")  # Edge case: empty string

def test_case_sensitivity():
    assert check_for_palindrome("Racecar") == (True, "It is a palindrome :)")

def test_non_alphanumeric_chars():
    assert check_for_palindrome("Madam, I'm Adam.") == (True, "It is a palindrome :)")

