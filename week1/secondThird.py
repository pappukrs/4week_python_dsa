# arr = [1,2,3,4,5,6,7,8,9,10]

# print(arr[1:3])
# print(arr[2:4])

# arr.append(11)

# print(arr)

# arr.pop()

# print(arr)

# arr.insert(0, 0)

# print(arr)


# arr[0]=6

# print(arr)


# for n in arr:
#     print(n)



def two_sum(nums, target):
    num_map = {}  # Create a hash map to store numbers and their indices
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return []


print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]





def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum



print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6





def merge_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    # Add remaining elements
    result.extend(nums1[i:])
    result.extend(nums2[j:])

    return result


print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]




def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit



print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5




def product_except_self(nums):
    n = len(nums)
    output = [1] * n

    # Calculate prefix product
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Calculate suffix product
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output



print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]




def move_zeroes(nums):
    non_zero_pos = 0  # Pointer to place the next non-zero element

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
            non_zero_pos += 1

    return nums


print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]




def rotate_array(nums, k):
    n = len(nums)
    k = k % n

    # Step 1: Reverse the entire array
    nums.reverse()

    # Step 2: Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Step 3: Reverse the remaining elements
    nums[k:] = reversed(nums[k:])

    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]




def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)



print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [2, 3]




def find_duplicates(nums):
    duplicates = []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            duplicates.append(abs(nums[i]))
        else:
            nums[index] = -nums[index]

    return duplicates



def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


print(find_missing_number([3, 0, 1]))  # Output: 2





def find_missing_number(nums):
    n = len(nums)
    xor_all = 0

    # XOR all numbers in the array
    for num in nums:
        xor_all ^= num

    # XOR all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i

    return xor_all




