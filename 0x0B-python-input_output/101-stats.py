#!/usr/bin/python3
"""
This module provides a script to read stdin line by line and compute metrics.
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def print_stats():
    """
    Prints the current statistics.
    """
    print("File size: {}".format(total_size))
    for code in status_codes:
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            status_code = int(parts[-2])
            size = int(parts[-1])
            if status_code in status_codes:
                code_counts[status_code] += 1
            total_size += size
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
