def find_max(arr):
    if not arr:
        return None
 
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    
    return max_left if max_left > max_right else max_right


numbers = [3, 7, 1, 9, 4, 2]
print(find_max(numbers))