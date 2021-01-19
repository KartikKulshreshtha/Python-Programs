try:
    print("Welcome to Coding's World...")
    Cases = int(input("Enter the number of test cases ..\n"))
except Exception as e:
    print("Please enter a number only")
    exit()
for i in range(Cases):
    Number = int(input(f"Enter the number of size {Cases}\n"))
    Number2 = Number
    while 1:
        Number = int(Number)
        Number = Number+1
        Number = str(Number)
        if Number == Number[::-1]:
            print(f"The next palindrome of {Number2} is {Number}")
            break