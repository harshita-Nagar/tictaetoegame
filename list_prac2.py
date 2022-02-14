# Python code to count the number of occurrences
# def countX(lst, x):
#     count = 0
#     for ele in lst:
#         if (ele == x):
#             count = count + 1
#         return count
#
# # Driver Code
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# print('{} has occurred {} times'.format(x, countX(lst, x)))


def count_x(lst,x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x=8
# print(format(x,count_x(lst,x)))

print('{} has occurred {} times'.format(x, count_x(lst, x)))












# # 1st method class for finding the occurrence of an element in a list
#
# class Count_element:
#     count=0
#     @staticmethod
#     def count_x(mylist, num):
#         for ele in mylist:
#             if ele==x:
#                 count=count+1
#         return count_x
#
#
# mylist=[3,4,6,3,4,8,9,9,7,5,6,7]
# x=4
# Count_element_obj=Count_element()
# K=Count_element_obj.count_x(mylist,x)
# print(K)
#
# # print("{} has occured {} times".format(x,count) )
#
# # 2nd method
# mylist_2=[4,4,6,8,9,1,2,4,5,6]
# x=6
# print("{} has occured {} times.".format(x,mylist_2.count(x)))
#
# # 3rd method
# from collections import Counter
# mylist_3=[2,5,7,5,6,8,7,1,3,2]
# x=7
# dic=Counter(mylist_3)
# print(dic)  # for occurrence of all the elements
# print("{} has occurred {} times".format(x, dic[x]))  # for occurrence of x
