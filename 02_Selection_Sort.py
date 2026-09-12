def SelectonSort(a):
    n=len(a)
    for i in range(n):
        for j in range(i,n-1):
            min=i
            if a[min]>a[j]:
                min=j
                a[i],a[min]=a[min],a[i]
    return a
b=[23,5,65,89,67,1,23,4]
print(SelectonSort(b))
