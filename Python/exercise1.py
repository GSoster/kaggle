####################################################################
######################## E X E R C I S E 1 #########################
####################################################################

pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * radius ** 2
print(area)
#q1.check() # area should be 7.0685775


####################################################################
######################## E X E R C I S E 2 #########################
####################################################################

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
#q2.store_original_ids()
######################################################################
temp = a
a = b
b = temp
# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

######################################################################
#q2.check()


#OBS: the code below can also be used to swap values, it uses tuples:
# a, b = b, a
