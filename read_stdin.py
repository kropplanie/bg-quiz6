#!/usr/bin/env python3

import sys
import re
import mmh3

# initialize maximum number of leading 0s
max_leading = 0
users_estimate = 1


while True:
    line = sys.stdin.readline()
    user_pattern = r'sender (\w{8})' # regex pattern for user id
    match = re.search(user_pattern, line) # use re.search to find the user ID in the line
    if match:
        user_id = match.group(1)  # extract user id

        hash_value = mmh3.hash(user_id, 42, signed=False) & ((1 << 32)-1)
        rev_hash_value = hash_value[::-1]
        
        # count the number of leading 0s
        leading_0s = next(i for i, e in enumerate(rev_hash_value + '1') if e == '1')

        # check if we have a new highest number of leading zeros and update if necessary
        if leading_0s > max_leading:
            print(f'new max leading zeros hash: {user_id}, {rev_hash_value}')
            max_leading = leading_0s # record new maximum
            users_estimate = 2**max_leading
    
    
    print(f"{line.strip()}")
    print(f"estimated number of users: {users_estimate}")

