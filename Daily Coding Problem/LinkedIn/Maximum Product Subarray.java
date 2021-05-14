// httpsleetcode.comproblemsmaximum-product-subarray
class Solution {
    public int maxProduct(int[] nums) {
        int min = nums[0];        int max = nums[0];
        int prod = nums[0];
        for(int i =1 ;i<nums.length;i++){
            
            if(nums[i] < 0){
                int temp = min;
                min = max;
                max = temp;
            }
            max = Math.max(nums[i] , nums[i] * max);            
            min = Math.min(nums[i] , nums[i] * min);
            prod = Math.max(prod , max);

        }
        return prod;

    }
}