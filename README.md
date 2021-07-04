###### Program works now, the code is commented so it should be easy to understand how it works.

# List Shift
Shifts a list over to the right or to the left.

So if you input `print(listShift([0, 1, 2, 3], 2))` at the end of the program it would output `[2, 3, 0, 1]`.
It works with str, int, bool, float, anything, really. (Feel free to test it out!

You can also input negative numbers like `print(listShift(['this', 'list', 'is', 'getting', 0.1, True, 'shifted', 1], -3))`, it should output `['getting', 0.1, True, 'shifted', 1, 'this', 'list', 'is']`

And if you enter something that is not an integer (how dare you?!) then it would return `"Sorry, it appears you have entered something other than an integer for the value 'shift'.\nPlease try again."`.

(Oh yeah and an input of 0 should output the original list)
