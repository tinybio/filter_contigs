#!/usr/bin/env python
import sys
from Bio import SeqIO
min_length, fasta_file_path = sys.argv[1:]
with open(fasta_file_path.replace('fa', 'filter{}.fa'.format(min_length)), 'w') as filtered_fasta:
	with open(fasta_file_path, 'rU') as input_fasta:
		def filtered_contigs_generator(min):
			for contig in SeqIO.parse(input_fasta, 'fasta'):
				if len(contig) >= min:
					yield contig
		SeqIO.write(filtered_contigs_generator(int(min_length)), filtered_fasta, 'fasta')
