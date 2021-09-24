#3rdrd Question Factorial
import math
def fact_of_fact(n):
    list1 = []
    list2 = []

    for i in range(n,0,-1):
        list1.append(i)
    for j in list1:
        list2.append(math.factorial(j))
    multi = 1
    for k in list2:
        multi = multi*k
    print("====",multi  )

    # for j in list2:

    
          

    print(list1)
    print(list2)
fact_of_fact(5)
fact_of_fact(6)

# #4th Questions Finding the combinations
from itertools import permutations
def mutations(x,y):
    perm = permutations([2, 3])
    for i in list(perm):
        print(i)
mutations(2,3)
def next_mutations(x,y,z):
    perm = permutations([3,7,4])
    for i in list(perm):
        print(i)
next_mutations(3,7,4)
def third_mutations(a,b,c,d):
    perm = permutations([2,3,4,5])
    for i in list(perm):
        print(i)
third_mutations(2,3,4,5)

# #2nd Question 
def multi(x,y):
    list = []
    for i in range(x,y):
        if (i%2) == 0:
            list.append(i)
    print(len(list))

        
multi(x = int(input("enter the number")),y = int(input("enter the number")))


# 5th sum 


def sum(a,b):
    print("add the two number",a+b)
    print("subract of the two number",a-b)
    print("divide of the two number", a*b)
    if b == 0:
        print(-1)
    else:
        print("divide of the two number", a//b)



sum(4,5)
# 1st sum
def binary(num):
    b_num = bin(num)
    b_list = list(b_num)
    b_list = b_list[2:]
    l = []
    for i in b_list:
        l.append(int(i))
        # print(l)
    length = len(l)
    count = 0
    res = 0
    for j in range(length):
        if l[j] == 1:
            count = 0 
        else:
            count = count + 1
            #print(count)
        res = max(res,count)
    print("000000",res)

bin(7526)

binary(7526)










    
    