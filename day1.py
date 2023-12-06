"""
Day 1 of Advent Of Code 2023
https://adventofcode.com/2023/
"""
import os
import re
import sys

import requests

SESSION_KEY = {"session": os.environ.get("SESSION_KEY", None)}
DAY = int(re.findall(r"[0-9]+", sys.argv[0].rsplit("/", maxsplit=1)[-1])[0])


response = requests.get(
    f"https://adventofcode.com/2023/day/{DAY}/input", cookies=SESSION_KEY, timeout=500
)

data = response.text

# data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""

data = """ninefourone1
53sevenvvqm
kscpjfdxp895foureightckjjl1
72fivebt9ndgq
28gtbkszmrtmnineoneightmx
"""

data = data.split("\n")[:-1]
# Part 1

num_list = []
for line in data:
    nums = re.findall("[0-9]", line)
    if len(nums) > 0:
        nums = nums[0] + nums[-1]
        num_list.append(int(nums))

print("Part 1:", sum(num_list))

# Part 2
number_words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

number_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

number_words_str = "|".join(number_words)

num_list = []
for j, line in enumerate(data):
    if j == 1000:
        print(nums)
    nums = re.findall(f"([0-9])|({number_words_str})", line)
    nums = [x for y in nums for x in y]

    for i, num in enumerate(nums):
        if num == "":
            nums.pop(i)

    if not nums:
        print("Line:", j, nums)

    num_list.append(nums)

int_nums = []
for i, nums in enumerate(num_list):
    if len(nums) > 0:
        if nums[0] in number_dict:
            num1 = str(number_dict[nums[0]])
        else:
            num1 = nums[0]

        if nums[-1] in number_dict:
            num2 = str(number_dict[nums[-1]])
        else:
            num2 = nums[-1]

        # print(i)
        # if i == 59:
        #     print(nums)
        print(num1 + num2, nums[0], nums[-1])
        number = int(num1 + num2)

        int_nums.append(number)

# print(num_list)
# print(data)
print(int_nums)
print(sum(int_nums))
print(len(int_nums), len(data))
