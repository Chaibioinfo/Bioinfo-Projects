from Bio import AlignIO

# Load the aligned FASTA file
alignment = AlignIO.read("aligned fasta.fasta", "fasta")
alignment_length = alignment.get_alignment_length()
print(f"Alignment length: {alignment_length}")

# Dictionary to store mutation counts at each position
mutation_counts = {}

for pos in range(alignment_length):
    position = pos + 1  # Convert to 1-based indexing
    bases = set()
    
    for record in alignment:
        base = record.seq[pos].upper()
        if base != '-':  # Ignore gaps
            bases.add(base)
    
    # If there's more than one base type (excluding gaps), it's a SNP
    if len(bases) > 1:
        mutation_counts[position] = len(bases) - 1  # Number of alternative bases

# Output results
total_snp_positions = len(mutation_counts)
total_mutations = sum(mutation_counts.values())

print(f"\nTotal SNP positions: {total_snp_positions}")
print(f"Total mutations: {total_mutations}\n")

# Write detailed output to file
with open("mutation_counts.txt", "w") as out:
    out.write("Position\tReference_Base\tAlternative_Bases\tMutation_Count\n")
    
    # To determine reference base (using the first sequence as reference)
    ref_seq = alignment[0].seq
    
    for pos in sorted(mutation_counts.keys()):
        ref_base = ref_seq[pos-1].upper()
        
        # Get all observed bases at this position
        bases = set()
        for record in alignment:
            base = record.seq[pos-1].upper()
            if base != '-':
                bases.add(base)
        
        alt_bases = [b for b in bases if b != ref_base]
        out.write(f"{pos}\t{ref_base}\t{', '.join(alt_bases)}\t{mutation_counts[pos]}\n")

print("Detailed mutation counts saved to 'mutation_counts.txt'")