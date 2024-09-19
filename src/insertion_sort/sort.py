def run_sort(unsorted_list: list[int]) -> list[int]:
    # Implement your function here ...
    for i in range(1, len(unsorted_list)):
        j = i-1
        key = unsorted_list[i]
        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
        unsorted_list[j+1] = key
    return unsorted_list