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
    network=[]
    
    # YOUR CODE GOES HERE
    lst = []
    tup = []
    position = None 
     
    
    for x in friends: #find how to do 
        lst.append(x.split())

    


    
    for x in lst:
        if len(x) == 2:
            
      

            if x[0] != position:
                position = x[0]
                
                for item in tup:
                    network.append(item)

                #network.append(tup[0]) # make lst no longer a list by using for item in lst 
                #network.append(item)
                tup = []
                tup.append( (x[0], [x[1]] ) )


                for y in network:
                    for z in y[-1]:
                            if z == tup[0][0]:
                                tup[-1][-1].append(y[0])
                 
                    '''
                        for w in network:
                           if w[0] == z:
                           '''
                                


                
            elif x[0] == position:
                tup[-1][-1].append((x[1]))
            
        
            for item in lst:
                for x in network
                    if item[0] in x[0]
    
            
    print(sorted(network))    
    return sorted(network)

    #social has to be tuple (0, [])
    network.append(social)
