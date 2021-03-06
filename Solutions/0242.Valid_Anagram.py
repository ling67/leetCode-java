/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
*/

//python version1 Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = Counter(s)
        arr2 = Counter(t)
        
        if arr1 == arr2:
            return True
        return False

//python version2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxyz')
   

/*
approach 1:sort
approach 2:int count[]
approach 3:hashtable

*/
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }
}
