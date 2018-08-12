####################################################################
######################## E X E R C I S E 1 #########################
####################################################################

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    return L[1] if len(L)>=2 else None
q1.check()


####################################################################
######################## E X E R C I S E 2 #########################
####################################################################
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[len(teams)-1][1]

q2.check()



####################################################################
######################## E X E R C I S E 3 #########################
####################################################################
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    temp = racers.pop()
    racers.append(racers[0])
    racers[0] = temp    
q3.check()


####################################################################
######################## E X E R C I S E 5 #########################
####################################################################
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """    
    isFashionably = True
    index = arrivals.index(name)
    return False if (index == (len(arrivals)-1) or index < (len(arrivals)/2)) else True
    # Clear way to read the above statement
    #if (index == (len(arrivals)-1)):
    #    isFashionably = False
    #if (index < (len(arrivals)/2)):
    #    isFashionably = False
    #return isFashionably
    

q5.check()

####################################################################
######################## E X E R C I S E 6 #########################
####################################################################
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """            
    if (0 not in nums):
        nums.append(0)
    nums.sort()
    return nums.index(0)

#count_negatives([3,2,-3,-2,-1,0,1])
q6.check()