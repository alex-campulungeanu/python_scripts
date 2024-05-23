def longest_consecutive(nums: list[int]) -> int:
    if nums == []:
        return 1
    nums = list(set(nums))
    nums.sort()
    count = 1
    longest = 1 
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            count += 1
            longest = max(longest, count)
        else:
            count = 1
    return longest

test_nums = [100, 4, 200, 1, 3, 2, 51,52,53,99,54,66,55,56]
res = longest_consecutive(test_nums)
print(res)
