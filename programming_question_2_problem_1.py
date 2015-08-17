def QuickSort(InputArray):
    if len(InputArray)==1 or len(InputArray)==0:
        return InputArray
    i=0
    j=1
    while j<len(InputArray):
        if InputArray[j]<InputArray[0]:
            InputArray[j],InputArray[i+1]=InputArray[i+1],InputArray[j]
            i+=1
        j+=1
    InputArray[0],InputArray[i]=InputArray[i],InputArray[0]
    InputArray[:i]=QuickSort(InputArray[:i])
    InputArray[i+1:]=QuickSort(InputArray[i+1:])
    return InputArray




