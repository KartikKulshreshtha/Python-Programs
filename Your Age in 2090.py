Age = int(input("Enter your Current Age"))

Year = int(input("And enter the current year"))

if Year>2025:
    print('You are not born yet!!!')
else:
    while Age <= 100:
        Year = Year + 1
        Age = Age + 1
print(f"You get the age of 100 years in the year : {Year}")
