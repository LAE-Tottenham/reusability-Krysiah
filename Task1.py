# Help! My code is too messy :( Please help me organise it and extract out the duplications.
# Make sure each function only does ONE thing!!!!!!!!!!!
# Define your reusable functions here:
import math
import functions 

def weird_calculation():
   print("Triangle 1")
   opp3 = functions.hypotenuse()

   print("Triangle 2")
   adj3 = functions.hypotenuse()
   
   hyp3 = math.sqrt(opp3**2 + adj3**2)
   return hyp3

weird_answer = weird_calculation()
print(weird_answer)


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# The input of the trianlge's opp & adj length must be a float/integer
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
#To shorten the code and avoid duplication of hypotenuse calculations
#We can import the hypotenuse function in many places

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
