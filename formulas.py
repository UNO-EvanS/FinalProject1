# Model
import random, sys

#This function will return the sum of all negative numbers in values. If none are present, returns as 0.
def add(values):
    sum = 0
    for x in values:
        if x < 0:
            sum += x
    return sum

#This function will return the difference of all the positive numbers in values. If none are present, returns as 0.
def subtract(values):
    pos_vals = [x for x in values if x > 0]
    if len(pos_vals) == 0: #If there are no positive values in the input, will return 0.
        return 0
    difference = pos_vals[0]
    for x in pos_vals[1:]:
        difference -= x
    return difference

#This function will return the product of all the non-zero numbers in values. If none are present, returns as 0.
def multiply(values):
    non_zeroes = [x for x in values if x != 0] #Will collect all the non-zero values
    product = 1 #Will multiply the first value by one to get that number for the next iteration
    if len(non_zeroes) == 0:
        return 0 #If no non-zero values exist in the input, will return 0
    else:
        for x in non_zeroes:
            product *= x #Multiplies every number in non_zeroes together
        return product

#Divides all numbers in values. If the first number is 0, the result is 0 unless there are other 0s in the list.
def divide(values):
    quotient = values[0]
    if 0 in values[1:]: #Checks to see if any of the divisors will be 0
        sys.exit("Cannot divide by 0")
    elif values[0] == 0: #If the first value is 0 and all following values are non-zero, the result is always 0
        return 0
    else:
        for x in values[1:]: #Startiing at index one will prevent the quotient from getting divided by itself
            quotient /= x
        return quotient

#This function will randomly return one of the numbers in values.
def choose(values):
    random_num = random.choice(values)
    return random_num