#!/usr/bin/env python
import sys
from Bio import SeqIO
import re

cov_pattern = re.compile("cov_([0-9.]+)")

min_coverage, fasta_file_path = sys.argv[1:]
with open(fasta_file_path.replace('fa', 'filter{}cov.fa'.format(min_coverage)), 'w') as filtered_fasta:
	with open(fasta_file_path, 'rU') as input_fasta:
		def filtered_contigs_generator(min):
			for contig in SeqIO.parse(input_fasta, 'fasta'):
				result = cov_pattern.search(contig.name)
				if result:
					if float(result.group(1)) >= min:
						yield contig
				
				
		SeqIO.write(filtered_contigs_generator(float(min_coverage)), filtered_fasta, 'fasta')
