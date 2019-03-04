def vig_cipher():
    key_word = ("enigma")
    file = open("file2.txt", 'r')
    contents = file.read()
    answer = ''
    item = 0
    
    for char in contents:
        num = key_word[item]
        new_char = ord(char) - ord(num)
        
        if new_char < 32:
            new_char + 95 

        answer += chr(new_char)

        item += 1 
        if item > 6:
            item = 0             
        
    return answer 
   

print(vig_cipher())
