Year = int(input("And enter the current year"))
Age = int(input("Enter your Current Age"))



if Year>=2020:
    print('You are not born yet!!!')
    exit()

elif Age>=100:
    print("You seems like the oldest person")
    exit()
else:

    while Age <= 100:
        Year = Year + 1
        Age = Age + 1
print(f"You get the age of 100 years in the year : {Year}")
