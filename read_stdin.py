#!/usr/bin/env python3

import sys
import re
import hashlib

# initialize maximum number of leading 0s
max_leading = 0
users_estimate = 1


while True:
    line = sys.stdin.readline()
    user_pattern = r'sender (\w{8})' # regex pattern for user id
    match = re.search(user_pattern, line) # use re.search to find the user ID in the line
    if match:
        user_id = match.group(1)  # extract user id

        hash_value = hashlib.sha256(user_id.encode('utf8')).hexdigest()
        hash_int = int(hash_value, 16)
        bin_hash = bin(hash_int)[2:]  # convert to binary
        
        # count the number of leading 0s
        leading_0s = next(i for i, e in enumerate(bin_hash + '1') if e == '1')

        # check if we have a new highest number of leading zeros and update if necessary
        if leading_0s > max_leading:
            print(f'new max leading zeros hash: {user_id}, {hash_rep}')
            max_leading = leading_0s # record new maximum
            users_estimate = 2**max_leading
    
    
    print(f"{line.strip()}")
    print(f"estimated number of users: {users_estimate}")

