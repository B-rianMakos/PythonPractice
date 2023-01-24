def get_tasks(f):
    """
    returns List of List[str, int, int]; return the task
    information stored in f.
    """
    lst = []
    lstinlst = []
    for x in f:
        
        s = x.strip().lower()
        if s == "":
            pass
        elif s == " ":  
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
