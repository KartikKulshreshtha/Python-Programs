#Author = Kartik Kulshreshtha
#Purpose = Practicing of Python
#Date = 20/01/2021

N = 6
a = int(input("Enter the number a : \n"))
b = int(input("Enter the number b : \n"))

count = 0

print("Player 1:\n")
print(f"Please guess the number between {a} to {b}\n")
while True:
    Number = int(input(f'Guess the Number please : \n'))
    if Number == N:
        print("Congrats You guess the correct number\n")
        break
    elif Number <= 10 and Number > a:
        print(f"You are very close to the number ...please guess between {a} to 10\n")
    elif Number > b:
        print(f"You cross the range of {b}. So you are dissqualified\n")
        break
    elif Number <= b and Number >= 10:
        print(f"You are too far to the number\n")
    else:
        print("You entered the invalied number")

    count = count+1

print(f"You Guess the correct number in {count} times...\n")

Count = 0
print("Player 2:\n")
print(f"Please guess the number between {a} to {b}\n")
while True:
    Number = int(input(f'Guess the Number please : \n'))
    if Number == N:
        print("Congrats You guess the correct number\n")
        break
    elif Number <= 10 and Number > a:
        print(f"You are very close to the number ...please guess between {a} to 10\n")
    elif Number > b:
        print(f"You cross the range of {b}. So you are dissqualified\n")
        break
    elif Number <= b and Number >= 10:
        print(f"You are too far to the number\n")
    else:
        print("You entered the invalied number")

    Count = Count+1

print(f"You Guess the correct number in {Count} times...")


if Count > count:
    print(f"Player 2 Won the game because he guessed the number in {Count} time and Player 1 guessed the number in {count} time")
elif Count == count:
    print(f"The game is tied because Player 1 and Player 2 both guessed the number in same times")
else:
    print(f'Player 1 Won the game because he guessed the number in {count} time and Player 1 guessed the number in {Count} time')



