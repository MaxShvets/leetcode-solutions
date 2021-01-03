import json
import time
from collections import Counter
from typing import List, Tuple


class Caterpillar:
    def __init__(self, list_: List[int], max_distinct_elements: int):
        self._list = list_
        self._max_distinct_elements = max_distinct_elements
        self._start = 0
        self._end = max_distinct_elements - 1
        self._counter = Counter(list_[self._start:self._end])

    @property
    def end(self) -> int:
        return self._end

    @property
    def num_distinct(self) -> int:
        return len(self._counter)

    def grow(self) -> Tuple[int, Counter]:
        while (
            len(self._counter) < self._max_distinct_elements
            and self._end < len(self._list)
        ):
            self._counter[self._list[self._end]] += 1
            self._end += 1

        while (
            self._end < len(self._list)
            and self._list[self._end] in self._counter
        ):
            self._counter[self._list[self._end]] += 1
            self._end += 1

        return self._end, self._counter

    def shrink(self) -> Tuple[int, Counter]:
        while self._max_distinct_elements <= len(self._counter):
            self._counter -= Counter([self._list[self._start]])
            self._start += 1

        return self._start, self._counter

    def count_good_subarrays(self) -> int:
        num_good_subarrays = 0
        counter = self._counter.copy()

        for i in range(self._start, self._end):
            sub_counter = counter.copy()
            j = self._end - 1

            while i <= j and len(sub_counter) == self._max_distinct_elements:
                num_good_subarrays += 1
                sub_counter -= Counter([self._list[j]])
                j -= 1

            counter -= Counter([self._list[i]])
            if len(counter) < self._max_distinct_elements:
                break

        return num_good_subarrays



class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        num_good_subarrays = 0
        caterpillar = Caterpillar(A, K)

        while caterpillar.end < len(A):
            caterpillar.grow()

            if caterpillar.num_distinct < K:
                break

            num_good_subarrays += caterpillar.count_good_subarrays()
            caterpillar.shrink()

        return num_good_subarrays


if __name__ == "__main__":
    solution = Solution()

    test_result = solution.subarraysWithKDistinct([1,2,1,2,3], 2)
    assert test_result == 7, test_result

    test_result = solution.subarraysWithKDistinct([2,2,1,2,2,2,1,1], 2)
    assert test_result == 23, test_result

    with open("k-elem-subarrays-test-case.json") as test_case_file:
        test_case = json.load(test_case_file)

    start_time = time.monotonic()
    print(solution.subarraysWithKDistinct(test_case["array"], test_case["K"]))
    print(f"Took {time.monotonic() - start_time}")
