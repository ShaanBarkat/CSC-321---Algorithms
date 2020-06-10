## Author: Shaan Barkat
## I have all of the different text files already set up below, just uncomment the ones that need to be checked!
def insertionSort(arr):
   count = 0
   for inf in range(1,len(arr)):

     currval = arr[inf]
     p = inf

     while p>0 and arr[p-1]>currval:
         arr[p]=arr[p-1]
         p = p-1
         count+=1

     arr[p]=currval

   print("{} comparisons made!".format(count))
     
with open('10_Random.txt') as my_file:
   array1 = my_file.readlines()

##with open('10_Reverse.txt') as my_file:
##   array2 = my_file.readlines()
##
##with open('10_Sorted.txt') as my_file:
##    array3 = my_file.readlines()
##
##with open('100_Random.txt') as my_file:
##    array4 = my_file.readlines()
##
##with open('100_Reverse.txt') as my_file:
##    array5 = my_file.readlines()
##
##with open('100_Sorted.txt') as my_file:
##    array6 = my_file.readlines()
##
##with open('1000_Random.txt') as my_file:
##    array7 = my_file.readlines()
##
##with open('1000_Reverse.txt') as my_file:
##    array8 = my_file.readlines()
##
##with open('1000_Sorted.txt') as my_file:
##    array9 = my_file.readlines()
    
    
insertionSort(array1)
##insertionSort(array2)
##insertionSort(array3)
##insertionSort(array4)
##insertionSort(array5)
##insertionSort(array6)
##insertionSort(array7)
##insertionSort(array8)
##insertionSort(array9)

print("This is 10 Random Numbers sorted using InsetionSort.")
print(array1)
print('------------------------------------------------------------------------')
##print("This is 10 Numbers in Reverse Order, that is sorted using InsetionSort.")
##print(array2)
##print('------------------------------------------------------------------------')
##print("This is 10 Sorted Numbers sorted using InsetionSort.")
##print(array3)
##print('------------------------------------------------------------------------')
##print("This is 100 Random Numbers sorted using InsetionSort.")
##print(array4)
##print('------------------------------------------------------------------------')
##print("This is 100 Numbers in Reverse Order.")
##print(array5)
##print('------------------------------------------------------------------------')
##print("This is 100 Sorted Numbers sorted using InsetionSort.")
##print(array6)
##print('------------------------------------------------------------------------')
##print("This is 1000 Random Numbers sorted using InsetionSort.")
##print(array7)
##print('------------------------------------------------------------------------')
##print("This is 1000 Numbers in Reverse Order.")
##print(array8)
##print('------------------------------------------------------------------------')
##print("This is 1000 Sorted Numbers sorted using InsetionSort.")
##print(array9)


