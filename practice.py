def search_number(nums,target):
    def binary_search_left(nums,target):
        left,right=0,len(nums)-1
        first_index=-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                first_index=mid
                right=mid-1

            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return first_index
    
    def binary_search_right(nums,target):
        left,right=0,len(nums)-1
        last_index=-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                last_index=mid
                left=mid+1

            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return last_index
    
    start = binary_search_left(nums, target)
    end = binary_search_right(nums, target)
 
    return [start, end]

nums=[5, 7, 7, 8, 8, 10]
target=8
print (search_number(nums,target))