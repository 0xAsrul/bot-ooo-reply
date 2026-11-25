#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — prints exactly one line."""

import os

LINE = "Out of office until Monday — my inbox is in the care of the office goldfish, who has already requested a transfer to a quieter bowl."

print(LINE)

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
