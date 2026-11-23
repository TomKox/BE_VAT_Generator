#!/usr/bin/env python3
"""Generate random Belgian VAT numbers with valid checksums.

Usage: python3 be_vat.py [count] [--invalid]
"""
import random
import sys


def make_vat(valid=True):
    # 8-digit base: leading 0 or 1, then 7 random digits
    base = int(random.choice("01") + "%07d" % random.randint(0, 9999999))
    check = 97 - base % 97
    if not valid:
        check = random.choice([c for c in range(1, 98) if c != check])
        check = check % 100
    return "BE%08d%02d" % (base, check)


def is_valid(vat):
    d = vat[2:]
    return len(d) == 10 and d.isdigit() and d[0] in "01" and 97 - int(d[:8]) % 97 == int(d[8:])


if __name__ == "__main__":
    args = sys.argv[1:]
    invalid = "--invalid" in args
    nums = [a for a in args if a.isdigit()]
    count = int(nums[0]) if nums else 10
    for _ in range(count):
        print(make_vat(valid=not invalid))