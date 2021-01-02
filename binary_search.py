from typing import List, Optional


def binary_search(array: List[int], target: int) -> Optional[int]:
    """
    :type array: sorted array
    :type target: target element

    :return None if the array contains the target element, the index of
    the first element greater than target if there is such an element,
    array length if all elements are smaller
    """
    start = 0
    end = len(array)

    while start <= end:
        middle = (start + end - 1) // 2

        if array[middle] == target:
            return None
        elif array[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return start


if __name__ == "__main__":
    assert binary_search([1, 2, 3], 2) is None
    assert binary_search([1, 2, 3, 5], 4) == 3
    assert binary_search([1, 2, 3], 4) == 3
    assert binary_search([1, 2, 3], 0) == 0
