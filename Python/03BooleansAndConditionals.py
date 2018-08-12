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

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


####################################################################
######################## E X E R C I S E 4 #########################
####################################################################
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0

q4.check()

####################################################################
######################## E X E R C I S E 5 #########################
####################################################################

# A:
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

# B:
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup == mustard == onion == True

q5.a.check()

# C:
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    #return not ketchup and not mustard and not onion
    return ketchup == mustard == onion == False

q5.b.check()

# D:
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return ketchup != mustard

q5.c.check()

####################################################################
######################## E X E R C I S E 6 #########################
####################################################################

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int (mustard) + int(onion)) == 1

q6.check()

####################################################################
######################## E X E R C I S E 7 #########################
####################################################################

# 42% win rate
def should_hit(player_total, dealer_total, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay. player_aces is the number of aces the player has.
    """
    hit = False
    if player_total < 12:
        hit = True
    if dealer_total > 17 and player_total < 17:
        hit = True
    return hit

q7.simulate(n_games=1000)