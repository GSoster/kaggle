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