function findOdd(arr) {
    let nums = {}
    arr.forEach(el => {
        nums[el] ? nums[el]++ : nums[el] = 1
    })
    
    let index = Object.values(nums).findIndex(el => el % 2 !== 0)
    return Object.keys(nums)[index]


  }