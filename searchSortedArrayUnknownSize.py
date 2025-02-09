# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:    
    def search(self, reader: 'ArrayReader', target: int) -> int:

        if reader.get(0) == target:
            return 0
        low=0
        high=1
        while(reader.get(high) <= target):
            low = high
            high = high * 2

        while (low <= high):
            mid = low + (high - low) // 2

            if (reader.get(mid) == target):
                return mid
            elif (target < reader.get(mid)):
                high = mid - 1
            else:
                low = mid + 1

        return -1