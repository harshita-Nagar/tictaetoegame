# class ReverseList:
#     def rev_list(first):
#         first.reverse()
#         return first
#
#
# list_1=[2,7,8,9,1]
# r=ReverseList
# k=r.rev_list(list_1)
# print(k)



# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])
# a=[1,2,3,4,5]
# print(a[3:0:-1])


# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#
#     return v
# print(fun(data[0]))



class Conversion:
    @staticmethod
    def convert(arg):
        print (tuple(arg))


list_1=[34,54,89]
C=Conversion()
K=C.convert(list_1)
print(K)


class ConversionofSet:
    def convert_set(arg):
        print(set(arg))


list_2=[3,3,7,9,0]
Q=ConversionofSet
S=Q.convert_set(list_2)
print(S)