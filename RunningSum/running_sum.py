def running_sum (l):
    if len(l) == 0:
        return []
    current_sum = 0
    result_list = []

    for num in l:
        current_sum += num
        result_list.append(current_sum)

    return result_list
