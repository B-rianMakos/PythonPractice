






##############
# Question 3
##############
import math
def longest_run():

    n = input("Please input a list of numbers seperated by a space: ").split()
    zero = 0
    count = 0
    new = 0
    for x in range(len(n)-1):

        if float(n[x][0]) == float(n[x+1][0]):
            count = count+1
            new = count
            if new < count:
                new = count
            else:
                new = new
        elif float(n[x][0]) != float(n[x+1][0]):
            count = 0
    
    y = len(n)
    if  y == 0:
        new =new
    else:
        new = new +1

    print(new)
    
longest_run()

'''
import math
def longest_run():

    n = input("Please input a list of numbers seperated by a space: ").split()
    zero = 0
    count = 0
    new = 0
    for x in range(len(n)-1):

        if n[x][0] == n[x+1][0]:
            count = count+1
            new = count
            if new < count:
                new = count
            else:
                new = new
        elif n[x][0] != n[x+1][0]:
            count = 0
        else:
            new = new +1
    new = new +1     

    print(new)
  
longest_run()
'''
