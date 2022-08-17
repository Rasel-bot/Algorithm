def selection_sort(L):
    for i in range(len(L)):
        min_indx = i
        
        for j in range(i+1, len(L)):
            if L[min_indx] > L[j]:
                min_indx = j
        L[i], L[min_indx] = L[min_indx], L[i] 
        
    return L
        
L = [5,4,6,9,2,1]
sort = selection_sort(L)
print(sort)