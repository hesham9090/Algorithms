"""
Brute Force String Match
Implements brute-force string matching
Input: An array text[0..n − 1] of n characters representing a text and
an array str[0..m − 1] of m characters representing a pattern (string)
Output: The index of the first character in the text that starts a matching substring or −1 if the search is unsuccessful

"""


def string_match(str, text):
    n = len(text)
    m = len(str)
    for i in range(n - m):
        j = 0
        while (j < m) and (str[j] == text[i + j]):
            j += 1
        if j == m :
            return i

    return -1


text = "hello , I am playing football today"
str = "football"

testcase = string_match(str, text)
print("Index is", testcase)
print("additional check: ", text[testcase:testcase+len(str)])
