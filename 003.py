"""3. Longest Substring Without Repeating Characters

Description:
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:
        0 <= s.length <= 5 * 10⁴
        s consists of English letters, digits, symbols and spaces.

Results:
    Runtime: 48 ms, faster than 98.72% of Python3 online submissions for
        Longest Substring Without Repeating Characters.
    Memory Usage: 13.9 MB, less than 97.52% of Python3 online submissions for
        Longest Substring Without Repeating Characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # At first, I started with set, that will contain every char before current symbol.
        # If char that is already in set appears, clean the set and refill it up with symbols starting on
        # previous occurence of symbol + 1. Now, all you need is to keep max length right.
        # Such recalculations consume a lot of time, so it was faster just to use dict, keeping last occurences of
        # symbols. But now I can't operate just lengths, I need a position to calculate it, because the dict can and
        # will contain positions that are beyond current starting symbol. To avoid it, all I need is to keep current
        # starting position and check if last occurence of current symbol is in current substring or is before it.

        seen, start, max_length = dict(), 0, 0

        for idx, char in enumerate(s):
            if char in seen and seen[char] >= start:
                max_length = max(max_length, idx - start)
                start = seen[char] + 1
            seen[char] = idx
        return max(len(s) - start, max_length)


def main():
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring(" ") == 1
    assert sol.lengthOfLongestSubstring("dvdf") == 3


if __name__ == "__main__":
    main()
