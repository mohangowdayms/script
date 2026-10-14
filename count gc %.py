from bio import seqIO
#read the fasta file
for record in seqIO.parse("sequence.fasta", "fasta"):
    #get sequence id
    seq_id = record.id
    #get sequence length
    length = len(record.seq)
    #calculate GC content
    gc_content = ( 
        record.seq.count("G") + record.seq.count("C"))/length 
    ) * 100
# display the results
print("ID:", seq_id)
print("length:", length)
print("GC content: {:.2f}%".format(gc_content))
print()