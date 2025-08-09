def two_sum(nums,target):
    """
    Input: nums (List[int]) and target (int).  
    Output: Indices of two numbers summing to target or empty list if none.  
    
    Uses a dictionary to track seen numbers for O(n) time complexity.  
    Finds two distinct numbers that add up to target in one pass.  
    Efficient and concise solution for the Two Sum problem.
    """
    map={} #map to store complements
    i=0
    while i<len(nums):
        num=nums[i]
        complement=target-num #Number needed to reach target 
        if complement in map: 
            #Found two numbers return their indexes 
            return [map[complement],i]
        map[num]=i #Store current number and index
        i+=1
    return []


'''
Java Implementation
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {
                        i,
                        j
                    };
                }
            }
        }
        return new int[] {};
    }
}
'''
