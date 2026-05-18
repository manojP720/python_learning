import math
def cal_mean(num):
    return sum(num)/len(num)
def cal_variance(num):
    v = sum((x-mean)**2 for x in num )/ len(num)
    return v
def cal_varience(variance):
    return math.sqrt(variance)

