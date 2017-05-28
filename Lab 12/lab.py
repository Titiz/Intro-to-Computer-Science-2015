import random
import helpers

#
# Each of the following functions have an arbitrary return value. You
# job is to edit the functions to return the correct value. You'll
# know it's correct because when you run test.py, the program will
# print "passed."
#
# Any code you add outside of these functions (in the global
# namespace) should be commented out before running test.py
#

def exponentiate(base, power):
    if power == 0:
        return 1
    else:
        return base * exponentiate(base, power - 1)


def get_nth(list_of, n):
    if n == 0:
        return helpers.head(list_of)
    else:
        return get_nth(helpers.tail(list_of), n-1)



def reverse(list_of):
    if not list_of:
        return []
    return reverse(helpers.tail(list_of)) + [helpers.head(list_of)]




def is_older(date_1, date_2):
        if date_1 == [] and date_2 == []:
            return False
        elif helpers.head(date_1) < helpers.head(date_2):
            return True
        elif helpers.head(date_2) < helpers.head(date_1):
            return False
        else:
            return is_older(helpers.tail(date_1), helpers.tail(date_2))



def number_before_reaching_sum(total, numbers):
    if total <= 0:
        return -1
    else:
        return number_before_reaching_sum(total - helpers.head(numbers), helpers.tail(numbers)) + 1



def what_month(day):
    return number_before_reaching_sum(day, helpers.month_days()) + 1
        
