import random
import math
import string



def pratice_random():
    num_chars = 18000
    result = ""
    for i in range(num_chars):
        n = random.randrange(32,127)
        result += chr(n)
    return(result)


def get_char_counts(result):
    counts = [0] * 127
    
    for c in result:
        n = ord(c)
        counts[n] += 1
        
    
    counts = counts[32:]
    print(counts)


def random_file_writer(num_chars):
    file_num = "0"

    for n in range(num_files):
        files =  open("file" + str(file_num) + '.txt', 'w' )

        file_num += str(1)

        for i in range(1):
            files.write(num_chars)
        
        

def chi_square(i):
    expected = i/126
    
    for n in num_files :
        pass
        
''' you got it to at least add all the letters for each letter 


#lets do this
num_files = 1
threshold = 50

'''for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content("files/"+ file_name)
    counts = get_char_counts(text)
    chi_square = chi_square(counts)


    if chi_square > threshold:
        print(file_name,chi_square)'''

    

    









pratice_random()

get_char_counts(pratice_random())

#chi_square()
random_file_writer(pratice_random())

