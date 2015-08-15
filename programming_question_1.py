def SortCount(input_array):
    if len(input_array) > 1:
        lower_part, count1 = SortCount(input_array[:len(input_array)//2])
        upper_part, count2 = SortCount(input_array[len(input_array)//2:])
        merge_part, count3 = MergeCount(lower_part,upper_part)
        return merge_part, count1+count2+count3
    else:
        return input_array, 0


def MergeCount(lower_part,upper_part):
    count = 0
    merge_result = []
    while lower_part and upper_part:
        if lower_part[0] <= upper_part[0]:
            merge_result.append(lower_part.pop(0))
        else:
            count += len(lower_part)
            merge_result.append(upper_part.pop(0))
    merge_result  += lower_part + upper_part
    return merge_result, count
