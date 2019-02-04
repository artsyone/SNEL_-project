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
    V = 0 
    for i in outcomes:
        V = (i - expected) ** 2 / (expected)

        
        

    print (V)


count_rolls()
sum_of_all()
expected_count(count_rolls(), sum_of_all())
chi_square(expected_count(count_rolls(), sum_of_all()))

