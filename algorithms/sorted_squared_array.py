def sorted_squared_array(array):
    result = [0] * len(array)
    smaller_index = 0
    larger_index = len(array) - 1
    i = len(array) - 1
    while smaller_index <= larger_index:
        smaller_value = array[smaller_index]
        larger_value = array[larger_index]
        if abs(smaller_value) > abs(array[larger_index]):
            result[i] = smaller_value ** 2
            smaller_index += 1
        else:
            result[i] = larger_value ** 2
            larger_index -= 1
        i -= 1
    return result
