def QuickSort(InputArray,Count):
    if len(InputArray)==1 or len(InputArray)==0:
        return InputArray,Count
    InputArray[0],InputArray[len(InputArray)-1]=InputArray[len(InputArray)-1],InputArray[0]
    i=0
    j=1
    while j<len(InputArray):
        Count+=1
        if InputArray[j]<InputArray[0]:
            InputArray[j],InputArray[i+1]=InputArray[i+1],InputArray[j]
            i+=1
            j+=1
        else:
            j+=1
    InputArray[0],InputArray[i]=InputArray[i],InputArray[0]
    InputArray[:i],Count=QuickSort(InputArray[:i],Count)
    InputArray[i+1:],Count=QuickSort(InputArray[i+1:],Count)
    return InputArray,Count
    

