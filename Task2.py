import requests
from pyfiglet import Figlet
import os, time
import gender_guesser
import Wfunction
import facts
import welcomefont

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!

###########################################

def weird_weather_bot():
    
    #intro (with added pizzaz :D)
    welcomefont.intro()

    #gender guess
    gender_guesser.gen_guess() 

    #weather check 1
    global pstcode
    pstcode = input("\nSo, what's your postcode? ")
    Wfunction.weathercheck_1(postcode_raw=pstcode)

    #funfact
    facts.funfact()

    #weathercheck 2
    Wfunction.weathercheck_2(postcode_raw=pstcode)

weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# All of the imports, so that the (valid) data entered can easily be refered to
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# To make the code faster and more efficient to use
# It's good to have a collection of functions to use accross different works whenever you need to re-use it.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
