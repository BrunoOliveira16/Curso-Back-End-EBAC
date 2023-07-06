def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):

        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] > unsorted_list[j+1]:

                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list