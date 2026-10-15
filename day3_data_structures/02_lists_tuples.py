# Lists
nums = [5, 2, 9, 1]
nums.append(7)              #add at end
nums.insert(0, 10)          #add at position 0
nums.remove(2)              #remove value 2
last = nums.pop()           #remove and return last item
print(nums, "popped:", last)

nums.sort()
print("Sorted:", nums)
nums.reverse()
print("Reversed:", nums)

print("Slice:", nums[1:3])
print("Backwards:", nums[::-1])
print("Length:", len(nums), "Sum", sum(nums))

# Tuples
point = (3, 4)
x, y  = point           #unpacking
print(x, y, point[0])

try:
    point[0] = 10       #tuples can't be changed
except TypeError as e:
    print("Error:", e)