def reverse_string(text):
    reversed_text = ""
    
    for ch in text:
        reversed_text = ch + reversed_text
    
    return reversed_text

print(reverse_string("hello"))