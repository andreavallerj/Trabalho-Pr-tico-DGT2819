array = [42, 12, 7, 89, 23, 1, 55, 34, 19, 90, 3, 15, 68, 77, 25]


for i in range(len(array)):
    
    min_index = i
    
    for j in range(i+1, len(array)):
        
        if array[min_index] > array[j]:
            min_index = j
   
    array[i], array[min_index] = array[min_index], array[i]

print("Array ordenado com Selection Sort:", array)