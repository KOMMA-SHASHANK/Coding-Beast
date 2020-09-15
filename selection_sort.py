k=[]
n=int(input('enter range'))
for i in range(n):
    k.append(int(input('enter')))
print("before swapping",k)
for i in range(n-1):
    min=i
    
    for j in range(i+1,n):
        if(k[j]<k[min]):
            min=j
    temp=k[min]
    k[min]=k[i]
    k[i]=temp
print("after sorting",k)        

    