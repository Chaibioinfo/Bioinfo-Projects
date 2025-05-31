Introduction

Nipah virus belongs to Henipavirus genus of the Paramyxoviridae family and is a zoonotic virus with a high case fatality rate. It was first recognized in humans in the Malaysian village of Kampung Sungai Nipah in 1998, initiating a deadly outbreak that lasted through 1999. Nipah virus was first isolated from patients with encephalitis during a 1998–99 epidemic among pig farmers in Malaysia, during which pigs were identified as the source of human infections. Since then, other outbreaks have been reported in south Asia, including in western and northwestern Bangladesh, over the Bangladesh–India border in West Bengal, and in Kerala, India. 
The goal of this project is to perform a comparative genomic analysis of Nipah virus (NiV) strains isolated from different outbreaks, including India, Bangladesh & Singapore, and Malaysia. By aligning their nucleotide sequences and constructing a phylogenetic tree, this study aims to: 

* Compare the genetic similarity and divergence among NiV strains across regions
* Identify mutations and conserved regions that may influence viral function or evolution
* Explore evolutionary relationships to infer patterns of geographic spread and strain origin
* Build a visual phylogenetic tree to illustrate how the strains cluster and differ over time

Methods

Data Retrieval:
Sequences were downloaded from NCBI GenBank using Biopython. Only complete CDS sequences from India, Bangladesh & singapore, and Malaysian strains were collected.

Multiple Sequence Alignment:
Performed using MAFFT. Aligned FASTA file was generated and used for further analysis. Mutation table was obtained from BV-BRC online protal.

Phylogenetic Tree Construction:
A Neighbor-Joining tree was built with bootstrap value of 1000 using MEGA software to determine evolutionary relationships. 


Results

Total sequences analyzed: 80 (only complete genome)

Alignment length: 18252

Total SNP positions: 3391

Total mutations: 3686

Mutation analysis:

The identified mutations provide important insights into the evolutionary dynamics of Nipah virus. The clustering of Indian and Bangladeshi strains with shared SNPs supports their close genetic relationship, while the Malaysian strains formed a genetically distinct clade with a high number of lineage-specific mutations. These findings reinforce the existence of two primary NiV genotypes (NiV-B and NiV-M) high number of mutations between these lineages shows they have been evolving independently, likely with different reservoir dynamics (bat populations), host transmission patterns, and outbreak profiles and demonstrate how mutation patterns reflect viral adaptation, geographic spread, and lineage divergence. Such molecular signatures can be used for outbreak tracking and may inform the development of region-specific diagnostic or therapeutic tools.


Phylogenetic tree Findings:

The most divergent lineage in the phylogenetic tree was the cluster of Malaysian strains clustered at the right bottom of the tree which showed longer branch lengths and formed a separate clade. This supports the established classification of Nipah virus into two major genotypes: the Malaysia genotype (NiV-M) and the Bangladesh genotype (NiV-B). The NiV-M strains are evolutionarily distant from more recent outbreaks observed in Bangladesh and India. The malaysian strains are genetically different from Bangladesh/India strains (NiV-B), 
evolutionarily more ancestral and less adapted for human-to-human transmission. Most nodes have high bootstrap values (99–100%), indicating very strong confidence in those evolutionary relationships.


Discussion 

The comparative genomic analysis of Nipah virus (NiV) strains revealed significant insights into the virus’s evolution and diversity. The alignment and phylogenetic tree confirmed the existence of two major lineages: the Malaysia genotype (NiV-M) and the Bangladesh genotype (NiV-B). Strains from recent outbreaks in India and Bangladesh clustered together tightly, indicating close genetic relationships and minimal divergence, while Malaysian strains formed a distinct, highly divergent clade.

Over 3686 SNPs were detected across an ~18,245 bp region, with several mutation hotspots found in variable genome regions. These mutations reflect the ongoing evolution of the virus and may have implications for transmissibility, virulence, and host adaptation. Some SNPs were unique to specific outbreak strains, suggesting their potential as epidemiological markers for outbreak tracking.

Although this study focused on full genome sequences, further work could explore mutations in specific genes (e.g., G or F glycoproteins), selection pressure, or host-pathogen interaction analysis. Moreover, integrating epidemiological data and host metadata would enhance the biological interpretation of the observed genetic variation.


Conclusion

This project presents a comparative genomic analysis of Nipah virus (NiV) strains from multiple outbreaks, focusing on sequence alignment, SNP identification, and phylogenetic reconstruction. The analysis revealed two major lineages — the Malaysia genotype (NiV-M) and the Bangladesh genotype (NiV-B). Indian isolates were found to cluster closely with Bangladeshi strains, indicating shared evolutionary origins. Over 18,000 base pairs were aligned, and numerous SNPs were identified, including region-specific mutations that may serve as molecular markers. These results underscore the genetic diversity of NiV and highlight the importance of genomic surveillance for understanding its transmission and evolution.




