#Family Name : Brian Makos
#Student number : 300194563
#Class : ITI 1100
#Assigment 4 part 2
#Year 2020

def number_divisible():
    '''
    (list, int) ---> None
    Preconditions: Must input a list of integers and a interger, n
    Function that counts how many numbers in the list of integers are dividable by n
    '''
    list1 = input("Please input a list of integers separated by spaces: ").strip().split()
    n = int(input("Please input an integer: "))
    answer = []
    num = 0
    for x in list1:
        if int(x)%n == 0:
            answer.append(int(x))
    for x in range(len(answer)):
        num += 1
    print(f"The number of elements divisible by {n} is {num}")       

number_divisible()
