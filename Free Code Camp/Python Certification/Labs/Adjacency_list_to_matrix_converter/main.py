def adjacency_list_to_matrix(dictionary):
    dictionary_len = len(dictionary)
    matrix = [[0]*dictionary_len for _ in range(dictionary_len)]
    
    for index in dictionary:
        for value in dictionary[index]:
            matrix[index][value] = 1

    for node in matrix:
        print(node)
    
    return matrix