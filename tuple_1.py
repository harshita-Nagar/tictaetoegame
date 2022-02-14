# for creating all possible combinations from tuple_1 and tuple_2 we will use chain and product module.
from itertools import chain,product
tuple1=(2,3)
tuple2=(6,7)
comb=list(chain(product(tuple1,tuple2),product(tuple2,tuple1)))
print(str(comb))


test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k=1
comb_1=list(filter(lambda x:len(x)!=k,test_list))
print(comb_1)

comb_2=[ele for ele in test_list if len(ele)!=k]
print(str(comb_2))

# remove none values
test_list_1 = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
comb_3=[sub for sub in test_list_1 if not all(elem==None for elem in sub)]
print(str(comb_3))

comb_4=list[filter(lambda sub: not all(eleme==None for eleme in sub),test_list_1)]
print(str(comb_4))

