def quick_sort(new_list):

    if len(new_list) <= 1:
        return new_list
        
    ref = new_list[0]

    equal_ref = []
    greater_ref = []
    less_ref = []

    for num in new_list:
        if num == ref:
            equal_ref.append(num)
        elif num > ref:
            greater_ref.append(num)
        else:
            less_ref.append(num)

    less_ref = quick_sort(less_ref)
    greater_ref = quick_sort(greater_ref)

    new_list = less_ref + equal_ref + greater_ref
    return new_list