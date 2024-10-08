from typing import List

def constructProductMatrix(grid: List[List[int]]) -> List[List[int]]:
    """
    Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:
    
     * Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
    
    Return the product matrix of grid.
    
    Example 1:
    
    Input: grid = [[1,2],[3,4]]
    Output: [[24,12],[8,6]]
    Explanation: p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
    p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
    p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
    p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
    So the answer is [[24,12],[8,6]].
    
    Example 2:
    
    Input: grid = [[12345],[2],[1]]
    Output: [[2],[0],[0]]
    Explanation: p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2.
    p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0. So p[0][1] = 0.
    p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0. So p[0][2] = 0.
    So the answer is [[2],[0],[0]].
    
    Constraints:
    
     * 1 <= n == grid.length <= 105
     * 1 <= m == grid[i].length <= 105
     * 2 <= n * m <= 105
     * 1 <= grid[i][j] <= 109
    """
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([[1, 2], [3, 4]]) == [[24,12],[8,6]]
    assert candidate([[12345], [2], [1]]) == [[2],[0],[0]]
    assert candidate([[1], [2]]) == [[2],[1]]
    assert candidate([[1, 2]]) == [[2,1]]
    assert candidate([[12345, 12345]]) == [[0,0]]
    assert candidate([[1], [4]]) == [[4],[1]]
    assert candidate([[3], [4]]) == [[4],[3]]
    assert candidate([[4], [3]]) == [[3],[4]]
    assert candidate([[1, 1, 1]]) == [[1,1,1]]
    assert candidate([[2, 1, 1]]) == [[1,2,2]]
    assert candidate([[3], [5], [2]]) == [[10],[6],[15]]
    assert candidate([[1, 2], [1, 1], [6, 4]]) == [[48,24],[48,48],[8,12]]
    assert candidate([[1, 2, 2], [1, 4, 3]]) == [[48,24,24],[48,12,16]]
    assert candidate([[2], [7], [2], [6]]) == [[84],[24],[84],[28]]
    assert candidate([[3], [4], [7], [7]]) == [[196],[147],[84],[84]]
    assert candidate([[3, 1, 1], [1, 3, 4]]) == [[12,36,36],[36,12,9]]
    assert candidate([[4], [8], [3], [7]]) == [[168],[84],[224],[96]]
    assert candidate([[5], [8], [8], [3]]) == [[192],[120],[120],[320]]
    assert candidate([[6], [5], [8], [5]]) == [[200],[240],[150],[240]]
    assert candidate([[8], [1], [3], [8]]) == [[24],[192],[64],[24]]
    assert candidate([[1], [10], [3], [10], [9]]) == [[2700],[270],[900],[270],[300]]
    assert candidate([[1, 1, 1, 1, 1]]) == [[1,1,1,1,1]]
    assert candidate([[1, 1, 2, 2, 1]]) == [[4,4,2,2,4]]
    assert candidate([[1, 2, 3], [3, 3, 5], [3, 4, 2]]) == [[6480,3240,2160],[2160,2160,1296],[2160,1620,3240]]
    assert candidate([[2], [7], [5], [3], [4]]) == [[420],[120],[168],[280],[210]]
    assert candidate([[2, 2, 2, 2, 1]]) == [[8,8,8,8,16]]
    assert candidate([[2, 2, 4, 4], [3, 2, 1, 4]]) == [[768,768,384,384],[512,768,1536,384]]
    assert candidate([[2, 4, 1, 1], [3, 4, 4, 1]]) == [[192,96,384,384],[128,96,96,384]]
    assert candidate([[3, 1, 1, 4], [1, 4, 1, 1]]) == [[16,48,48,12],[48,12,48,48]]
    assert candidate([[3, 2, 5], [6, 4, 3], [6, 3, 1]]) == [[615,7095,7776],[6480,9720,615],[6480,615,1845]]
    assert candidate([[5, 5, 5], [4, 3, 1], [4, 5, 1]]) == [[6000,6000,6000],[7500,10000,5310],[7500,6000,5310]]
    assert candidate([[6, 3], [1, 5], [2, 7], [6, 5]]) == [[6300,255],[765,7560],[6555,5400],[6300,7560]]
    assert candidate([[6, 3, 2], [2, 3, 1], [5, 5, 4]]) == [[3600,7200,10800],[10800,7200,9255],[4320,4320,5400]]
    assert candidate([[6, 5, 3], [4, 4, 5], [3, 2, 5]]) == [[11310,6165,10275],[4620,4620,6165],[10275,9240,6165]]
    assert candidate([[8], [5], [5], [9], [8]]) == [[1800],[2880],[2880],[1600],[1800]]
    assert candidate([[10], [5], [6], [8], [6]]) == [[1440],[2880],[2400],[1800],[2400]]
    assert candidate([[10], [9], [3], [4], [3]]) == [[324],[360],[1080],[810],[1080]]
    assert candidate([[1, 1, 1, 2, 2, 1]]) == [[4,4,4,2,2,4]]
    assert candidate([[1, 1, 2, 1, 2, 1]]) == [[4,4,2,4,2,4]]
    assert candidate([[1, 1, 2, 1, 2, 2]]) == [[8,8,4,8,4,4]]
    assert candidate([[1, 1, 2, 2, 1, 2]]) == [[8,8,4,4,8,4]]
    assert candidate([[1, 1, 2, 2, 2, 2]]) == [[16,16,8,8,8,8]]
    assert candidate([[1, 1, 3, 3], [3, 4, 4, 2], [6, 6, 3, 4]]) == [[2898,2898,966,966],[966,6897,6897,1449],[483,483,966,6897]]
    assert candidate([[1, 2, 1, 1, 1, 2]]) == [[4,2,4,4,4,2]]
    assert candidate([[1, 2, 1, 1, 2, 2]]) == [[8,4,8,8,4,4]]
    assert candidate([[1, 2, 2, 4, 3], [3, 4, 1, 4, 2]]) == [[4608,2304,2304,1152,1536],[1536,1152,4608,1152,2304]]
    assert candidate([[1, 3, 1, 3, 1], [2, 1, 3, 2, 3]]) == [[324,108,324,108,324],[162,324,108,162,108]]
    assert candidate([[1, 3, 3, 3, 4], [2, 2, 1, 4, 4]]) == [[6912,2304,2304,2304,1728],[3456,3456,6912,1728,1728]]
    assert candidate([[1, 4, 5], [1, 3, 2], [7, 2, 6], [6, 2, 2]]) == [[7365,11100,11349],[7365,6570,9855],[9870,9855,3285],[3285,9855,9855]]
    assert candidate([[1, 6, 6, 4], [4, 1, 2, 5], [5, 4, 6, 2]]) == [[12105,8190,8190,12285],[12285,12105,12225,4890],[4890,12285,8190,12225]]
    assert candidate([[2, 1, 3, 2, 1], [3, 1, 3, 1, 2]]) == [[108,216,72,108,216],[72,216,72,216,108]]
    assert candidate([[2, 2, 2, 1, 1, 1]]) == [[4,4,4,8,8,8]]
    assert candidate([[2, 2, 2, 2, 1, 2]]) == [[16,16,16,16,32,16]]
    assert candidate([[2, 2, 3, 2, 3], [3, 1, 3, 2, 4]]) == [[2592,2592,1728,2592,1728],[1728,5184,1728,2592,1296]]
    assert candidate([[2, 3, 4], [2, 4, 2], [1, 8, 1], [8, 8, 8]]) == [[8697,5798,10521],[8697,10521,8697],[5049,11433,5049],[11433,11433,11433]]
    assert candidate([[2, 4, 4, 5], [5, 5, 1, 4], [4, 2, 2, 5]]) == [[10405,11375,11375,9100],[9100,9100,8465,11375],[11375,10405,10405,9100]]
    assert candidate([[3, 4, 1, 1], [3, 1, 4, 4], [1, 5, 1, 5]]) == [[4800,3600,2055,2055],[4800,2055,3600,3600],[2055,2880,2055,2880]]
    assert candidate([[3, 4, 6, 3], [4, 5, 4, 4], [5, 2, 6, 3]]) == [[11625,11805,11985,11625],[11805,6975,11805,11805],[6975,11265,11985,11625]]
    assert candidate([[4, 1, 4, 4, 4], [2, 2, 2, 3, 3]]) == [[4608,6087,4608,4608,4608],[9216,9216,9216,6144,6144]]
    assert candidate([[4, 8, 8], [6, 2, 5], [7, 3, 7], [6, 3, 5]]) == [[3525,7935,7935],[6465,7050,2820],[7305,585,7305],[6465,585,2820]]
    assert candidate([[6], [8], [2], [12], [6], [4]]) == [[4608],[3456],[1479],[2304],[4608],[6912]]
    assert candidate([[6, 2, 5, 2], [5, 5, 2, 3], [4, 6, 5, 2]]) == [[3990,11970,12195,11970],[12195,12195,11970,7980],[5985,3990,12195,11970]]
    assert candidate([[6, 3, 4, 3], [6, 4, 2, 5], [3, 3, 6, 1]]) == [[9795,7245,8520,7245],[9795,8520,4695,4347],[7245,7245,9795,9390]]
    assert candidate([[6, 5, 6, 6], [3, 2, 6, 4], [1, 3, 4, 1]]) == [[2415,2898,2415,2415],[4830,7245,2415,9795],[2145,4830,9795,2145]]
    assert candidate([[7], [11], [12], [7], [12], [7]]) == [[3546],[12],[8241],[3546],[8241],[3546]]
    assert candidate([[7, 4, 5], [2, 1, 2], [5, 3, 8], [3, 6, 7]]) == [[12135,5805,2175],[11610,10875,11610],[2175,7740,9075],[7740,3870,12135]]
    assert candidate([[8], [6], [7], [2], [7], [4]]) == [[2352],[3136],[2688],[9408],[2688],[4704]]
    assert candidate([[8], [6], [7], [5], [3], [6]]) == [[3780],[5040],[4320],[6048],[10080],[5040]]
    assert candidate([[8, 1], [9, 6], [2, 4], [1, 3], [3, 6]]) == [[10983,1449],[8391,6414],[6897,9621],[1449,483],[483,6414]]
    assert candidate([[8, 4, 3], [7, 7, 4], [1, 2, 3], [5, 2, 4]]) == [[8955,5565,11535],[3180,3180,5565],[9915,11130,11535],[1983,11130,5565]]
    assert candidate([[12], [8], [4], [3], [9], [5]]) == [[4320],[6480],[615],[4935],[5760],[10368]]
    assert candidate([[1, 1, 1, 1, 2, 2, 2]]) == [[8,8,8,8,4,4,4]]
    assert candidate([[1, 1, 1, 2, 1, 1, 1]]) == [[2,2,2,1,2,2,2]]
    assert candidate([[1, 1, 2, 1, 2, 1, 2]]) == [[8,8,4,8,4,8,4]]
    assert candidate([[1, 1, 6, 5, 6], [1, 6, 6, 2, 5], [3, 4, 1, 1, 4]]) == [[11805,11805,12255,4830,12255],[11805,12255,12255,12075,4830],[12165,12210,11805,11805,12210]]
    assert candidate([[1, 2, 1, 1, 1, 2, 2]]) == [[8,4,8,8,8,4,4]]
    assert candidate([[1, 2, 1, 2, 2, 1, 1]]) == [[8,4,8,4,4,8,8]]
    assert candidate([[1, 3, 1, 2, 1, 2], [3, 2, 3, 4, 2, 3]]) == [[5184,1728,5184,2592,5184,2592],[1728,2592,1728,1296,2592,1728]]
    assert candidate([[1, 3, 5, 2], [1, 3, 6, 5], [8, 1, 2, 7], [6, 2, 3, 5]]) == [[2895,9195,10455,7620],[2895,9195,10770,10455],[1905,2895,7620,10995],[10770,7620,9195,10455]]
    assert candidate([[1, 4, 4, 4, 3, 3], [1, 1, 3, 4, 4, 1]]) == [[2958,6912,6912,6912,9216,9216],[2958,2958,9216,6912,6912,2958]]
    assert candidate([[1, 5, 5, 6], [4, 7, 6, 1], [2, 3, 3, 6], [3, 6, 3, 7]]) == [[6570,11190,11190,1095],[7815,11520,1095,6570],[3285,2190,2190,1095],[2190,1095,2190,11520]]
    assert candidate([[1, 6, 4, 4, 1], [6, 2, 5, 1, 4], [6, 4, 3, 5, 6]]) == [[3705,10905,10185,10185,3705],[10905,8025,3210,3705,10185],[10905,10185,9465,3210,10905]]
    assert candidate([[1, 7, 2, 8], [3, 7, 2, 5], [2, 3, 5, 6], [5, 4, 2, 7]]) == [[4065,7635,8205,11310],[9585,7635,8205,8220],[8205,9585,8220,10965],[8220,10275,8205,7635]]
    assert candidate([[2, 1, 1, 1, 1, 2, 2]]) == [[4,8,8,8,8,4,4]]
    assert candidate([[2, 1, 1, 1, 2, 2, 1]]) == [[4,8,8,8,4,4,8]]
    assert candidate([[2, 1, 2, 2, 2, 2, 2]]) == [[32,64,32,32,32,32,32]]
    assert candidate([[2, 1, 3, 2, 4, 4], [1, 3, 2, 2, 4, 1]]) == [[4608,9216,3072,4608,2304,2304],[9216,3072,4608,4608,2304,9216]]
    assert candidate([[2, 2, 2, 2, 1, 2, 1]]) == [[16,16,16,16,32,16,32]]
    assert candidate([[2, 4, 3, 3, 3, 4], [3, 1, 4, 3, 4, 2]]) == [[966,483,8874,8874,8874,483],[8874,1932,483,8874,483,966]]
    assert candidate([[2, 5, 4, 8], [4, 6, 3, 3], [1, 5, 1, 4], [8, 6, 6, 5]]) == [[30,4950,15,6180],[15,4125,8250,8250],[60,4950,60,15],[6180,4125,4125,4950]]
    assert candidate([[2, 7], [10, 12], [2, 4], [8, 11], [2, 12], [11, 2]]) == [[8340,5910],[6606,5505],[8340,4170],[2085,8250],[8340,5505],[8250,8340]]
    assert candidate([[2, 9], [1, 4], [10, 12], [2, 7], [4, 10], [10, 8]]) == [[3435,10365],[6870,7890],[5625,10860],[3435,2745],[7890,5625],[5625,3945]]
    assert candidate([[3], [9], [5], [1], [4], [14], [12]]) == [[5550],[10080],[5799],[4305],[10335],[6480],[7560]]
    assert candidate([[3, 2, 2, 2, 4, 3], [4, 1, 3, 1, 1, 2]]) == [[2304,3456,3456,3456,1728,2304],[1728,6912,2304,6912,6912,3456]]
    assert candidate([[3, 2, 4, 2, 2, 3], [2, 2, 4, 1, 2, 3]]) == [[9216,1479,6912,1479,1479,9216],[1479,1479,6912,2958,1479,9216]]
    assert candidate([[3, 6, 2, 2, 5], [1, 4, 3, 4, 1], [4, 5, 2, 4, 4]]) == [[7590,3795,11385,11385,2085],[10425,11865,7590,11865,10425],[11865,2085,11385,11865,11865]]
    assert candidate([[4, 1, 5, 4, 5], [6, 5, 3, 4, 4], [3, 2, 6, 2, 3]]) == [[6945,3090,8025,6945,8025],[8745,8025,5145,6945,6945],[5145,1545,8745,1545,5145]]
    assert candidate([[4, 3, 9], [3, 9, 10], [9, 7, 8], [8, 4, 7], [6, 1, 3]]) == [[3255,225,75],[225,75,11178],[75,1860,7800],[7800,3255,1860],[6285,675,225]]
    assert candidate([[5, 1, 1, 1, 5], [3, 4, 2, 6, 6], [3, 3, 2, 5, 1]]) == [[6105,5835,5835,5835,6105],[6060,4545,9090,3030,3030],[6060,6060,9090,6105,5835]]
    assert candidate([[5, 3], [9, 2], [2, 6], [4, 9], [12, 2], [10, 4]]) == [[1050,5865],[10185,2625],[2625,9105],[7485,10185],[10725,2625],[525,7485]]


def test_check():
    check(constructProductMatrix)


### Metadata below ###
# question_id = 3031
# question_title = Construct Product Matrix
# question_title_slug = construct-product-matrix
# question_difficulty = Medium
# question_category = Algorithms
# question_likes = 187
# question_dislikes = 11