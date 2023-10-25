def sum_of_two(nums:list[int], target:int) -> list[int]:
    res:list[int] = [0,1]
    diffs:dict[int, int] = {}

    for i in range(len(nums)):
        num:int = nums[i]
        diff:int = target - num
        if (diffs.get(diff) != None):
            return [diffs.get(diff), i]
        else:
            diffs[num] = i
    return []

def check(nums, res, target):
    print("Success" if (nums[res[0]] + nums[res[1]] == target) else "Fail")


#main
if __name__ == '__main__':
    #Example1
    nums = [2,7,11,15]
    target = 9
    solution = sum_of_two(nums, target)
    check(nums, solution, target)

    #Example2
    nums = [3,2,3]
    target = 6
    solution = sum_of_two(nums, target)
    check(nums, solution, target)

    #Example3
    nums = [3,3]
    target = 6
    solution = sum_of_two(nums, target)
    check(nums, solution, target)
