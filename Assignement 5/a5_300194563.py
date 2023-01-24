#Family Name : Brian Makos
#Student number : 300194563
#Class : ITI 1100
#Assigment 5
#Year 2020



import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[" "]
    w = 0
    z = 0

    


    lst = []
    for x in friends: #Turns wordfile into ordered list 
        lst.append(x.split())
        
    for x in range(1,len(lst)): 
        condition1 = False
        condition2 = False
        social = int(lst[x][1])
        ID = int(lst[x][0])

        lenght = len(network)
        for y in range(lenght):
            if social == network[y][0]:
                condition1 = True
                z = y
            if ID == network[y][0]:
                condition2 = True
                w = y

        if condition1 == True:
            network[z][1].append(ID)
        else:
            network.append((social, [ID]))  
        if condition2 == True:
            network[w][1].append(social)
        else:
            network.append((ID,[social]))
        

    network.remove(network[0])

    
    return sorted(network)


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
        
    # YOUR CODE GOES HERE

    mutual1 = []
    mutual2 = []
        
    network = create_network(file_name)

    for x in range(len(network)):
        if network[x][0] == user1:
            mutual1.append(network[x][1])
    
    for y in range(len(network)):
        if network[y][0] == user2:
            mutual2.append(network[y][1])
   
    for x in mutual1[0]:
        if x in mutual2[0]:
            common.append(x)
    
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE

    userfriends = []
    usersfriendsfriends = []
    recommend = 0
    network = create_network(file_name)
    
    for x in range(len(network)):
        if network[x][0] == user:
            userfriends.append(network[x][1])

    for y in network:
        if y[0] in userfriends[0]:
            for z in y[1]:
                usersfriendsfriends.append(z)
    
    for x in usersfriendsfriends:
        if x == user:
            usersfriendsfriends.remove(x)

    z = 0
    while z < (len(usersfriendsfriends)):
        if usersfriendsfriends[z] in userfriends[0]:
            usersfriendsfriends.remove(usersfriendsfriends[z])
        else:
            z = z +1
    
    count = 0
    usersfriendsfriends.sort()

    for w in usersfriendsfriends:
        maximum = usersfriendsfriends.count(w)
        if maximum > count:
            count = maximum
            recommend = w
    if recommend == user:
        return None
    return recommend 
    
      
   
#if result of get common friend not in inital user friends friends 



def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    
    network = create_network(file_name)

    counter = 0
    total = 0
    for x in network:
        for y in range(len(x[1])):
            counter = counter +1
        if counter >= k:
            total = total +1
        counter = 0    
        
    return total

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE

    network = create_network(file_name)
    
    maxfriends = 0
    counter = 0

    for x in network:
        for y in range(len(x[1])):
            counter = counter +1

        if counter > maxfriends:
            maxfriends = counter

        counter = 0
    
    return maxfriends
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE

    network = create_network(file_name)
    maximum = maximum_num_friends(network)

    counter = 0
    
    for x in network:
        for y in range(len(x[1])):
            counter = counter +1

        if counter == maximum:
            max_friends.append(x[0])

        counter = 0

    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE

    network = create_network(file_name)
    total = 0
    counter = 0

    for x in network:
        total = total +1
        for y in range(len(x[1])):
            counter = counter +1
    
    average = counter/total

    return average

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    

    for x in network:
        if len(x[1]) == len(network) - 1:
            return True

    return False
            
'''    
    for x in network:
        everyone.append(x[0])


    for x in network:
        for y in x[1]:
            if y in everyone and x[0] in everyone:
                con1 = True
'''
    #return con1
####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    possible = []

    for x in network:
        possible.append(x[0])

    answer = None

    while answer == None:
        try:
            answer = int(input("Please enter and integer for a user ID: "))

            if answer not in possible:
                print("This user ID does not exist")
                answer = None
            
        except :
            print("That was not an integer. Please try again: ")
    
        
        
    return answer

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
