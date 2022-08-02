def insertion_sort(L):
    print("unsorted:", L)
    for i in range(1,len(L)):
        current_element = L[i]
        
        while current_element < L[i-1] and i > 0:
            L[i] = L[i-1]
            i = i - 1
        L[i] = current_element
    return L

L = [5,4,6,9,2,1]
sort = insertion_sort(L)
print("sorted:",sort)         
         