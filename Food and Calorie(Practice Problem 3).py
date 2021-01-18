i = 1
x = []
while i <=3:
    Input = input("Enter the name of the food : ")
    x.append(Input)
    i = i +1


#Here we use reverse() to reverse the list.....
x.reverse()
print(x)

#Here we use Slicing to reverse the list.....

print(x[::-1])

if x.reverse() != x[::-1]:
    print("All the methods gives the same result....")
else:
    print("Some of the above methods gives the another output")
