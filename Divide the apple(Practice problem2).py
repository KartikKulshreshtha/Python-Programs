n = int(input("Enter the numbers of the apple harry got : "))
mn = int(input("Enter the minimum range"))
mx = int(input("Enter the maximum range"))


if mn == mx:
    print("This is not a range and here mn is equal to mx")
else:

    while mn <= mx:
        if n % mn == 0:
            print(f"{mn} is divisible by {n}")
            mn = mn + 1
        else:
            print(f"{mn} is not divisible by {n}")
            mn = mn + 1



