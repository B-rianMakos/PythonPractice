def two_length_run():
    '''
    (list) --> Bool
    Precondtion: Must input a list of integers
    Functions that returns True if two consecutive numbers are the same, False otherwise
    '''
    

    list1 = input("Please input a list of numbers separated by space: ").strip().split()
    
    answer = False

    for x in range(len(list1)-1):
        if list1[x] == list1[x+1]:
            answer = True
        else:
            answer = answer
    print(answer)
    return answer
two_length_run()
