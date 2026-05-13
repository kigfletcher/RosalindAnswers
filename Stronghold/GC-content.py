from Bio import SeqIO

#Add path to FASTA file here
fa = "/Users/kylefletcher/Downloads/rosalind_gc.txt"

fasta_dict = SeqIO.to_dict(SeqIO.parse(fa, "fasta"))
gc_results = {}
for name, record in fasta_dict.items():
    seq = record.seq
    gc_content = (seq.count('G') + seq.count('C'))/len(seq) * 100
    gc_results[name] = gc_content

#Print ID
print(max(gc_results, key=gc_results.get))
#Print value
print(max(gc_results.values()))