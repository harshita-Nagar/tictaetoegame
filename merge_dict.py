# merging two dictionaries
class Merge_dict:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def merge(self):
        self.y.update(self.x)
        print(self.x)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
M=Merge_dict(dict1,dict2)
K=M.merge()
print(K)
print(dict2)