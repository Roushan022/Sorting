def InsertionSort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
a=[23,45,67,89,90]
print(InsertionSort(a))
