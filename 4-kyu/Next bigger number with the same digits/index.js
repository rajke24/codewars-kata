function nextBigger(number){
    let digits = number.toString().split('')
    let pivotInd = -1

    for (let i = digits.length; i >=0; i--){
        if(digits[i] > digits[i - 1]){
            pivotInd = i - 1
            break
        }
    }

    if(pivotInd === -1) return pivotInd

    let rightPart = digits.splice(pivotInd)
    
    let diff = 10;
    let numToSwapInd = 0
    let pivValue = rightPart[0]
    for(let i = 1; i < rightPart.length; i++){
        if(rightPart[i] > pivValue){
            let curDiff = rightPart[i] - pivValue
            if (curDiff < diff) {
                diff = curDiff
                numToSwapInd = i
            }
        }
    }
    pivValue = rightPart.splice(numToSwapInd,1)[0]
    rightPart.sort()

    let res = Number(digits.concat([pivValue]).concat(rightPart).join(''))
    
    return res
}