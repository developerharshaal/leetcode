class Solution:
    def mergeSort(self,nums,low,high):
        cnt =0
        if low >= high:
            return 0
        mid = (low + high)//2
        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid+1, high)
        cnt += self.countPairs(nums, low, mid, high)
        self.merge(nums,low, mid, high)
        return cnt

    def merge(self, nums, low, mid, high):
        temp = []
        left = low
        right = mid+1
        while left <=mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        
        for i in range(low, high+1):
            nums[i] = temp[i - low]

    def countPairs(self,nums, low, mid, high):
        right = mid+1
        cnt = 0
        for i in range(low, mid+1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            cnt += (right - (mid+1))
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        cnt = self.mergeSort(nums,0,len(nums)-1)
        return cnt
