def listShift(lst, shift): # Simple list shifting program.
    if shift == 0:
        return lst
    for _ in range(shift):
        if shift < 0:
            lst.insert(-1, lst[0])
            lst.pop(0)
        else:
            lst.insert(0, lst[-1])
            lst.pop()
    return lst