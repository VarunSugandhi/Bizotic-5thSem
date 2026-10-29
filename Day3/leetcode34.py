# Leetcode problem number 34


def searchRange(nums, target):
        def firstfind():
            ans = -1
            low = 0
            high = len(nums) - 1

            while low <= high :
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    high = mid - 1
                elif nums[mid] < target :
                    low = mid + 1
                else :
                    high = mid - 1
            return ans
        def lastfind():
            ans = -1
            low = 0
            high = len(nums) - 1

            while low <= high :
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1
                elif nums[mid] < target :
                    low = mid + 1
                else :
                    high = mid - 1
            return ans
        return [firstfind(), lastfind()]

nums = [5,7,7,8,8,10]
target = 8
# list = searchRange(nums,target)
print("The target is present at index :",searchRange(nums,target))
