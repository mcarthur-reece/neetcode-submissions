class Solution {
    public int removeDuplicates(int[] nums) {
        TreeSet<Integer> hash = new TreeSet<>();
        for(int num: nums){
            hash.add(num);
        }
        int i = 0;
        for (int num : hash) {
            nums[i++] = num;
        }
       
        return hash.size();
    }
}