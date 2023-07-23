def square_root(x):
    if x < 0:
        return -1
    elif x == 0 or x == 1:
        return x
    else:
        estimate = x/2
        while abs(estimate*estimate - x) > 0.01:
            estimate = (estimate + (x/estimate))/2
        return estimate

number = input("Enter a number: ")
number = int(number)
result = square_root(number)
if result == -1:
    print("Cannot compute square root of a negative number")
else:
    print("The square foot of ", number, " is ", result)