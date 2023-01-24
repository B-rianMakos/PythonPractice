def get_tasks(f):
    """
    returns List of List[str, int, int]; return the task
    information stored in f.
    """
    lst = []
    lstinlst = []
    y=""
    for x in f:
        y = y + x.strip().lower()

    newx = y.split(",")
    s = newx

    for w in s:
        if w == "":
            pass
        elif w == " ":  
            lstinlst.append(s)
        else:
            lstinlst.append(s)
            
    if lstinlst == []:
         pass
        
    else:
          lst.append(lstinlst)
    lstinlst = []
    return lst
