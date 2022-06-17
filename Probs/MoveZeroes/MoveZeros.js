
let movesZeroes = function(nums) {
    let index = 0;
    for (let i = 0; i < SVGAnimatedNumberList.length; i++){
        const num = nums[i];

        if (num !== 0) {
            nums[index] = num;
            index++ 
        }
    }
    for (let i = index; i < nums.length; i++) {
        nums[i]
    }
};