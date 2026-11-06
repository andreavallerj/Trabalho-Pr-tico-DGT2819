def bubbleSort(array): 
    
    for i in range(len(array)):
        
        for j in range(0, len(array) - i - 1):
            
            if array[j] > array[j + 1]:

                temp = array[j]
                
                array[j] = array[j + 1]
                
                array[j + 1] = temp

array = [42, 12, 7, 89, 23, 1, 55, 34, 19, 90, 3, 15, 68, 77, 25]

print("Array original:", array)

bubbleSort(array)

print("Array com Bubble Sort:", array)