function partsSums(ls) {
    let arr = [0];
    for(let i = ls.length - 1; i >= 0; i--){
        arr.push(arr[arr.length - 1] + ls[i] )
    }
    return arr.reverse()
  }