print("Welcome Guys in this problem")
Limit = int(input("Enter the Limit of the list\n"))
#Here we initialize two emplty list
List = []
List1 = []
for i in range(Limit):
    Number = int(input("Enter the numbers in the list\n"))
    List.append(Number)

for i in range(len(List)):
    #Here we take the value of i in the temp variable
   temp = int(List[i])
   while 1:
       #Here we check that the value of temp is eaqual to its palindrome or not and greater than 10
       if str(temp) == str(temp)[::-1] and int(List[i])>10:
           List1.append(str(temp))
           break
       elif int(List[i])<10:
           List1.append(str(temp))
           break
       temp = temp+1
print(List1)
