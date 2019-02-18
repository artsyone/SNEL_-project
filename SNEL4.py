import random
import math
import string
import os

def practice_random():
    num_chars = 18000
    result = ""
    for i in range(num_chars):
        n = random.randrange(32,127)
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
    #print (file_names)
     
    #fix the fact it doesnt increase files


def get_char_counts(result):

    counts = [0] * 127
    for c in result:
        n = ord(c)
        counts[n] += 1
    counts = counts[32:]

    return counts 
     
   

   
def chi_square(counts):

    a = sum(counts[32:])
    b =(len(counts[:]))
    
    x = 0
    
    expected = a / b
    
    for observed in range(b) :
        x += (observed - expected) ** 2 / (expected)
    return x 

    print(expected)
    
def file_read():
    for n in range(18000): 
         file = open("file" + str(get_hex(n)) + '.txt', 'r')
         print(x)


    

#write get hex function

  
''' you got it to at least add all the letters for each letter''' 


#lets do this
'''
num_files = 1
threshold = 50


for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content("files/"+ file_name)
    counts = get_char_counts(text)
    chi_square = chi_square(counts)


    if chi_square > threshold:
        print(file_name,chi_square)
'''

print( get_file_name(0) ) # file_0000.txt
print( get_file_name(9) ) # file_0009.txt
print( get_file_name(10) ) #file_000A.txt
print( get_file_name(2342) )
print( get_file_name(17999) )
print( get_file_content(0)   )
print( get_char_counts(practice_random())  )

#fix chi_square!!!
num = 0
for i in range(11):
    
    print( get_file_name(num) )
    print( get_file_content(num)   )
    print( chi_square(( get_char_counts(practice_random())  )))

    num += 1 

    print(num)

#print( get_char_counts(get_file_content()) )



