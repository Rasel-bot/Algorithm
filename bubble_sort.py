def bubble_sort(L):
    print("unsorted:", L)
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                print(L)
            else:
                print(L)
        print()
    return L    
        
L = [5,4,6,9,2,1]
sort = bubble_sort(L)
print("sorted:", sort)