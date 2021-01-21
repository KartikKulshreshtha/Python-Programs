import random

def Jumble_Words(First_name,Last_name,Number):
    for i in range(0, Number):
        # Changing the last name
        joumbled_name = First_name[i] + " " + Last_name[random.randint(0, Number - 1)]
        print(joumbled_name)


if __name__ == '__main__':
    Number = int(input("Enter the Number of your friends:\n"))
    Name_List = []
    First_name = []
    Last_name = []

    for i in range(1, Number + 1):
        name = input("Enter the name\n")
        Name_List.append(name)

    for ele in Name_List:
        Split_Name = ele.split(' ')
        First_name.append(Split_Name[0])
        Last_name.append(Split_Name[1])

    Jumble_Words(First_name,Last_name,Number)