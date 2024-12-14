def permute_a_palindrome(word):
    return len({letter for letter in word if word.count(letter) % 2 != 0}) < 2