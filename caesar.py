def caesar_cipher():

    file = open("file6.txt", 'r')
    contents = file.read()
    new_char = ''
    for char in contents:

        

        if ord(char) <= 65:
            old_char = ord(char) + 61
            new_char += chr(old_char)

        else:
            old_char = ord(char) - 34 
            new_char += chr(old_char)

            
    return new_char


print(caesar_cipher())
