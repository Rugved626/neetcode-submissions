from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1  # Move past '#'

            res.append(s[j:j + length])
            i = j + length

        return res