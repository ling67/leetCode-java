/*
描述
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

The unit of length is centimeter.The length of the woods are all positive integers,you couldn't cut wood into float length.If you couldn't get >= k pieces, return 0.

样例
Example 1

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Example 2

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.
挑战
O(n log Len), where Len is the longest length of the wood.
*/

from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def wood_cut(self, l: List[int], k: int) -> int:
        if not l:
            return 0
        start, end = 1, max(l)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.getcnt(l, mid, k):
                start = mid
            else:
                end = mid
        if self.getcnt(l, end, k):
            return end
        if self.getcnt(l, start, k):
            return start
        return 0
    
    def getcnt(self, l, length, k):
        cnt = 0
        for wood in l:
            cnt += wood // length
        return True if cnt >= k else False 


/********************************************java version*******************************************/

public class Solution {
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */
    public int woodCut(int[] L, int k) {
        // write your code here
        int max = 0;
        for (int i = 0; i < L.length; i++) {
            max = Math.max(max, L[i]);
        }

        int start = 1, end = max;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (count(L, mid) >= k) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (count(L, end) >= k) {
            return end;
        }
        if (count(L, start) >= k) {
            return start;
        }
        return 0;
    }

    private int count (int[] L, int lendth) {
        int sum = 0;
        for (int i = 0; i < L.length; i++){
            sum += L[i] / length;
        }
    }

}
