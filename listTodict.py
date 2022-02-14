#Create a class
# Create two variable in class
# printList(list)
# CreateDicf()

# first method
list_1=["Pooja","Seema","Mona"]
list_2=[1,2,3,6]

print("This is my first list", str(list_1))
print("This is my first list", str(list_2))
# dict_new={}
# for key in list_1:
#     for val in list_2:
#         dict_new[key]=val
#         list_2.remove(val)
#         break

# print(str(dict_new))

# second method-list comprehension method
# dict_new={list_1[i]:list_2[i] for i in range(len(list_1))}
# print(str(dict_new))

# third method-zip method
dict_new=dict(zip(list_1,list_2))
print(str(dict_new))
