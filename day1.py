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
    f"https://adventofcode.com/2022/day/{DAY}/input", cookies=SESSION_KEY, timeout=500
)

data = response.text
