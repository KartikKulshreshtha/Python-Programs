while True:
    try:
        n = int(input("Enter the number of the apple harry got"))
        mn = int(input("Enter the minimum range"))
        mx = int(input("Enter the maximum range"))
    except Exception as e:
        print("You entered a invalid number")
        exit()

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

    break



