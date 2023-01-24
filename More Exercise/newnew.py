def get_tasks(f):
    """
    returns List of List[str, int, int]; return the task
    information stored in f.
    """
    lst = []
    lstinlst = []

    
    newx = f.split(",")
    s = newx.strip().lower()
    for y in s:
        if y == "":
            pass
        elif y == " ":  
            lstinlst.append(s)
        else:
            lstinlst.append(s)
            
    if lstinlst == []:
         pass
        
    else:
          lst.append(lstinlst)
    lstinlst = []
    return lst
