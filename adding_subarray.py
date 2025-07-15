# testing sum of incrementing subarray 
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

lower_bound = 0
upper_bound = 4
total = 0
current_elements = [] 

while lower_bound <= upper_bound:
    total += nums[lower_bound]
    current_elements.append(nums[lower_bound])
    print(f"elem added[{lower_bound}] = {nums[lower_bound]}, current total: {total}")
    print(f"current elements being added: {current_elements}")
    lower_bound += 1

print("all elems added:")
print(current_elements)
print("final total:", total)
