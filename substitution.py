def sub_cipher():

    file = open("file0.txt", 'r')
    contents = file.read()
    answer = ''
    for char in contents:
            
         
            old_char = ord(char) - 32
            new_char = 126 - old_char

           
            answer += (chr(new_char))


    return answer
def sub_cipher_5():
    
    file = open("file4.txt", 'r')
    contents = file.read()

    key =("`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"'"'"ZXCVBNM<>?")
  
    new_char = ''
    for char in contents:
        a = char
        loc = key.find(a)

 
        new_char += chr(loc + 33)

    return new_char


print(sub_cipher())
print("")
print("")

print(sub_cipher_5())
