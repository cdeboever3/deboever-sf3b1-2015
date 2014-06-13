import os

# File locations
# Rather than specifying paths all over, I'll just put the paths to commonly
# used files and directories here and use the package to open them. 
x = os.getcwd()
root = os.path.join(x.split('deboever-sf3b1-2014')[0], 'deboever-sf3b1-2014')

subdir = 'data'
metadata = os.path.join(root, subdir, 'metadata.tsv')
cosmic_sf3b1 = os.path.join(root, subdir, 'cosmic_sf3b1.tsv')
expressdir = os.path.join(root, subdir, 'express')
sjoutdir = os.path.join(root, subdir, 'sjout')

subdir = 'ext_data'
gencode_gtf = os.path.join(root, subdir, 'gencode',
                           'gencode.v14.annotation.gtf')

subdir = os.path.join('output', 'gencode_sjout_express_processing')
gene_info = os.path.join(root, subdir, 'gene_info.tsv')
transcript_eff_counts = os.path.join(root, subdir, 'transcript_eff_counts.tsv')
gene_eff_counts = os.path.join(root, subdir, 'gene_eff_counts.tsv')
junction_info = os.path.join(root, subdir, 'junction_info.tsv')
transcripts_genes = os.path.join(root, subdir, 'transcripts_genes.tsv')
um_sj_counts = os.path.join(root, subdir, 'um_sj_counts.tsv')
um_sj_annot = os.path.join(root, subdir, 'um_sj_annot.tsv')
