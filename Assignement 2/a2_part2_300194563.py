# Family name: Brian Makos
# Student number 300194563
# Course: IT1 1120
# Assignment number 2
#Year: 2020


#Question 1

def min_enclosing_rectangle(radius, x, y):
    '''
    (num, num, num) --> (num,num)
    Precondtion: must input numbers
    Function that returns the bottom left coordinates of a the smallest possible square containing a circle 
    '''
    coordx = x - radius
    coordy = y - radius
    if radius <=0 :
        return 

    else :
        return(coordx, coordy)

#Question 2

def vote_percentage(results):
    '''
    (string) --> float
    Precondtion: Only input one string containing all the "yes", "no" or "abstained" votes
    Function that returns the percentage of yes votes
    '''
    subyes = "yes"
    tyes = results.count(subyes)
    subno = "no"
    tno = results.count(subno)
    return (tyes/(tno + tyes))

#Question 3
def vote():
    '''
    (none) -- > string
    precondition: Only input one string containing all the "yes", "no" or "abstained" votes
    Fucntion that takes the total votes and determines if the proposal passes unanimously, with super majority or a simple majority
    '''
    results = input("Please input all the yes, no and abstained votes in this following box: ")
    final = vote_percentage(results)
    if final == 1 :
        print("proposal passes unanimously")
    elif final >= (2/3) and final < 1:
        print("proposal passes with super majority")
    elif final >=(1/2) and final < (2/3) :
        print("proposal passes with simple majority")
    else :
        print("proposal fails")
