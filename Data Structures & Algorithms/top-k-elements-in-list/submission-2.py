class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res_dict = defaultdict(int) #[7,2] [number val, count of num]
        # counter = 0
        # res = []
        # for i in nums:
        #     res_dict[i] += 1
        # #sort_dict = sorted(res_dict.values(), reverse = True) #list
        # sort_keys = sorted(res_dict, key=lambda x: res_dict[x], reverse=True)
        # return sort_keys[:k]

        #2nd solution
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        hasil = sorted(count, key=count.get, reverse=True)
        return hasil[:k]