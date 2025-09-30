# class Solution(object):
# def twoSum(self, nums, target):
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("What is the target number? "))
found = False
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if (nums[i] + nums[j]) == target:
#             print(f"Target found. Indices: [{i}, {j}]")
#             found = True
#             break
#     if found:
#         break
# if not found:
#     print("Target not found.")

hashmap = {}
for i in range(len(nums)):
    hashmap[nums[i]] = i

for i in range(len(nums)):
    complement = target - nums[i]
    # check if the complement exist in hashmap
    if complement in hashmap and hashmap[complement] != i:
        print(f"Target found. Indices: [{i}, {hashmap[complement]}]")
        found = True
        break
if not found:
     print("Target not found.") 