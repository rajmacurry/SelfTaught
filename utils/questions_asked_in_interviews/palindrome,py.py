def is_palindrome(w1):
    w1 = w1.lower()
    return w1[::-1] == w1

print(is_palindrome("level"))
