def are_overlapping(start1, end1, start2, end2):

    if end2 <= start1:
        if end1 >= start2:
            return True
        if end1 <= start2:
            return False

    

    elif end2 >= start1:
        if end1 >= start2:
            return True
        if end1 <= start2:
            return False
    else:
        return False

def is_free(start, end, tasks):

    for x in tasks:
        start1 = x[1]
        end1 = x[2]
        boolean = are_overlapping(start, end, start1, end1)
    return boolean
