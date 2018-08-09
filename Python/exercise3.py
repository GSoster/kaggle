####################################################################
######################## E X E R C I S E 1 #########################
####################################################################

# Your code goes here. Define a function called 'sign'
def sign(value):
    if value < 0:
        return -1
    elif value > 0:
        return +1
    else:
        return 0
q1.check()

####################################################################
######################## E X E R C I S E 2 #########################
####################################################################
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies" if total_candies > 1 else "candy")
    return total_candies % 3

to_smash(91)
to_smash(1)

####################################################################
######################## E X E R C I S E 3 #########################
####################################################################