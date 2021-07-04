def listShift(lst, shift): # Simple list shifting program.

    shift = int(shift) % len(lst) # So we won't have to torture the program with massive numbers.

    # To check if shift is an integer (we already checked outside the program in a loop, but this is in case someone runs it without a loop.)
    isInt = True
    try:
        int(shift)
    except ValueError:
        isInt = False
    # Error message.
    if not isInt:
        print("Sorry, it appears you have entered something other than an integer for the value 'shift'.\nPlease try again.")
    
    else: # continue
        # No need to do anything is shift is 0
        if shift == 0: return lst

        # Algorithm to shift over and insert shifted over elements
        for _ in range(shift):
            if shift < 0:
                lst.insert(-1, lst[0])
                lst.pop(0)
            else:
                lst.insert(0, lst[-1])
                lst.pop()
        
        # Return the list- we are now done.
        return lst

# Empty list so that it is defined.
yourLst = []

# Take an input to see how long we want our list is (in an infinite loop)
while True:
    yourLstLen = input("How long do you want your list? ")
    # If it follows the criteria, break out of loop.
    if yourLstLen.isnumeric(): break
    # Otherwise give an error message.
    print("It appears you entered something other than a non-negative integer. Please try again.")

# Append list elements into the list.
for _ in range(int(yourLstLen)):
    yourLstValue = input("Enter a list element: ")
    yourLst.append(yourLstValue)

# Infinite loop to get value of shift.
while True:
    yourShift = input("Enter a shift value: ")
    isYourInt = True

    # Try except to check if it is an integer.
    try: int(yourShift)
    except ValueError: isYourInt = False

    # If it is an integer, we can break out of the loop
    if isYourInt: break
    # Otherwise send an error message and repeat.
    print("It appears you entered something other than an integer. Please try again.")

# Finally print out the results.
print(listShift(yourLst, yourShift))
