class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            #print(sorted_s)
            sort_dict[sorted_s].append(s)
        for value in sort_dict.values():
            res.append(value)
        return res