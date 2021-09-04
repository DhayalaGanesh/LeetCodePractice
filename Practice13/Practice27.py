from typing import List
def removeElement(nums: List[int], val: int) -> int:
    index = 0
    for i in range(0,len(nums)):
        if(nums[i] != val):
            nums[index] = nums[i]
            index = index + 1
    return index

print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))

