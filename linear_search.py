def linear_search(arr, target):
    """
    Perform a linear search on the given array for the target element.
    
    Parameters:
    arr (list): The list in which to search for the target element.
    target (any): The element to search for in the list.
    
    Returns:
    int: The index of the target element if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    database = ["item1", "item2", "item3", "item4", "item5"]
    target_item = "item3"
    index = linear_search(database, target_item)
    
    if index != -1:
        print(f"Item '{target_item}' found at index {index}.")
    else:
        print(f"Item '{target_item}' not found in the database.")
