#/usr/bin/ptython

w=[3,2,4,6]
v=[3,5,2,4]
threadhold=7

def sum(a):
    sum=0;
    for i in range(len(a)):
        sum=sum+a[i]
    return sum

print sum(w)
bag=[];
for i in range(len(w)):
    bag.append(w[i])




