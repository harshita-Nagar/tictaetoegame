# list comprehension
l=[]
for i in range(10):
    if i%3==0:
        l.append(i)

print(l)

l=[i for i in range(100) if i%3==0]
print(l)

# dict comprehension
dic={i:f"iten{i}" for i in range(100)}
print(dic)