## Author: Shaan Barkat
## I have all of the different text files already set up below, just uncomment the ones that need to be checked!
counter = 0 
def mergeSort(arr):
    global counter
    # using recursion, so, use of a global counter is needed or else counter would be out of range
    if len(arr)>1:
        counter+=1
        middle = len(arr)//2#check middle of array
        lefth = arr[:middle]#check left of array
        righth = arr[middle:]#check right of array

        mergeSort(lefth)#merge the left side as well as sort it
        mergeSort(righth)#merge the right side as well as sort it

        x=0
        y=0
        z=0
        while x < len(lefth) and y < len(righth):
            if lefth[x] < righth[y]:
                arr[z]=lefth[x]
                x=x+1
                counter+=1
              
            else:
                arr[z]=righth[y]
                y=y+1
                counter+=1
            z=z+1

        while x < len(lefth):
            arr[z]=lefth[x]
            x=x+1
            z=z+1
            counter+=1
            
        while y < len(righth):
            arr[z]=righth[y]
            y=y+1
            z=z+1
            counter+=1

with open('10_Random.txt') as my_file:
    array1 = my_file.readlines()
##
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
##   array7 = my_file.readlines()
##
##with open('1000_Reverse.txt') as my_file:
##    array8 = my_file.readlines()
##
##with open('1000_Sorted.txt') as my_file:
##    array9 = my_file.readlines()

mergeSort(array1)
#mergeSort(array2)
##mergeSort(array3)
##mergeSort(array4)
##mergeSort(array5)
##mergeSort(array6)
##mergeSort(array7)
##mergeSort(array8)
##mergeSort(array9)

print("This is 10 Random Numbers sorted using mergeSort. The number of comparisons are: {} ".format(counter))
print(array1)
print('------------------------------------------------------------------------')
##print("This is 10 Numbers in Reverse Order, that is sorted using mergeSort. The number of comparisons are: {} ".format(counter))
##print(array2)
##print('------------------------------------------------------------------------')
##print("This is 10 Sorted Numbers sorted using mergeSort. The number of comparisons are: {} ".format(counter))
##print(array3)
##print('------------------------------------------------------------------------')
##print("This is 100 Random Numbers sorted using mergeSort. The number of comparisons are: {} ".format(counter))
##print(array4)
##print('------------------------------------------------------------------------')
##print("This is 100 Numbers in Reverse Order, that is sorted using mergesort. The number of comparisons are: {} ".format(counter))
##print(array5)
##print('------------------------------------------------------------------------')
##print("This is 100 Sorted Numbers sorted using mergesort. The number of comparisons are: {} ".format(counter))
##print(array6)
##print('------------------------------------------------------------------------')
##print("This is 1000 Random Numbers sorted using mergeSort. The number of comparisons are: {} ".format(counter))
##print(array7)
##print('------------------------------------------------------------------------')
##print("This is 1000 Numbers in Reverse Order, that is sorted using mergeSort. The number of comparisons are: {} ".format(counter))
##print(array8)
##print('------------------------------------------------------------------------')
##print("This is 1000 Sorted Numbers sorted using mergeSort. The number of comparisons are: {} ".format(counter))
##print(array9)


