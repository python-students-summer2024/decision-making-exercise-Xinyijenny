"""
A few decision-making puzzles to solve using if/elif/else logic.
Do not call any of these functions from within this file... only do that by running the main.py file.
Your job is to complete the definitions of each function so that it achieves its indicated behavior.
"""

import math
import datetime


def get_year():
    """
    This function is given to you... it is used by the is_leap_year() function below.
    Do not modify this function.
      :returns: The current y.ear, eg. 2020
    """

    now = datetime.datetime.now()  # get the current time now
    year = now.year  # the current year
    return year


def is_square():
    """
    Asks the user to enter the width and height of an area in inches and determines whether it is square.
    Users can enter either integers or floating point numbers.

      :returns: True if square (i.e. if equal length and height), False otherwise.
    """
    #### write your solution for this function below here. ####
    width = input("Width in inches: ")
    height = input("height in inches: ")

    # check the input, turn in to float or integer
    if "." in width:
        width = float(width)
    else:
        width = int(width)

    if "." in height:
        height = float(height)
    else:
        height= int(height)
    # check the square
    if width == height:
        return True
    else:
        return False



def get_greatest():
    """
    Asks the user for two integers, and returns the number that is greatest, as an int.
    You are not allowed to use Python's builtin max() function for this.
    If both numbers are the same, return that number.

    :returns: the greatest of the two input numbers, as an int.
    """
    #### write your solution for this function below here. ####

    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))

    if int1 > int2:
        return int1
    else:
        return int2  




def get_bmi_category():
    """
    Asks the user to enter their height (in inches) and weight (in pounds), in that order, and then returns the user's BMI statistical category.
    Users can enter either integers or floating point numbers.

    The BMI formula was developed in the 1830s, and is still widely used today in public health policy, medical practice, and legislation.
    The formula for calculating BMI is 703 * weight / height^2.
    The BMI statistical categories are:
    - Very severely underweight (BMI < 15)
    - Severely underweight (15 <= BMI < 16)
    - Underweight (16 <= BMI < 18.5)
    - Normal (18.5 <= BMI < 25)
    - Overweight (25 <= BMI < 30)
    - Moderately obese (30 <= BMI < 35)
    - Severely obese (35 <= BMI < 40)
    - Very severely obese (BMI >= 40)

      :returns: The name of the BMI statistical category, based on the inputted height and weight.
    """
    #### write your solution for this function below here. ####

    
    height = input("Your Height(in inches): ")
    weight = input("Your Weight(in pounds): ")

    # determine if input is float or integer
    if "." in weight:
        weight = float(weight)
    else:
        weight = int(weight)
    if "." in height: 
        height = float(height)
    else:
        height = int(height)
    
    # calculation BMI
    bmi =  703 * weight / height**2
    print(bmi)

    if bmi < 15 :
        return "Very severely underweight"
    elif bmi >= 15 and bmi < 16:
        return "Severely underweight"
    elif bmi >= 16 and bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    elif bmi >= 30 and bmi < 35:
        return "Moderately obese"
    elif bmi >= 35 and bmi < 40:
        return "Severely obese"
    else:
        return "Very severely obese"
    





def get_discount():
    """
    Imagine this scenario: a surgical mask distributor will give you a 20% discount on orders of 5000 or more.
    Each mask individually costs $5.
    This function asks the user how many masks they would like, and returns the total cost after applying any relevant discount
    The total cost must be rounded to the nearest integer and formatted as in "$4,000".

      :returns: The cost of the masks, after any discounts, e.g. "$4,000" for 1000 masks.
    """
    #### write your solution for this function below here. ####
    num_mask = int(input("How many masks do you want?"))
    
    # total = number * cost
    cost_of_mask = num_mask * 5
   

    if num_mask >= 5000:
        return "$" + format(round(0.8 * cost_of_mask),",d") # round to nearest int and format with "," for thousands
    else:
        return "$" + format(cost_of_mask,",d")
    
    
    
     


def is_leap_year():
    """
    Determines whether the current year is a leap year.
    Any year evenly divisible by 4 is a leap year, except century years such as 1900, 2000, 2100, etc. Only century years evenly divisible by 400 are leap years.

    :returns: True if the current year is a leap year, False otherwise.
    """
    year = (
        get_year()
    )  # this line is given to you - the variable, year, holds the current year
    #### write your solution for this function below here. ####

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


