import streamlit as st

st.title("Two Sum")
# class Solution(object):
# def twoSum(self, nums, target):
# Create a text input box for the user
user_input = st.text_input("Enter a list of integers separated by spaces (e.g. 1 2 3):")
nums = []
# Parse the input into a list of integers
if user_input:
    try:
        # Split the input by commas, strip whitespace, and convert to integers
        nums = [int(x.strip()) for x in user_input.split(" ")]
        #st.write("Parsed List of Integers:", nums)
    except ValueError:
        st.error("Please enter valid integers separated by commas.")

# Integer-only input
target_input = st.text_input("Enter the target sum number:")
target = 0
if target_input:
    try:
        # Split the input by commas, strip whitespace, and convert to integers
        target = int(target_input)
        #st.write("Parsed List of Integers:", nums)
    except ValueError:
        st.error("Please enter valid integers")

#st.write("You entered:", target)

#nums = list(map(int, input("Enter numbers separated by space: ").split()))
#target = int(input("What is the target number? "))
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
        st.write(f"Target found. Indices: [{i}, {hashmap[complement]}]")
        found = True
        break
if not found:
     st.write("Target not found.") 