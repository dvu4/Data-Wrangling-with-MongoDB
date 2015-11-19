
'''
Programming background in Python.

The first exercise allows you to assess your ability to program in Python.
As a data analyst, you will spend much of your time writing code and
programs to work with data or to build mathematical, statistical, or
machine learning models to find insights from data.

Complete this function that modifies a list of integers.

1)  For numbers that are multiples of three replace the integer with the string "Fizz".

2)  For numbers that are multiples of five replace the integer with the string "Buzz".

3)  For numbers that are multiples of both three AND five replace the integer
    with the string "FizzBuzz"

Your function should take in a list of integers as input.
Your function should not modify the input list.
Your function should return an updated list with integers and strings.
'''


def fizzbuzz(intList):
    '''
    Your fizzbuzz function. The grader will run `fizzbuzz(intList)` to check if your
    function returns the correct output.
    
    intList: list containing integers

    Make sure you write the script so that your algorithm is part of the
    function; you do not need to call the function yourself.
    '''

    # YOUR CODE HERE
    print "The original list of integers:",intList
    new_list = intList
    
    for indx, val in enumerate(new_list):
        if val%5 == 0 and val%3 == 0:
            new_list[indx] = 'FizzBuzz'
        elif val%3 == 0:
            new_list[indx] = 'Fizz'
        elif val%5 == 0:
            new_list[indx] = 'Buzz'
    
    print "The new list of integers:",new_list
        
                      
    return new_list


#intlist = [3,4,6,15,35,78,99,135]
intlist= [1,4,2,5,7,8,9,11,13,75]
#intlist = [31,41,36,145,775,789,919,1315]
new_list = fizzbuzz(intlist)

'''

def test():
    #intlist = [3,4,6,15,35,78,99,135]
    intlist= [1,4,2,5,7,8,9,11,13,75]
    #intlist = [31,41,36,145,775,789,919,1315]
    new_list = fizzbuzz(intlist)

    
test()
'''
