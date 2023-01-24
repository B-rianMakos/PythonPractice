def order_tasks(tasks):

    lst = []
    num = 0
    series = []

    

    for x in tasks:
        series.append[x[0]]

    for x in range(len(sorted(series))-1):
        if series[x] == series[x+1]:
            series.remove(x)
    
    for x in tasks:
        for y in series:
            if x[0] == y:
                lst.append(x)  


    return lst
            
