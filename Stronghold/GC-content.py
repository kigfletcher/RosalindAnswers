from Bio import SeqIO

#Add path to FASTA file here
fa = "..."

#Can read fasta file directly into the loop
gc_results = {}
for record in SeqIO.parse(fa, "fasta"):
    name = record.id
    seq = str(record.seq)
    gc_content = (seq.count('G') + seq.count('C'))/len(seq) * 100
    gc_results[name] = gc_content

#Obtain best id and then use that to query the dictionary
best_id = (max(gc_results, key=gc_results.get))
best_gc = gc_results[best_id]

print(best_id)
print(best_gc)