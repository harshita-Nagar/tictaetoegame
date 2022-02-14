mylist=[2,4,6,8]

#first method
# tuplelist=[]
# for val in mylist:
#   mytuple=(val,(val*val*val))
# tuplelist.append(mytuple)
# print("The list of tuple is:", str(tuplelist))

# second method
# short syntax and also called list comprehension
# tuplelist=[(val,(val*val*val)) for val in mylist]
# print(tuplelist)

#third method
# tuplelist=[(val,pow(val,3)) for val in mylist]
# print(tuplelist)

# joining a list and a tuple
# first method

mytup=(11,13,15)
# mylist+=mytup
# print(mylist)

# second method
newlist=tuple(list(mytup)+mylist)
print(str(newlist))


# joining two list

emp=("naveen","bharat")
comp=("apple","google")
zipped=set(zip(emp,comp))
# print(zipped)

for (a,b) in zipped:
    print(a,b)