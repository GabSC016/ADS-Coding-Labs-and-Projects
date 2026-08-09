def selection_sort(num_list):
    list_length = len(num_list)
    current_index = 0
    while current_index < list_length:
        index_minimum = None
        value_minimum = num_list[current_index]
        for index in range(current_index,list_length):
            if value_minimum > num_list[index]:
                index_minimum = index
                value_minimum = num_list[index]
        if index_minimum == None:
            current_index += 1
        else:
            original_value = num_list[current_index]
            num_list[current_index] = value_minimum
            num_list[index_minimum] = original_value
            current_index += 1
    return num_list