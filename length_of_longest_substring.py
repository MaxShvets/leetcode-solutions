class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_start = 0
        seen_chars = {}
        longest_length = 0
        i = 0

        for i, char in enumerate(s):
            if char in seen_chars and substr_start <= seen_chars[char]:
                substr_length = i - substr_start

                if longest_length < substr_length:
                    longest_length = substr_length

                substr_start = seen_chars[char] + 1

            seen_chars[char] = i

        substr_length = i - substr_start

        if longest_length < substr_length:
            longest_length = substr_length

        return longest_length


if __name__ == "__main__":
    solution = Solution()
    text = "abcabcbb"
    print(solution.lengthOfLongestSubstring(text))
