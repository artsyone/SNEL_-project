import random
import math
import string
import os

def practice_random():
    num_chars = 18000
    result = ""
    for _ in range(num_chars):
        n = random.randrange(32,126)
        
        result += chr(n)
        
    return(result)

def random_file_writer(num_chars):
    file_num = "0"
    for n in range(num_files):
        files =  open("file" + str(file_num) + '.txt', 'w' )
        file_num += str(1)
       
def get_file_name(num):
    num_str = hex(num)
    num_str = num_str[2:]

    return "file_" + num_str.upper().zfill(4) + ".txt"


def get_file_content(num):
    # open file_name, read it, return the contents

    
    num_str = hex(num)
    num_str = num_str[2:]
    
        
    file_names = open('text_files/file_' + num_str.upper().zfill(4) + '.txt', 'r')
         
    return(file_names)
   

def get_char_counts(result):

    counts = [0] * 127
    for c in result:
        n = ord(c)
        counts[n] += 1

    final_counts = [count for count in counts if count != 0]

    return final_counts 
     
   
def chi_square(counts):

    a = sum(counts)
    b = len(counts)
   
    
    x = 0
    
    expected = a / b
    
    for observed in counts  :
        x += (observed - expected) ** 2 / (expected)
    return x 

    print(expected)
    
    
def first_char():
    
    for i in range(18000):
        url = ''
        with open("text_files/file_" + hex(i)[2:].upper().zfill(4) + ".txt", "r") as file:
            file_r = file.read()

        url += str(file_r[0:1])
        

        print(url,end= '')
        
   
#lets do this


print( get_file_name(0) ) # file_0000.txt
print( get_file_name(9) ) # file_0009.txt
print( get_file_name(10) ) #file_000A.txt
print( get_file_name(2342) )
print( get_file_name(17999) )
print( get_file_content(0)   )
print( get_char_counts(practice_random())  )


equal = 0
for i in range(1):
    
    with open("text_files/file_" + hex(i)[2:].upper().zfill(4) + ".txt", "r") as file:
        file_r = file.read()

   
    
    if (chi_square(get_char_counts(file_r))) > 147:


    
        print(chi_square(get_char_counts(file_r)))


        print(hex(i)[2:].upper().zfill(4))

        equal += 1 

        print(equal)




   
   

   
      


  





