# count all occurrences of each number and store them in a dictionary
# value : count

nums = [1, 2, 4, 3, 1, 2]
seen = {} # empty dict

for num in nums:
    if num in seen: # if num ("key" - starts at 1) is in dict
        seen[num] += 1 # assign an additional 1 to the value of num
    else:
        seen[num] = 1 # key, value = num, 1 -- for the first time seeing this digit

for num, count in seen.items():
    print(f"num: {num}, count: {count}")

