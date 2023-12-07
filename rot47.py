def rot47(text):
    result = ""
    
    for char in text:
        if char.isprintable():
            if '!' <= char <= '~':
                result += chr(((ord(char) - 33 + 47) % 94) + 33)
            else:
                result += char
        else:
            result += char
    
    return result


original_text = input("Enter a text to ROT47 encode: ")
encoded_text = rot47(original_text)
print("--------------------------------------")
print("\nOriginal Text: ", original_text)
print("--------------------------------------")
print("\nROT47 Encoded: ", encoded_text)
print("--------------------------------------")
