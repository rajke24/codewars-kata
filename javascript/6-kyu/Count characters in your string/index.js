function count (string) {  
    let obj = {};   
    string.split('').forEach(s => {
    obj[s] ? obj[s]++ : obj[s] = 1
});
      return obj;
}
   