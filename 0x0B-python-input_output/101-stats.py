#!/usr/bin/python3
import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        split_line = line.split()
        if len(split_line) < 2:
            continue
        status = split_line[-2]
        file_size += int(split_line[-1])
        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print("File size:", file_size)
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")
finally:
    print("File size:", file_size)
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
