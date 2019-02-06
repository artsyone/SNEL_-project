import random
import math

die_rolls = [1,2,3,4,5,6]
outcomes = [11,9,7,8,14,11]


def count_rolls():
    rolls = 0 
    for die in die_rolls:
        rolls += 1
    return rolls 

def sum_of_all():
    count = 0 
    for o in outcomes:
        count += o

    return count

def expected_count(rolls,count):

    expected = (count/rolls)
    
    return expected

def get_char_count():
    count = [0] * 127
    return counts[32:]


def chi_square(expected):
   print(sum([(i - expected) ** 2 / expected for i in outcomes]))
   
    
def random_file_writer():
    file_num = "0"

    for n in range(num_files):
        files =  open("file" + str(file_num) + '.txt', 'w' )

        files.write(str(random.randrange(32,127)))
        
        file_num += str(1)

#def get_file_content(file_name):
        ''' helps with coops files'''
    #with open(file_name,'r') as f :
        #content = f.read()
    #return content

#lets do this
num_files = 2
threshold = 50

#for n in range(num_files):
    #if chi square > threshold:

        #print(files,chi_square)


    

    









        

count_rolls()
sum_of_all()
expected_count(count_rolls(), sum_of_all())
chi_square(expected_count(count_rolls(), sum_of_all()))
random_file_writer()

