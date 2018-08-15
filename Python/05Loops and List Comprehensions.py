####################################################################
######################## E X E R C I S E 1 #########################
####################################################################

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """    
    for num in nums:
        if num % 7 == 0:
            return True
    return False
q1.check()


####################################################################
######################## E X E R C I S E 2 #########################
####################################################################
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    #l = []
    #for i in range(len(L)):
    #    l.append(True if L[i] > thresh else False )
    #return l
    return [i > thresh for i in L] #list comprehension

q2.check()

####################################################################
######################## E X E R C I S E 3 #########################
####################################################################
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """    
    for i in range(len(meals)-1):
        if (meals[i] == meals[i + 1]):
            return True
    return False
q3.check()


####################################################################
######################## E X E R C I S E 4 #########################
####################################################################
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    total = 0
    pay_per_play_value = 1
    for run in range(n_runs):
        total += play_slot_machine()
    total - (pay_per_play_value * n_runs)
    return total / n_runs

estimate_average_slot_payout(1000)