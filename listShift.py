# If you want to see what happens if the program takes an invalid input,
# feel free to comment out/delete lines 34 to 43 and replace that with `yourShift = input("Enter an integer: ")`

def listShift(lst, shift): # Simple list shifting program.

    isInt = True
    try:
        int(shift)
    except ValueError:
        isInt = False
    
    if not isInt:
        print("Sorry, it appears you have entered something other than an integer for the value 'shift'.\nPlease try again.")
    
    else: # continue
        shift = int(shift)

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

while True:
    yourShift = input("Enter an integer: ")
    isYourInt = True
    try:
        int(yourShift)
    except ValueError:
        isYourInt = False
    
    if isYourInt:
        break

listShift(yourLst, yourShift)
