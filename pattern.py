num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

num_1=int(input("Enter the number:"))
for i in range(num_1):
    for j in range(num_1):
        print("#", end=" ")
    print()