#!/usr/bin/python3
# function that adds all unique integers in a list (only once for each integer)
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)
    return sum
