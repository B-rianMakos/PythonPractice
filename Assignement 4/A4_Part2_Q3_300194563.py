#Family Name : Brian Makos
#Student number : 300194563
#Class : ITI 1100
#Assigment 4 part 2
#Year 2020

##############
# Question 3
##############

def longest_run():
    '''
    (list) ---> int
    Precondtions: Must input a list of integers
    Function that returns the lenght of the highest  
    '''
    n = input("Please input a list of numbers seperated by a space: ").split()
    zero = 0
    count = 0
    new = 0
    for x in range(len(n)-1):

        if float(n[x][0]) == float(n[x+1][0]):
            count = count+1
            
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
    return new
    
longest_run()



