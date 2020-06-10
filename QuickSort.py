## Author: Shaan Barkat
## I have all of the different text files already set up below, just uncomment the ones that need to be checked!
counter = 0
def quickSort(arr):
   Help(arr,0,len(arr)-1)

def Help(arr,start,end):
   if start<end:

       partpoint = partition(arr,start,end)

       Help(arr,start,partpoint-1)
       Help(arr,partpoint+1,end)


def partition(arr,start,end):
   global counter
   val = arr[start]

   leftm = start+1
   rightm = end

   fin = False
   while not fin:

       while leftm <= rightm and arr[leftm] <= val:
           leftm = leftm + 1
           counter+=1


       while arr[rightm] >= val and rightm >= leftm:
           rightm = rightm -1
           counter+=1
           

       if rightm < leftm:
           fin = True
           counter+=1
           
       else:
           newa = arr[leftm]
           arr[leftm] = arr[rightm]
           arr[rightm] = newa
           counter+=1
           

   newa = arr[start]
   arr[start] = arr[rightm]
   arr[rightm] = newa
   
   return rightm
   

with open('10_Random.txt') as my_file:
    array1 = my_file.readlines()
##
##with open('10_Reverse.txt') as my_file:
##    array2 = my_file.readlines()

##with open('10_Sorted.txt') as my_file:
##    array3 = my_file.readlines()

##with open('100_Random.txt') as my_file:
##    array4 = my_file.readlines()

##with open('100_Reverse.txt') as my_file:
##    array5 = my_file.readlines()

##with open('100_Sorted.txt') as my_file:
##    array6 = my_file.readlines()

##with open('1000_Random.txt') as my_file:
##    array7 = my_file.readlines()

##with open('1000_Reverse.txt') as my_file:
##    array8 = my_file.readlines()

##with open('1000_Sorted.txt') as my_file:
##    array9 = my_file.readlines()
    
    
quickSort(array1)
##quickSort(array2)
##quickSort(array3)
##quickSort(array4)
##quickSort(array5)
##quickSort(array6)
##quickSort(array7)
##quickSort(array8)
##quickSort(array9)

print("This is 10 Random Numbers sorted using quickSort. The number of comparisons are: {} ".format(counter))
print(array1)
print('------------------------------------------------------------------------')
##print("This is 10 Numbers in Reverse Order, that is sorted using quickSort. The number of comparisons are: {} ".format(counter))
##print(array2)
##print('------------------------------------------------------------------------')
##print("This is 10 Sorted Numbers sorted using quickSort. The number of comparisons are: {} ".format(counter))
##print(array3)
##print('------------------------------------------------------------------------')
##print("This is 100 Random Numbers sorted using quickSort. The number of comparisons are: {} ".format(counter))
##print(array4)
##print('------------------------------------------------------------------------')
##print("This is 100 Numbers in Reverse Order, that is sorted using quicksort. The number of comparisons are: {} ".format(counter))
##print(array5)
##print('------------------------------------------------------------------------')
##print("This is 100 Sorted Numbers sorted using quicksort. The number of comparisons are: {} ".format(counter))
##print(array6)
##print('------------------------------------------------------------------------')
##print("This is 1000 Random Numbers sorted using quickSort. The number of comparisons are: {} ".format(counter))
##print(array7)
##print('------------------------------------------------------------------------')
##print("This is 1000 Numbers in Reverse Order, that is sorted using quickSort. The number of comparisons are: {} ".format(counter))
##print(array8)
##print('------------------------------------------------------------------------')
##print("This is 1000 Sorted Numbers sorted using quickSort. The number of comparisons are: {} ".format(counter))
##print(array9)
