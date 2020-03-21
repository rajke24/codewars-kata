function findOdd(arr) {
    let nums = {}
    arr.forEach(el => {
        nums[el] ? nums[el]++ : nums[el] = 1
    })
    
    Object.values(nums).forEach(el => {
        if(el % 2 !== 0) return el
    })
  }