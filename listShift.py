def listShift(lst, shift): # Simple list shifting program.

    shift = int(shift) % len(lst) # So we won't have to torture the program with massive numbers.

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

yourLst = []
while True:
    yourLstLen = input("How long do you want your list? ")
    if yourLstLen.isnumeric(): break
    print("It appears you entered something other than a non-negative integer. Please try again.")

for _ in range(int(yourLstLen)):
    yourLstValue = input("Enter a list element: ")
    yourLst.append(yourLstValue)

while True:
    yourShift = input("Enter a shift value: ")
    isYourInt = True

    try: int(yourShift)
    except ValueError: isYourInt = False

    if isYourInt: break
    print("It appears you entered something other than an integer. Please try again.")

print(listShift(yourLst, yourShift))
