class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for val in strs:
            count = [0] * 26

            for char in val:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)

            if key in hash_map:
                hash_map[key].append(val)
            else:
                hash_map[key] = [val]

        return list(hash_map.values())