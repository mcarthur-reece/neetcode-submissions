class Solution {
    public boolean hasDuplicate(int[] nums) {
        if(nums.length == 0){return false;}
        int[] sets = new int[nums.length];
        Arrays.sort(nums);
        sets[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] == sets[i - 1]){
                return true;
            }
            sets[i] = nums[i];
        }
        return false;
    }
}
