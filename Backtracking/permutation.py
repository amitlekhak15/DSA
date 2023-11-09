def permutation(i,rs,a):
    if(i==len(a)):
        rs.append(a[:])
        return
    for index in range(i,len(a)):
        a[i],a[index]=a[index],a[i]
        permutation(index+1,rs,a)
        a[i],a[index]=a[index],a[i]


a=[1,2,3]
rs=[]
permutation(0,rs,a)
print(rs)