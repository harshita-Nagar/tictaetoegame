# adjacent element multiplication
test_list=[2,3,8,9,5]
print("This is the original list:", str(test_list))
# res=tuple(i*j for i,j in zip(test_list,test_list[1:]))
# print(str(res))

# using lambda function 
res=tuple(map(lambda i,j:i*j, test_list[1:],test_list[:-1]))
print(str(res))