const twoSum = (nums, target) => {
    for (i=0; i<nums.length; i++){
        for (j=0; j<nums.length; j++){
            if (nums[i] + nums[j] == target) {
                if (i == j) {
                    break;
                } 
                else {
                    return [i, j];
                }
            }
        }
    }
}

nums = [2,4,3,8,6];
target = 12;

const tes = twoSum(nums, target);

console.log(tes);