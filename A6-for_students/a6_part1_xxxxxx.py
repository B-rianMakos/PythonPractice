import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE


    file_name = None

    
    while file_name == None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
    
    return file_name 


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE

    file = open(file_name).read()
    print(file)
    dict1 = {}
    lines = file.split()
    words = lines.split()

    file.split()
    
    num = ["1","2","3","4","5","6","7","8","9","0"]
    text = ""

    for x in file:
        if x not in num:
            text.append(x)
    
    
    for x in file:
        if x not in dict1:
            dict1.append(x)



def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    pass
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

