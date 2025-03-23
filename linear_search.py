# Linear Search using recursion

def linear_search(arr, target):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    if len(arr) == 0:
        return False
        
    if arr[0] == target:
        return True
    return linear_search(arr[1:], target)


# Linear search using iteration
def linear_search(arr, target):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    
    for element in arr:
        if element == target:
            return True
    else:
        return False
    
