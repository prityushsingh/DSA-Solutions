class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)

            if key in anagrams:
                anagrams[key].append(s)             
            else:
                anagrams[key] = [s]
        return list(anagrams.values())


#Time complexity : O(N*M)
#Space complexity : O(M)
