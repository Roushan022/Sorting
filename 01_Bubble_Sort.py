def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
    return a
a=[78, 34, 56, 89, 12, 45, 67, 23, 90, 11,
               33, 77, 88, 44, 55, 66, 99, 100, 1, 2,
               3, 4, 5, 6, 7, 8, 9, 10, 13, 14,
               15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
               25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
print(bubble_sort(a))


