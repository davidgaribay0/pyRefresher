def is_valid_subsequence(array, sequence):
    j = 0
    sequence_length = len(sequence)
    for i in range(len(array)):
        if array[i] == sequence[j]:
            j += 1
        if j == sequence_length:
            return True
    return False
