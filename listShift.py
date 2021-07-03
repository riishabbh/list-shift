# Right now, if you enter a shift value that is not an integer, it allows it but the function will say that you have entered something incorrect.
# By uncommenting (is that a word?) lines 25, 27, and 28, and indenting line 26, it will loop your input till you enter something that is allowed.

def listShift(lst, shift): # Simple list shifting program.

    if isinstance(shift, int): shift = int(shift)
    else: print("Sorry, it appears you have entered something other than an integer for the value 'shift'.\nPlease try again.")

    if shift == 0: return lst

    for _ in range(shift):
        if shift < 0:
            lst.insert(-1, lst[0])
            lst.pop(0)
        else:
            lst.insert(0, lst[-1])
            lst.pop()
    return lst

while True:
    yourLst = input("Enter a list: ")
    if isinstance(yourLst, list):
        break

# while True:
yourShift = input("Enter an integer: ")
    # if isinstance(yourShift, int):
        # break
