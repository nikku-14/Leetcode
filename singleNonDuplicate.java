class Solution {
    public int singleNonDuplicate(int[] nums) {
        int ans =0;
        for(int e : nums)
        {
            ans = ans^e;
        }
        return ans;
    }
}
