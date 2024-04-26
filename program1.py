def smallest_missing_positive_integer(nums: List[int]) -> int:
    """
    Implement the function smallest_missing_positive_integer 
    using the provided smallest_missing_positive_integer function 
    to find the smallest missing positive integer in the given list.

    """
    res = 0 
    nums.sort()
    for i in nums :
        if res == i:
            res+=1
        







    



  

