"""5. Longest Palindromic Substring

Difficulty:
    Medium.

Link:
    https://leetcode.com/problems/longest-palindromic-substring/

Description:
    Given a string s, return the longest palindromic substring in s.

    Example 1:
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

    Example 2:
        Input: s = "cbbd"
        Output: "bb"

    Constraints:
        1 <= s.length <= 1000
        s consist of only digits and English letters.

Results:
    Runtime: 628 ms, faster than 90.58% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 14 MB, less than 81.78% of Python3 online submissions for Longest Palindromic Substring.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Kinda straight-forward approach. Starting with the first character at position i, find the same character
        # from the end of the string at position j. Then, if a substring between i and j is a palindrome, do the same
        # thing for the next character. If it isn't, find the next occurence of the character to the left of the
        # previous position j. Compare the length of found palindrom to the length of the current longest palindrome
        # (the current maximum) and pick the longest palindrome as the result.
        #
        # To speed up the process, there're some conditions to break from loops early:
        #   1. if whole given string is a palindrome, return it as a result.
        #   2. If a current substring (from i to the end of the string) is a palindrome, return it¹.
        #   3. If the current maximum is greater than the length of the rest of the string, exit².
        #   4. If the length of a substring between i and j is less than the current maximum, skip to the next char³.
        #   5. If the length of a new found palindrome is greater than the length of the rest of the string, exit¹.
        #
        # ¹ — conditions 1, 3 and 5 are working together: if the current substring is a palindrome, it will never be
        #      shorter than the current maximum because conditions 3 and 5 will be satisfied earlier.
        # ² — "exit" hereinafter means "return the current longest palindrome".
        # ³ — is made by setting the start value for rfind to i + maximum.

        # if string itself is a palindrome, return it
        if s == s[::-1]:
            return s

        # definitions and one-time calculations
        s_length = len(s)
        palindrome, length = "", 0

        for i, char in enumerate(s):
            # if rest of string itself is a palindrom, return it
            if s[i:] == s[i::-1]:
                return s[i:]

            # if current maximum is greater than the rest of the string, exit
            if length > s_length - i:
                return palindrome

            last = s_length

            # while same symbol as char is on the right side of string,
            # and the distance between chars is less than current maximum
            while (idx := s.rfind(char, i + length, last)) > -1:
                # get substring and check if it's a palindrome; if it is, compare the lengths
                substring = s[i : idx + 1]
                if substring == substring[::-1] and (new_len := len(substring)) > length:
                    palindrome, length = substring, new_len

                    # if the length of a new palindrome is greater than the length of the rest of the string, exit
                    if length > s_length - i:
                        return palindrome

                # shrink the search area
                last = idx

        return palindrome


def main():
    sol = Solution()

    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("aacabdkacaa") == "aca"
    assert sol.longestPalindrome("ac") in ("a", "c")
    assert sol.longestPalindrome("awerwerrewrewg") == "werwerrewrew"

    input_1 = (
        "xiqhechagdpbcdthaafmcnplenylepawbafsmxqlwhzgqmuemwolgoockcafchdsfggulwfzwwkvivnwgbelbbydzfkcfsschvbantskuosunh"
        "qihmqjmzgavfnonwhwrkfxgcbowfsebthbrhhklxxyoxiphrgxqodulrbbvdwcclpyjhljgyypztbqzkiyzbfnvnoargyyakaidkiyleurvjba"
        "dzwqjtrluayhblhdokmwrwhassruxpftwlbalfvwxtfcqibywsusrlwmbcibvgwnmmdmuhswuperbjoxarhqcpcebbtyhnrouvuwftspmzsmdh"
        "fcqovffkuikzrcweffmpnjldoalhcvqvjavllvajvqvchlaodljnpmffewcrzkiukffvoqcfhdmszmpstfwuvuornhytbbecpcqhraxojbrepu"
        "wshumdmmnwgvbicbmwlrsuswybiqcftxwvflablwtfpxurssahwrwmkodhlbhyaulrtjqwzdabjvruelyikdiakayygraonvnfbzyikzqbtzpy"
        "ygjlhjyplccwdvbbrludoqxgrhpixoyxxlkhhrbhtbesfwobcgxfkrwhwnonfvagzmjqmhiqhnusoukstnabvhcssfckfzdybblebgwnvivkww"
        "zfwluggfsdhcfackcooglowmeumqgzhwlqxmsfabwapelynelpncmfaahtdcbpdgahcehqix"
    )

    assert sol.longestPalindrome(input_1) == input_1

    input_2 = (
        "ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecs"
        "iqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvm"
        "yxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjqua"
        "yfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnku"
        "tmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhve"
        "zhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzu"
        "umilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"
    )

    assert sol.longestPalindrome(input_2) == input_2


if __name__ == "__main__":
    main()
