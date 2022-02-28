"""6. Zigzag Conversion

Difficulty:
    Medium.

Link:
    https://leetcode.com/problems/zigzag-conversion/

Description:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

        string convert(string s, int numRows);


    Example 1:
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

    Example 2:
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
            P     I    N
            A   L S  I G
            Y A   H R
            P     I

    Example 3:
        Input: s = "A", numRows = 1
        Output: "A"

    Constraints:
        1 <= s.length <= 1000
        s consists of English letters (lower-case and upper-case), ',' and '.'.
        1 <= numRows <= 1000

Results:
    A:
        Runtime: 63 ms, faster than 83.52% of Python3 online submissions for Zigzag Conversion.
        Memory Usage: 14 MB, less than 76.93% of Python3 online submissions for Zigzag Conversion.

    B:
        Runtime: 44 ms, faster than 99.71% of Python3 online submissions for Zigzag Conversion.
        Memory Usage: 13.9 MB, less than 89.25% of Python3 online submissions for Zigzag Conversion.
"""


class Solution:
    # At first, it's possible to skip all the calculations if `numRows == 1` or the length of the given string is less
    # or equal to the `numRows`. As for storing the results: let's create an array of empty strings, which one
    # representing a row, with a length of `numRows`, and join them at the end.
    #
    # It's easy to see that resulting "image" has repeating pattern with each block containing `numRows * 2 - 2`
    # characters, e.g. 4 for 3 and 6 for 4. So, first approach was to calculate positions and append each character to
    # the right row. Let's take char at position `i`. Corresponding row number would be `row = i % (numRows * 2 - 2)`,
    # and if such row number is greater than `numRows - 1`, then `row = (numRows - 1) * 2 - row` because it's on the
    # backwards line.
    #
    # But why to calculate row index at all? It always goes up and down by 1 until met top or bottom border.
    # So, next approach is to create an index variable `i` and direction flag `up`. If direction is "up", next index
    # will be equal to `i + 1`, and if "down", `i - 1`, or, combining both, `i += 1 if up else -1`. Next step is to
    # change direction: if calculated index is less than 0 or greater than `numRows - 1`, do the switch. Also, it's
    # needed to reset the index value. Thus, `if i < 0 or i > numRows - 1` then `i = numRows - 2 if up else 1` and
    # `up = not up`. Notice that such index resetting is incorrect if starting skip isn't applied, general value would
    # be equal to `i = max(0, numRows - 2) if up else min(numRows - 1, 1)`, because `numRows` can be equal to 1.
    #
    # So, first approach is implemented as `convert_a`, second one as `convert_b`.

    def convert_a(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [""] * numRows
        block_size, col_size = numRows * 2 - 2, numRows - 1

        for i, char in enumerate(s):
            row = i % block_size
            if row > col_size:
                row = col_size * 2 - row
            result[row] += char

        return "".join(result)

    def convert_b(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [""] * numRows
        col_size = numRows - 1

        i, up = 0, True
        for char in s:
            result[i] += char
            i += 1 if up else -1
            if i < 0 or i > col_size:
                i = col_size - 1 if up else 1
                up = not up

        return "".join(result)


def main():
    sol = Solution()

    assert sol.convert_a("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert_a("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert_a("A", 1) == "A"
    assert sol.convert_a("BACBACBAC", 2) == "BCABCABCA"
    assert sol.convert_a("ABC", 1) == "ABC"
    assert sol.convert_a("ABC", 3) == "ABC"

    assert sol.convert_b("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert_b("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert_b("A", 1) == "A"
    assert sol.convert_b("BACBACBAC", 2) == "BCABCABCA"
    assert sol.convert_b("ABC", 1) == "ABC"
    assert sol.convert_b("ABC", 3) == "ABC"


if __name__ == "__main__":
    main()
