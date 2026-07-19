class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        insert_pos = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                if i != insert_pos:
                    arr[insert_pos] = arr[i]
                    arr[i] = 0
                insert_pos += 1
