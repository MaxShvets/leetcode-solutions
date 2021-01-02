import pprint
from typing import List, Optional


class Solution:
    def binarySearchRow(
        self,
        matrix: List[List[int]],
        row_num: int,
        start: int,
        end: int,
        target: int,
    ) -> Optional[int]:
        """
        :type array: sorted array
        :type target: target element

        :return None if the array contains the target element, the index of
        the first element greater than target if there is such an element,
        array length if all elements are smaller
        """
        while start <= end:
            middle = (start + end) // 2
            element = matrix[row_num][middle]

            if element == target:
                return None
            elif element < target:
                start = middle + 1
            else:
                end = middle - 1

        return start

    def binarySearchColumn(
        self,
        matrix: List[List[int]],
        column_num: int,
        start: int,
        end: int,
        target: int,
    ) -> Optional[int]:
        """
        :type array: sorted array
        :type target: target element

        :return None if the array contains the target element, the index of
        the first element greater than target if there is such an element,
        array length if all elements are smaller
        """
        while start <= end:
            middle = (start + end) // 2
            element = matrix[middle][column_num]

            if element == target:
                return None
            elif element < target:
                start = middle + 1
            else:
                end = middle - 1

        return start

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        last_row = len(matrix) - 1
        column = len(matrix[0]) - 1

        while row <= last_row and 0 <= column:
            current_element = matrix[row][column]

            if current_element == target:
                return True
            elif current_element < target:
                row += 1
                row = self.binarySearchColumn(
                    matrix,
                    column,
                    row,
                    last_row,
                    target,
                )

                if row is None:
                    return True
            elif target < current_element:
                column -= 1
                column = self.binarySearchRow(
                    matrix,
                    row,
                    0,
                    column,
                    target,
                )

                if column is None:
                    return True
                else:
                    column -= 1

        return False


if __name__ == "__main__":
    matrix = [[-1, 3]]
    target = -1

    pprint.pprint(matrix)

    solution = Solution()
    print(solution.searchMatrix(matrix, target))
