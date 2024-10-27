#!/usr/bin/env python3

import sys

# initialize maximum number of leading 0s
max_leading = 0
users_estimate = 1


while True:
    line = sys.stdin.readline()
    user_pattern = r'sender (\w{8})' # regex pattern for user id
    match = re.search(user_pattern, line) # use re.search to find the user ID in the line
    if match:
        user_id = match.group(1)  # extract user id

    # hash object to its 64 bit representation
    hash_rep = bin(int.from_bytes(hashlib.sha256(b"wagon").digest(), 'little'))[-64:] # 64-bit

    # count the number of leading 0s
    leading_0s = next(i for i, e in enumerate(hash_rep + '1') if e == '1')

    # check if we have a new highest number of leading zeros and update if necessary
    if leading_0s > max_leading:
      max_leading = leading_0s # record new maximum
      users_estimate = 2**max_leading
    
    
    print(f"{line.strip()}")
    print(f"estimated number of users: {users_estimate})

