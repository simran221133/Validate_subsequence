function isValidSubsequence(array, sequence) {
//pointer to array  
let arrid=0;
//pointer to sequence
let seqid=0;

//pointer less then lenghth of array and sequence
while (arrid < array.length && seqid < sequence.length){
       if (array[arrid] === sequence[seqid])
         arrid=arrid+1;
    }
    seqid=seqid+1
return sequence === sequence.length
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;
