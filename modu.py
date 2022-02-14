from operator import mod
# tup_1=(2,5,8,9)
# tup_2=(7,1,4,3)
# print("The original tuple 1 : " + str(tup_1))
# print("The original tuple 2 : " + str(tup_2))
#
# res = tuple(ele1 % ele2 for ele1, ele2 in zip(tup_1,tup_2))

# res=tuple(map(mod(,tup_1,tup_2)))
# print(str(res))

#  Update each element in tuple list
#  Using list comprehension

my_tup=[(3,4,5),(6,7,8),(1,9,7)]
print("This is original list:",str(my_tup))

add_ele=4
# res=[tuple(j + add_ele for j in sub) for sub in my_tup]
# print(str(res))

#  Update each element in tuple list
# using lambda method
res=[tuple(map(lambda ele:ele+add_ele,sub)) for sub in my_tup]
print(str(res))


# filter even number from a list

# def is_even(n):
#     return n%2==0
#
#
# num=[2,4,6,7,9,5,1]
# evens=list(filter(is_even,num))
# print(evens)

# filter even number from a list

# def is_odd(n):
#     return n%2==1
#
#
# num=[2,4,6,7,9,5,1]
# odds=tuple(filter(is_odd,num))
# print(odds)


# filter even numbers using lambda function
num=[2,4,6,7,9,5,1]
evens=list(filter(lambda n:n%2==0,num))
print(evens)

