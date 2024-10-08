from typing import List

def divideArray(nums: List[int], k: int) -> List[List[int]]:
    """
    You are given an integer array nums of size n and a positive integer k.
    Divide the array into one or more arrays of size 3 satisfying the following conditions:
    
    Each element of nums should be in exactly one array.
    The difference between any two elements in one array is less than or equal to k.
    
    Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
    
    Example 1:
    
    Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
    Output: [[1,1,3],[3,4,5],[7,8,9]]
    Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
    The difference between any two elements in each array is less than or equal to 2.
    Note that the order of elements is not important.
    
    Example 2:
    
    Input: nums = [1,3,3,2,7,3], k = 3
    Output: []
    Explanation: It is not possible to divide the array satisfying all the conditions.
    
    
    Constraints:
    
    n == nums.length
    1 <= n <= 105
    n is a multiple of 3.
    1 <= nums[i] <= 105
    1 <= k <= 105
    """
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 3, 4, 8, 7, 9, 3, 5, 1], 2) == [[1,1,3],[3,4,5],[7,8,9]]
    assert candidate([1, 3, 3, 2, 7, 3], 3) == []
    assert candidate([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14) == [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
    assert candidate([33, 26, 4, 18, 16, 24, 24, 15, 8, 18, 34, 20, 24, 16, 3], 16) == [[3,4,8],[15,16,16],[18,18,20],[24,24,24],[26,33,34]]
    assert candidate([6, 1, 8, 8, 5, 8, 5, 9, 8, 9, 5, 8, 3, 4, 6], 7) == [[1,3,4],[5,5,5],[6,6,8],[8,8,8],[8,9,9]]
    assert candidate([20, 21, 34, 3, 19, 2, 23, 32, 20, 17, 14, 13, 19, 20, 6], 15) == [[2,3,6],[13,14,17],[19,19,20],[20,20,21],[23,32,34]]
    assert candidate([6, 10, 5, 12, 7, 11, 6, 6, 12, 12, 11, 7], 2) == [[5,6,6],[6,7,7],[10,11,11],[12,12,12]]
    assert candidate([12, 15, 26, 7, 10, 13, 15, 5, 27, 16, 14, 15], 18) == [[5,7,10],[12,13,14],[15,15,15],[16,26,27]]
    assert candidate([12, 7, 13, 10, 7, 19, 11, 23, 3, 3, 7, 9], 16) == [[3,3,7],[7,7,9],[10,11,12],[13,19,23]]
    assert candidate([19, 3, 23, 4, 8, 1, 1, 3, 26], 7) == [[1,1,3],[3,4,8],[19,23,26]]
    assert candidate([11, 13, 24, 11, 9, 23, 16, 19, 13], 8) == [[9,11,11],[13,13,16],[19,23,24]]
    assert candidate([6, 12, 21, 12, 6, 12, 25, 20, 15, 22, 11, 19, 8, 4, 18, 26, 17, 18, 12, 5, 8], 11) == [[4,5,6],[6,8,8],[11,12,12],[12,12,15],[17,18,18],[19,20,21],[22,25,26]]
    assert candidate([15, 17, 14, 3, 25, 15, 11, 25, 15, 16, 12, 18], 10) == [[3,11,12],[14,15,15],[15,16,17],[18,25,25]]
    assert candidate([16, 20, 16, 19, 20, 13, 14, 20, 14], 10) == [[13,14,14],[16,16,19],[20,20,20]]
    assert candidate([2, 13, 15, 14, 18, 15, 3, 13, 2], 1) == []
    assert candidate([1, 14, 20, 7, 17, 2, 14, 1, 8], 11) == [[1,1,2],[7,8,14],[14,17,20]]
    assert candidate([8, 12, 19, 8, 9, 19, 9, 19, 9, 8, 6, 9, 6, 6, 12], 3) == [[6,6,6],[8,8,8],[9,9,9],[9,12,12],[19,19,19]]
    assert candidate([18, 16, 17, 19, 12, 25, 11, 27, 11, 32, 32, 17], 20) == [[11,11,12],[16,17,17],[18,19,25],[27,32,32]]
    assert candidate([21, 11, 24, 20, 17, 13, 7, 20, 20, 16, 24, 20, 12, 17, 16, 15, 7, 7, 18, 15, 20], 6) == [[7,7,7],[11,12,13],[15,15,16],[16,17,17],[18,20,20],[20,20,20],[21,24,24]]
    assert candidate([6, 7, 7, 6, 7, 6], 13) == [[6,6,6],[7,7,7]]
    assert candidate([11, 12, 12, 5, 6, 5], 9) == [[5,5,6],[11,12,12]]
    assert candidate([5, 5, 12, 5, 5, 22, 2, 2, 5, 2, 5, 5, 16, 2, 22, 2, 12, 16, 15, 13, 19], 3) == [[2,2,2],[2,2,5],[5,5,5],[5,5,5],[12,12,13],[15,16,16],[19,22,22]]
    assert candidate([11, 28, 12, 5, 19, 15, 16, 9, 21, 13, 12, 9, 19, 19, 18], 9) == [[5,9,9],[11,12,12],[13,15,16],[18,19,19],[19,21,28]]
    assert candidate([10, 14, 17], 15) == [[10,14,17]]
    assert candidate([16, 15, 9, 20, 17, 19, 11, 18, 16], 9) == [[9,11,15],[16,16,17],[18,19,20]]
    assert candidate([16, 28, 16, 7, 18, 13, 5, 27, 27, 16, 20, 22, 13, 6, 17], 11) == [[5,6,7],[13,13,16],[16,16,17],[18,20,22],[27,27,28]]
    assert candidate([14, 7, 13, 2, 3, 7, 17, 13, 13, 2, 14, 7], 3) == [[2,2,3],[7,7,7],[13,13,13],[14,14,17]]
    assert candidate([20, 8, 6, 5, 10, 5, 10, 2, 20, 6, 12, 13, 13, 20, 4], 6) == [[2,4,5],[5,6,6],[8,10,10],[12,13,13],[20,20,20]]
    assert candidate([12, 14, 16, 9, 20, 18, 16, 4, 24, 14, 16, 30, 1, 17, 30, 16, 30, 6], 13) == [[1,4,6],[9,12,14],[14,16,16],[16,16,17],[18,20,24],[30,30,30]]
    assert candidate([13, 6, 19, 21, 16, 11, 1, 14, 7], 20) == [[1,6,7],[11,13,14],[16,19,21]]
    assert candidate([13, 2, 12, 22, 18, 15, 3, 20, 2, 18, 3, 14, 2, 10, 14, 9, 14, 3, 14, 17, 5], 9) == [[2,2,2],[3,3,3],[5,9,10],[12,13,14],[14,14,14],[15,17,18],[18,20,22]]
    assert candidate([12, 13, 12, 14, 14, 6, 5, 7, 23, 21, 21, 16, 15, 20, 22, 14, 20, 7], 10) == [[5,6,7],[7,12,12],[13,14,14],[14,15,16],[20,20,21],[21,22,23]]
    assert candidate([15, 14, 3, 19, 17, 18, 19, 23, 2, 16, 19, 3], 5) == [[2,3,3],[14,15,16],[17,18,19],[19,19,23]]
    assert candidate([12, 8, 18, 6, 12, 6, 8, 33, 20, 6, 17, 17, 27, 8, 12], 16) == [[6,6,6],[8,8,8],[12,12,12],[17,17,18],[20,27,33]]
    assert candidate([1, 1, 23, 17, 18, 1], 12) == [[1,1,1],[17,18,23]]
    assert candidate([13, 13, 3, 7, 6, 13, 6, 4, 3], 1) == [[3,3,4],[6,6,7],[13,13,13]]
    assert candidate([19, 10, 9, 20, 29, 28, 29, 9, 18, 27, 23, 4, 16, 8, 11, 19, 10, 12, 10, 10, 21], 20) == [[4,8,9],[9,10,10],[10,10,11],[12,16,18],[19,19,20],[21,23,27],[28,29,29]]
    assert candidate([13, 12, 12, 11, 22, 10], 15) == [[10,11,12],[12,13,22]]
    assert candidate([15, 16, 12, 34, 16, 16, 24, 21, 3, 24, 29, 10], 20) == [[3,10,12],[15,16,16],[16,21,24],[24,29,34]]
    assert candidate([17, 16, 17, 11, 13, 6], 19) == [[6,11,13],[16,17,17]]
    assert candidate([11, 16, 16, 6, 8, 20, 21, 3, 20, 11, 16, 6, 6, 11, 6], 3) == [[3,6,6],[6,6,8],[11,11,11],[16,16,16],[20,20,21]]
    assert candidate([2, 16, 8, 7, 15, 16], 9) == [[2,7,8],[15,16,16]]
    assert candidate([15, 17, 22], 14) == [[15,17,22]]
    assert candidate([8, 4, 9, 18, 18, 5, 10, 11, 19, 18, 19, 23, 4, 15, 25, 20, 20, 6], 7) == [[4,4,5],[6,8,9],[10,11,15],[18,18,18],[19,19,20],[20,23,25]]
    assert candidate([12, 20, 16, 12, 15, 16, 15, 20, 14, 16, 19, 13], 1) == [[12,12,13],[14,15,15],[16,16,16],[19,20,20]]
    assert candidate([20, 19, 8, 21, 13, 18, 21, 12, 12, 18, 9, 9], 1) == [[8,9,9],[12,12,13],[18,18,19],[20,21,21]]
    assert candidate([6, 14, 19, 17, 13, 4, 17, 10, 17], 19) == [[4,6,10],[13,14,17],[17,17,19]]
    assert candidate([8, 8, 12], 4) == [[8,8,12]]
    assert candidate([3, 16, 17, 18, 10, 8, 20, 16, 20, 10, 10, 21], 16) == [[3,8,10],[10,10,16],[16,17,18],[20,20,21]]
    assert candidate([19, 14, 17, 20, 16, 16, 7, 10, 18, 8, 16, 15, 15, 13, 12, 14, 17, 11], 8) == [[7,8,10],[11,12,13],[14,14,15],[15,16,16],[16,17,17],[18,19,20]]
    assert candidate([18, 7, 11, 13, 13, 9, 22, 20, 21, 13, 7, 18, 8, 8, 16], 4) == [[7,7,8],[8,9,11],[13,13,13],[16,18,18],[20,21,22]]
    assert candidate([10, 15, 9, 15, 15, 10], 1) == [[9,10,10],[15,15,15]]
    assert candidate([16, 17, 16], 16) == [[16,16,17]]
    assert candidate([15, 1, 15, 14, 18, 17, 1, 18, 12, 16, 6, 6, 7, 1, 12], 4) == [[1,1,1],[6,6,7],[12,12,14],[15,15,16],[17,18,18]]
    assert candidate([6, 11, 6, 18, 11, 13, 13, 8, 11, 4, 4, 11, 12, 17, 11], 12) == [[4,4,6],[6,8,11],[11,11,11],[11,12,13],[13,17,18]]
    assert candidate([5, 13, 4, 14, 11, 18, 9, 10, 20, 5, 17, 11, 5, 8, 20, 5, 14, 4, 18, 17, 17], 8) == [[4,4,5],[5,5,5],[8,9,10],[11,11,13],[14,14,17],[17,17,18],[18,20,20]]
    assert candidate([13, 6, 20, 13, 12, 8, 7, 12, 22, 16, 13, 7, 12, 17, 5], 6) == [[5,6,7],[7,8,12],[12,12,13],[13,13,16],[17,20,22]]
    assert candidate([23, 2, 15, 20, 18, 14, 20, 7, 2, 22, 4, 14, 7, 9, 15, 14, 2, 7], 8) == [[2,2,2],[4,7,7],[7,9,14],[14,14,15],[15,18,20],[20,22,23]]
    assert candidate([19, 9, 2, 4, 17, 2, 27, 18, 17], 18) == [[2,2,4],[9,17,17],[18,19,27]]
    assert candidate([5, 20, 29, 4, 12, 14, 31, 6, 11, 2, 15, 17, 15, 19, 4], 20) == [[2,4,4],[5,6,11],[12,14,15],[15,17,19],[20,29,31]]
    assert candidate([15, 20, 5, 24, 18, 16, 25, 21, 28, 12, 19, 28, 25, 20, 14, 18, 24, 28], 17) == [[5,12,14],[15,16,18],[18,19,20],[20,21,24],[24,25,25],[28,28,28]]
    assert candidate([9, 6, 23, 17, 7, 17], 20) == [[6,7,9],[17,17,23]]
    assert candidate([24, 23, 19], 6) == [[19,23,24]]
    assert candidate([6, 19, 22, 7, 17, 7, 15, 17, 7, 18, 4, 14, 9, 10, 16], 9) == [[4,6,7],[7,7,9],[10,14,15],[16,17,17],[18,19,22]]
    assert candidate([4, 3, 15, 1, 15, 15], 4) == [[1,3,4],[15,15,15]]
    assert candidate([10, 22, 18, 15, 7, 21, 6, 7, 11, 9, 7, 6, 7, 10, 18], 8) == [[6,6,7],[7,7,7],[9,10,10],[11,15,18],[18,21,22]]
    assert candidate([16, 17, 2, 17, 9, 7, 22, 17, 12, 4, 14, 17, 4, 19, 12, 18, 19, 8, 17, 5, 6], 7) == [[2,4,4],[5,6,7],[8,9,12],[12,14,16],[17,17,17],[17,17,18],[19,19,22]]
    assert candidate([20, 18, 18, 22, 7, 9, 9, 10, 16, 4, 18, 18, 11, 9, 18, 11, 11, 21], 7) == [[4,7,9],[9,9,10],[11,11,11],[16,18,18],[18,18,18],[20,21,22]]
    assert candidate([5, 11, 15, 9, 17, 6, 16, 14, 4, 9, 5, 13, 10, 12, 13, 15, 13, 12, 16, 12, 13], 5) == [[4,5,5],[6,9,9],[10,11,12],[12,12,13],[13,13,13],[14,15,15],[16,16,17]]
    assert candidate([4, 16, 17], 20) == [[4,16,17]]
    assert candidate([10, 9, 22, 13, 17, 11, 6, 9, 11], 10) == [[6,9,9],[10,11,11],[13,17,22]]
    assert candidate([3, 11, 19, 8, 22, 23, 15, 18, 37, 7, 25, 20, 12, 19, 7], 18) == [[3,7,7],[8,11,12],[15,18,19],[19,20,22],[23,25,37]]
    assert candidate([4, 6, 6, 3, 11, 11], 16) == [[3,4,6],[6,11,11]]
    assert candidate([10, 17, 10, 15, 16, 8], 7) == [[8,10,10],[15,16,17]]
    assert candidate([4, 20, 4, 19, 8, 7, 4, 20, 7], 3) == [[4,4,4],[7,7,8],[19,20,20]]
    assert candidate([4, 4, 4], 17) == [[4,4,4]]
    assert candidate([18, 6, 15, 20, 5, 27, 23, 15, 26, 11, 11, 4, 17, 23, 11], 15) == [[4,5,6],[11,11,11],[15,15,17],[18,20,23],[23,26,27]]
    assert candidate([8, 9, 5], 15) == [[5,8,9]]
    assert candidate([20, 15, 8, 11, 11, 10, 19, 7, 20], 7) == [[7,8,10],[11,11,15],[19,20,20]]
    assert candidate([12, 11, 18, 13, 13, 21], 11) == [[11,12,13],[13,18,21]]
    assert candidate([19, 29, 11, 18, 19, 17, 29, 19, 7], 14) == [[7,11,17],[18,19,19],[19,29,29]]
    assert candidate([14, 1, 25, 1, 14, 19, 2, 2, 4, 16, 17, 11, 26, 29, 12], 17) == [[1,1,2],[2,4,11],[12,14,14],[16,17,19],[25,26,29]]
    assert candidate([14, 25, 16, 11, 7, 13, 12, 16, 24, 19, 5, 17], 13) == [[5,7,11],[12,13,14],[16,16,17],[19,24,25]]
    assert candidate([11, 26, 19, 10, 16, 10, 11, 18, 9], 11) == [[9,10,10],[11,11,16],[18,19,26]]
    assert candidate([16, 8, 15], 16) == [[8,15,16]]
    assert candidate([12, 8, 18, 8, 18, 13, 12, 18, 18, 13, 12, 23, 21, 8, 13], 5) == [[8,8,8],[12,12,12],[13,13,13],[18,18,18],[18,21,23]]
    assert candidate([12, 16, 9, 8, 22, 16], 16) == [[8,9,12],[16,16,22]]
    assert candidate([15, 16, 18, 8, 12, 7, 5, 17, 23, 17, 18, 13, 5, 4, 13, 18, 7, 20], 6) == [[4,5,5],[7,7,8],[12,13,13],[15,16,17],[17,18,18],[18,20,23]]
    assert candidate([12, 11, 14, 13, 9, 16, 31, 19, 21, 22, 7, 1, 22, 23, 9, 2, 21, 21], 15) == [[1,2,7],[9,9,11],[12,13,14],[16,19,21],[21,21,22],[22,23,31]]
    assert candidate([7, 15, 18, 20, 6, 21, 18, 17, 11, 1, 14, 15, 18, 8, 17, 13, 11, 8, 5, 12, 11], 10) == [[1,5,6],[7,8,8],[11,11,11],[12,13,14],[15,15,17],[17,18,18],[18,20,21]]
    assert candidate([13, 16, 17, 16, 6, 12], 11) == [[6,12,13],[16,16,17]]
    assert candidate([17, 17, 17, 16, 17, 17], 1) == [[16,17,17],[17,17,17]]
    assert candidate([6, 14, 6, 15, 14, 6], 17) == [[6,6,6],[14,14,15]]
    assert candidate([23, 19, 21, 10, 10, 13, 15, 19, 19, 3, 15, 3], 12) == [[3,3,10],[10,13,15],[15,19,19],[19,21,23]]
    assert candidate([11, 4, 3, 11, 3, 27, 19, 10, 6, 12, 11, 24, 27, 1, 31], 17) == [[1,3,3],[4,6,10],[11,11,11],[12,19,24],[27,27,31]]
    assert candidate([8, 18, 18, 20, 20, 19, 20, 31, 7], 17) == [[7,8,18],[18,19,20],[20,20,31]]
    assert candidate([4, 22, 8, 12, 1, 4, 4, 17, 22, 4, 10, 1], 12) == [[1,1,4],[4,4,4],[8,10,12],[17,22,22]]
    assert candidate([16, 15, 16, 6, 9, 22, 14, 16, 10, 26, 18, 16, 11, 18, 7], 10) == [[6,7,9],[10,11,14],[15,16,16],[16,16,18],[18,22,26]]
    assert candidate([5, 16, 12, 26, 16, 18, 1, 6, 23, 2, 1, 21, 8, 11, 9], 14) == [[1,1,2],[5,6,8],[9,11,12],[16,16,18],[21,23,26]]
    assert candidate([6, 3, 24, 13, 19, 24, 13, 12, 15, 3, 6, 3], 17) == [[3,3,3],[6,6,12],[13,13,15],[19,24,24]]


def test_check():
    check(divideArray)


### Metadata below ###
# question_id = 3241
# question_title = Divide Array Into Arrays With Max Difference
# question_title_slug = divide-array-into-arrays-with-max-difference
# question_difficulty = Medium
# question_category = Algorithms
# question_likes = 95
# question_dislikes = 20