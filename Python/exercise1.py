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


####################################################################
######################## E X E R C I S E 4 #########################
####################################################################


# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3 # == 1

#q4.check()

####################################################################
######################## E X E R C I S E 6 #########################
####################################################################
# The following is an example of a tricky piece of arithmetic manipulation you might encounter when using Python for visualization.

# Suppose we're working with the [QuickDraw dataset](https://www.kaggle.com/google/tinyquickdraw) of doodled sketches and we want to visualize several sketches at once in a grid-like arrangement.

# We'd like to reserve 2x2 inches for each image, and we'd like the whole grid to be no wider than 16 inches.

# The code below almost works. It does the following:

# 1. Get a random number of sketches from some category (e.g. bears, stars, hockey sticks...)
# 2. Create variables `rows`, `cols`, `height`, and `width`, setting them to numbers we pulled out of the air.
# 3. Calls `plt.subplots()` using the variables from step 2, which creates a grid with the given characteristics.
# 4. Draws the sketches from step 1 in the grid from step 3.
import random
from matplotlib import pyplot as plt
from learntools.python.quickdraw import random_category, sample_images_of_category, draw_images_on_subplots

## Step 1: Sample some sketches
# How many sketches to view - a random number from 2 to 20
n = random.randint(2, 20)

# Choose a random quickdraw category. (Check out https://quickdraw.withgoogle.com/data for an overview of categories)
category = random_category()
imgs = sample_images_of_category(n, category)

## Step 2: Choose the grid properties
######## Your changes should go here ###############
rows = ((n * 2) / 16) + 0.5 #precisa arredondar, ex.: (9 * 2) / 16 = 1.25 -> necessário arredondar p/cima: rounded_up = -(-numerator // denominator)
rows = int(round(rows))
if rows == 0:
    rows = 1
cols = n
if cols > 8:
    cols = 8
# The height and width of the whole grid, measured in inches.
height = 2 * rows
width = 2 * cols
if width > 16:
    width = 16
#print("N: ", n, " rows: ", rows, " cols: ", cols, " Width: ", width, " height: ", height)
## Step 3: Create the grid
grid = plt.subplots(rows, cols, figsize=(width, height))

## Step 4: Draw the sketches in the grid
draw_images_on_subplots(imgs, grid)