def two_number_sum(array, target):
    numbers = {}
    for i in range(0, len(array)):
        current_number = array[i]
        numbers[target - current_number] = current_number
        current_numbers_key = numbers.get(current_number)
        if current_numbers_key and current_numbers_key != current_number:
            return [current_number, numbers.get(current_number)]
    return []
