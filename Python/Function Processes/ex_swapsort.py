def swapSort(list):
    currentIndex=0
    while currentIndex<len(list):
        smallest = list[-1]
        smallestIndex=len(list)-1
        for i in range(currentIndex, len(list)):
            if list[i] < smallest:
                smallest=list[i]
                smallestIndex=i
        list[smallestIndex],list[currentIndex]=list[currentIndex],list[smallestIndex]
        currentIndex+=1
    return(list)
preSort = [-100,0,0,5,-9,43,-2,7,-99]
print(swapSort(preSort))


