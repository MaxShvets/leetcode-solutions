import json
import time
from collections import Counter
from typing import List, Tuple


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter = Counter(A[0:K])
        r = K - 1

        while r + 1 < len(A) and len(counter) < K:
            r += 1
            counter[A[r]] += 1

        if r == len(A):
            return 0

        result = 0

        l1 = 0
        l2 = 0
        short_counter = counter.copy()
        while len(short_counter) == K:
            short_counter[A[l2]] -= 1
            if short_counter[A[l2]] == 0:
                del short_counter[A[l2]]
            l2 += 1

        result += l2 - l1

        while r + 1 < len(A):
            r += 1

            if A[r] in short_counter:
                counter[A[r]] += 1
                short_counter[A[r]] += 1
            elif A[r] not in counter:
                short_counter[A[r]] += 1
                l1 = l2
                counter = short_counter.copy()
                while len(short_counter) == K:
                    short_counter[A[l2]] -= 1
                    if short_counter[A[l2]] == 0:
                        del short_counter[A[l2]]
                    l2 += 1
            elif A[r] in counter:
                counter[A[r]] += 1
                short_counter[A[r]] += 1
                while len(short_counter) == K:
                    short_counter[A[l2]] -= 1
                    if short_counter[A[l2]] == 0:
                        del short_counter[A[l2]]
                    l2 += 1

            result += l2 - l1

        return result


if __name__ == "__main__":
    solution = Solution()

    test_result = solution.subarraysWithKDistinct([2, 1, 2, 1, 1], 3)
    assert test_result == 0

    test_result = solution.subarraysWithKDistinct([1,2,1,2,3], 2)
    assert test_result == 7, test_result

    test_result = solution.subarraysWithKDistinct([2,2,1,2,2,2,1,1], 2)
    assert test_result == 23, test_result

    with open("k-elem-subarrays-test-case.json") as test_case_file:
        test_case = json.load(test_case_file)

    start_time = time.perf_counter()
    print(solution.subarraysWithKDistinct(test_case["array"], test_case["K"]))
    print(f"Took {time.perf_counter() - start_time}")
