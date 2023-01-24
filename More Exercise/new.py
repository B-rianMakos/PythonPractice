def get_tasks():
    """
    returns List of List[str, int, int]; return the task
    information stored in f.
    """
    f = [["  very important meeting  ",1200,1300]["bal",1400,1500]["movie date",1700,1800]]
    lst = []
    lstinlst = []
    for x in range(len(f)):
        print(x)
        for y in x:
            s = y.strip().lower()
            if s == "":
                pass
            elif s== " ":  
                lstinlst.append(s)
            else:
                lstinlst.append(s)
            s = ""
        if lstinlst == []:
            pass
        
        else:
            lst.append(lstinlst)
        lstinlst = []
    return lst
