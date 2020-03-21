function step(step, start, end) {
    for(let i = start; i < end; i++){
        if(isPrime(i) && isPrime(i + step)) return [i, i + step]
    }

    return null
}

function isPrime(number){
    if(number < 2) return false
    if(number % 2 === 0) return false
    for(let i = 3; i <= Math.sqrt(number); i+=2){
        if(number % i === 0) return false
    }

    return true
}