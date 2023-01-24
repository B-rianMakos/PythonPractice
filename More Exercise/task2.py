def get_task_information(tasks, task_name):


    lst = []
    lstinlst = []
    for x in tasks:
        if x[0] == task_name:
            lstinlst.append(x)
        else:
            pass

    return lstinlst

