import random
import math

die_rolls = [1,2,3,4,5,6]
outcomes = [11,9,7,8,14,11]

#observed =




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



def chi_square(expected):
   print(sum([(i - expected) ** 2 / expected for i in outcomes]))
   

def get_char_counts(text):
    counts = [0] * 127
    '''do stuff here'''
    return counts[32:]

       
def get_file_name(num):

    for n in num_files:
        with open(file_name + '.txt', 'w') as f:
            print ("Fingers crossed")
  

    ''' returns a file name like file_00001.txt '''
    pass
def get_file_content(file_name):
    with open(file_name,'r') as f :
        content = f.read()
    return content
    
def random_file_writer():
    pass


#lets do this

num_files = 2
threshold = 50

for n in range(num_files):
    file_name = get_file_name(n)
    text = get_file_content("files/"+ file_name)
    counts = get_char_counts(text)
    chi_square = chi_square(counts)


    if chi_square > threshold:
        print(file_name,chi_square)



        

count_rolls()
sum_of_all()
expected_count(count_rolls(), sum_of_all())
chi_square(expected_count(count_rolls(), sum_of_all()))

