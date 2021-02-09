function isValidSubsequence(array, sequence) {
 # pointer to array
 let arrid=0;
 # pointer to sequence
 let seqid=0;
 
 # pointer less then lenghth of array and sequence
 while (arrid < array.length && seqid < sequence.length){
				if (array[arrid] === sequence[seqid]) seqid++
	        arrid=arrid+1;
				}
        seqid=sequid+1
return seqid === sequence.length
}

exports.isValidSubsequence = isValidSubsequence;

