from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Helper function to check if it's possible to make m bouquets by day x
        def canMakeBouquets(x):
            bouquets = flowers = 0
            for bloom in bloomDay:
                flowers = flowers + 1 if bloom <= x else 0
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            return bouquets >= m
        
        # If there are not enough flowers to make m bouquets, return -1
        if len(bloomDay) < m * k:
            return -1
        
        # Binary search to find the minimum day
        low, high = 1, max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        return low



