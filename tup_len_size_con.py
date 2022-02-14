# size and length of Tuples
import sys
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

# print the sizes of sample Tuples
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")
print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")
print(str(Tuple3.__sizeof__()))

print("size of tuple3 is:", sys.getsizeof(Tuple3),"bytes")  # another method to find size

print(len(Tuple1))
print(len(Tuple2))
print(len(Tuple3))

# converting tuple to string
t=("hi","friends")
st=" ".join(t)
print(st)
print(type(st))

# Python program to Convert Tuple String to
# Integer Tuple using eval() method

tup_str="(1,4,6,9)"
print("The string tuple is:", tup_str)
int_tup=eval(tup_str)
print("The integer tuple is:", int_tup)

# Python program to clear Tuple elements
Tuple_1=(2,5,7,4)
print("This is my tuple:", Tuple_1)
con_list=list(Tuple_1)
con_list.clear()
empty_tuple=tuple(con_list)
print("This is an empty tuple:", empty_tuple)



