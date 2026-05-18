import math
def cal_mean(num):
    return sum(num)/len(num)
def cal_variance(num, mean):
    v = sum((x-mean)**2 for x in num )/ len(num)
    return v
def cal_std_deviation(variance):
    return math.sqrt(variance)

num = int(input("Enter the number of elements:  "))
num = []
for i in range(num):
    num1 = float (input("enter the number:     " ))
    num.append(num1)
mean = cal_mean(num)
variance = cal_variance(num, mean)
d = cal_std_deviation(variance)
print("Mean: ", mean)   
print("Variance: ", variance)
print("Standard Deviation: ", d)


