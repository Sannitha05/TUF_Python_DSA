class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        res = []
        for num in arr:
            if num != 0:
                res.append(num)
        while len(res) < len(arr):
            res.append(0)
        print(res)

        for i in range(len(arr)):
            arr[i] = res[i]