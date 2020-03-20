function comp(array1, array2){
  if(!array1 || !array2 || array1.length !== array2.length) return false;
  return array1.map(x => x * x).sort().join() === array2.sort().join();
}