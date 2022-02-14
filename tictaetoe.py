t = 0
a = []

while True:
 k = input("Numbers please:")
 len_k=len(k)
 if len_k!=9:
    print("Please enter 9 character")

 else:

  break


for i in range(3):
    p=[]
    for j in range(3):
        p.append(k[t])
        t=t+1
    a.append(p)
print(a)

def conditions(p1,p2,p3):
    p=(('x' == p1) and ('x' == p2) and ('x' == p3))
    return p


con_1= conditions(a[0][0],a[1][0],a[2][0])
con_2=conditions(a[0][0],a[0][1],a[0][2])
con_3=conditions(a[0][2], a[1][2],a[2][2])
con_4=conditions(a[2][0],a[2][1],a[2][2])
con_5=conditions(a[0][1], a[1][1],a[2][1])
con_6=conditions(a[1][0],a[1][1],a[1][2])
con_7=conditions(a[0][0],a[1][1],a[2][2])
con_8=conditions(a[0][2],a[1][1],a[2][0])
# firstCondition = (('x' == a[0][0]) and ('x' == a[1][0]) and ('x' == a[2][0]));
# secondCondition = (('x' == a[0][0]) and ('x' == a[0][1]) and ('x' == 0][2]));
# thirdCondition = (('x' == a[0][2]) and ('x' == a[1][2]) and ('x' == a[2][2]));
# fourthCondition = (('x' == a[2][0]) and ('x' == a[2][1]) and ('x' == a[2][2]));
# fifthCondition = (('x' == a[0][1]) and ('x' == a[1][1]) and ('x' == a[2][1]));
# sixthCondition = (('x' == a[1][0]) and ('x' == a[1][1]) and ('x' == a[1][2]));
# seventhCondition = (('x' == a[0][0]) and ('x' == a[1][1]) and ('x' == a[2][2]));
# eighthCondition = (('x' == a[0][2]) and ('x' == a[1][1]) and ('x' == a[2][0]));
result=con_1 or con_2 or con_3 or con_4 or con_5 or con_6 \
       or con_7 or con_8


if result:
  print("Ok")
else:
    print("Not ok")







