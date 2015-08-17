def SortCount(input_array):
    if len(input_array) > 1:
        lower_part = SortCount(input_array[:len(input_array)//2])
        upper_part = SortCount(input_array[len(input_array)//2:])
        merge_part = MergeCount(lower_part,upper_part)
        return merge_part
    else:
        return input_array


def MergeCount(lower_part,upper_part):
    merge_result = []
    while lower_part and upper_part:
        if lower_part[0] <= upper_part[0]:
            merge_result.append(lower_part.pop(0))
        else:
            merge_result.append(upper_part.pop(0))
    merge_result  += lower_part + upper_part
    return merge_result
