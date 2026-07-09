class Solution:
    def get_kth(self, nums1: list[int], nums2: list[int], k: int) -> int:
        if len(nums1) > len(nums2):
            return self.get_kth(nums2, nums1, k)

        if len(nums1) == 0:
            return nums2[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        i = min(len(nums1), k // 2)
        j = min(len(nums2), k // 2)

        if nums1[i - 1] < nums2[j - 1]:
            return self.get_kth(nums1[i:], nums2, k - i)
        return self.get_kth(nums1, nums2[j:], k - j)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return float(self.get_kth(nums1, nums2, (total + 1) // 2))
        
        left = self.get_kth(nums1, nums2, total // 2)
        right = self.get_kth(nums1, nums2, total // 2 + 1)
    
        return (left + right) / 2.0