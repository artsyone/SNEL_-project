def vig_cipher():
    key_word = ("enigma")
    file = open("file2.txt", 'r')
    contents = file.read()
    answer = ''
    item = 0
    num = key_word[item]
    for char in contents:

        new_char = ord(char) - ord(num)
        
        if item > 6:
            item = 0 
     
        if new_char < 0:
            if new_char + 95 > 126:
                
                #diff = 

                final_char = ord(32 + new_char + diff)
                answer += chr(final_char)
            else:
                new_char + 95 
                final_char = ord( new_char)
                answer += chr(final_char)
                

            else:
                final_char = new_char + 95
                answer += chr(final_char)
                item += 1 
            
        else:
            new_char
            answer += chr(new_char)
            item += 1 
            
        

            

       
    return answer 
   

print(vig_cipher())
