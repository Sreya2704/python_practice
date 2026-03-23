def is_palindrome(text):
    reversed_text = ""
    
    for ch in text:
        reversed_text = ch + reversed_text
    
    if text == reversed_text:
        return True
    else:
        return False

print(is_palindrome("madam"))