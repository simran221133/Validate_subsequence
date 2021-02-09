function isValidSubsequence(array, sequence) {
let arrid=0;
let seqid=0;
while (arrid < array.length && seqid < sequence.length){
  if (array[arrid] === sequence[seqid])
    arrid=arrid+1;
    }
    seqid=seqid+1
  return sequence === sequence.length
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;
