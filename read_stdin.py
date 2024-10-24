#!/usr/bin/env python3

import sys

# define a function to hash an entry into one of 10 buckets
def hash_10(input):
  return hash(input) % 10

with open('queries_sample.txt', 'a') as f:
  while True:
      line = sys.stdin.readline() # read in the current line
      if hash_10(line) == 0: # if it is hashed into bucket 0
        f.write(f"{line.strip()}") # save the query in the sample file
        f.flush() # write the data to the file immediately
      print(f"{line.strip()}") # print the query (all queries)
