function moreZeros(s){
    if (!s) return []
    return removeDuplicates(s.split('').filter(v=>
    (v.charCodeAt().toString(2).match(/0/g) === null ? 0 : v.charCodeAt().toString(2).match(/0/g).length)>
    (v.charCodeAt().toString(2).match(/1/g) === null ? 0 : v.charCodeAt().toString(2).match(/1/g).length)))
}
    
function removeDuplicates(array) {
  return [...new Set(array)]
}