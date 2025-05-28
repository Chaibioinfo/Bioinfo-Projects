from Bio import Entrez,     SeqIO
Entrez.email = "chaithra.nmurthy@gmail.com" 
query = "Nipah virus[Organism] AND Bangladesh[All Fields] AND complete genome[Title]"
search_handle = Entrez.esearch(db="nucleotide", term=query, retmax=250)
search_results = Entrez.read(search_handle)
search_handle.close()
id_list = search_results["IdList"]
for genbank_id in id_list:
    fetch_handle = Entrez.efetch(db="nucleotide", id=genbank_id, rettype="fasta", retmode="text")
    fasta_data = fetch_handle.read()
    fetch_handle.close()
    filename = f"nipah_{genbank_id}.fasta"
    with open(filename, "w") as f:
        f.write(fasta_data)
    print(f"Saved {filename}")

from Bio import SeqIO
import glob

# Step 1: Collect all FASTA files with "nipah_" prefix
fasta_files = glob.glob("nipah_*.fasta")

# Step 2: Collect all sequence records
all_records = []
for file in fasta_files:
    records = list(SeqIO.parse(file, "fasta"))
    all_records.extend(records)

# Step 3: Write all sequences to one combined FASTA file
with open("combined_nipah.fasta", "w") as output_file:
    SeqIO.write(all_records, output_file, "fasta")

print("All sequences combined into 'combined_nipah.fasta")