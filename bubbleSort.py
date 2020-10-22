def bubble_Sort(array): 
    m = len(array) 
    for i in range(m-1):   
        for j in range(0, m-i-1): 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 
                
                
array = [30, 38, 14, 1, 40, 99, 9,54,87] 
bubble_Sort(array) 
  
print ("Sorted arrayay using bubble sort:") 
for i in range(len(array)): 
    print ("%d" %array[i]),  
