def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

nlist = [155,6536,1653,2267,56527,42211,4652,25411,702854]
insertionSort(nlist)
print(nlist)
