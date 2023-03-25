#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    cumm_list = []
    sum_b = 0
    for a, b in my_list:
        cumm_list.append(a*b)
        sum_b += b
    cumm_sum = sum(cumm_list)
    weightavg = cumm_sum/sum_b
    return weightavg
