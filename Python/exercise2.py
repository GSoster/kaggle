####################################################################
######################## E X E R C I S E 1 #########################
####################################################################
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    #pass
    return round(num, 2)

#q1.check()

####################################################################
######################## E X E R C I S E 3 #########################
####################################################################

def to_smash(total_candies, friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between the given number of friends. 
    If no friends quantity is provided the function assumes a value of 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends

#q3.check()

####################################################################
######################## E X E R C I S E 4 #########################
####################################################################

x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))

def f(x):
    y = abs(x)
    return y

print(f(-5))

####################################################################
######################## E X E R C I S E 5 #########################
####################################################################
from time import time
def time_call(fn, arg):
    """Return the amount of time the given function takes (in seconds) when called with the given argument.
    """
    previousTime = time()
    fn(arg);
    afterwardsTime = time()
    timeTaken = afterwardsTime - previousTime
    return(timeTaken)

fn = lambda time: sleep(time)
time_call(fn,1)


####################################################################
######################## E X E R C I S E 6 #########################
####################################################################
def slowest_call(fn, arg1, arg2, arg3):
    """Return the amount of time taken by the slowest of the following function
    calls: fn(arg1), fn(arg2), fn(arg3)
    """
    return max(time_call(fn, arg1), time_call(fn, arg2), time_call(fn, arg3))    

slowest_call(sleep, 2, 1, 4)


####################################################################
######################## E X E R C I S E 8 #########################
####################################################################
# A:

def smallest_stringy_number(s1, s2, s3):
    """Return whichever of the three string arguments represents the smallest number.
    
    >>> smallest_stringy_number('1', '2', '3')
    '1'
    """
    return min(s1, s2, s3)

smallest_stringy_number('10.5', '2', '32')

# B:
def smallest_stringy_number(s1, s2, s3):
    """Return whichever of the three string arguments represents the smallest number.
    
    >>> smallest_stringy_number('1', '2', '3')
    '1'
    """
    return str(min(int(s1), int(s2), int(s3)))

q8.b.check()