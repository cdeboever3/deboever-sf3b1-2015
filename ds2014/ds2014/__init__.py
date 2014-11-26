import os
from os.path import join

from Bio.Seq import Seq
import matplotlib.colors as colors
import matplotlib.ticker as tkr
import numpy as np
import pandas as pd
import pybedtools as pbt
import subprocess

# File locations
# Rather than specifying paths all over, I'll just put the paths to commonly
# used files and directories here and use the package to open them. 
x = os.getcwd()
root = join(x.split('deboever-sf3b1-2014')[0], 'deboever-sf3b1-2014')

## data
subdir = join(root, 'data')
metadata = join(subdir, 'metadata.tsv')
ighv_zap70 = join(subdir, 'ighv_zap70.tsv')
cosmic_sf3b1 = join(subdir, 'cosmic_sf3b1.tsv')
sf3b1_mut_info = join(subdir, 'sf3b1_mut_info.tsv')
expressdir = join(subdir, 'express')
sjoutdir = join(subdir, 'sjout')
logfinaldir = join(subdir, 'logfinal')
ferreira_sfile3 = join(subdir, 'Supplemental_File3_Splicingtable.xls')

### cancer_databases
subdir = join(root, 'data', 'cancer_databases')
cancer_gene_census = join(subdir, 'cancer_gene_census.tsv')
cancer_genes = join(subdir, 'cancergenes.txt')
ts_genes = join(subdir, 'Human_716_TSGs.txt')

## ext_data
subdir = join(root, 'ext_data')
gencode_gtf = join(subdir, 'gencode',
                           'gencode.v14.annotation.gtf')
gencode_transcripts = join(subdir, 'gencode',
                                   'gencode.v14.pc_transcripts.fa')
gencode_translations = join(subdir, 'gencode',
                                   'gencode.v14.pc_translations.fa')
hg19 = join(subdir, 'hg19.fa')

## output

### gencode_sjout_express_processing
subdir = join(root, 'output', 'gencode_sjout_express_processing')
gene_info = join(subdir, 'gene_info.tsv')
transcript_eff_counts = join(subdir, 'transcript_eff_counts.tsv')
gene_eff_counts = join(subdir, 'gene_eff_counts.tsv')
transcript_fpkm = join(subdir, 'transcript_fpkm.tsv')
gene_fpkm = join(subdir, 'gene_fpkm.tsv')
junction_info = join(subdir, 'junction_info.tsv')
transcripts_genes = join(subdir, 'transcripts_genes.tsv')
star_logs = join(subdir, 'star_logs.tsv')
um_sj_counts = join(subdir, 'um_sj_counts.tsv')
um_sj_annot = join(subdir, 'um_sj_annot.tsv')
um_sj_stats = join(subdir, 'um_sj_stats.tsv')
cll_sj_counts = join(subdir, 'cll_sj_counts.tsv')
cll_sj_annot = join(subdir, 'cll_sj_annot.tsv')
cll_sj_stats = join(subdir, 'cll_sj_stats.tsv')
brca_sj_counts = join(subdir, 'brca_sj_counts.tsv')
brca_sj_annot = join(subdir, 'brca_sj_annot.tsv')
brca_sj_stats = join(subdir, 'brca_sj_stats.tsv')
brca_cll_um_sj_counts = join(subdir, 'brca_cll_um_sj_counts.tsv')
brca_cll_um_sj_annot = join(subdir, 'brca_cll_um_sj_annot.tsv')
brca_cll_um_sj_stats = join(subdir, 'brca_cll_um_sj_stats.tsv')
brca_cll_luad_lusc_um_sj_counts = join(subdir, 'brca_cll_luad_lusc_um_sj_counts.tsv')
brca_cll_luad_lusc_um_sj_annot = join(subdir, 'brca_cll_luad_lusc_um_sj_annot.tsv')
brca_cll_luad_lusc_um_sj_stats = join(subdir, 'brca_cll_luad_lusc_um_sj_stats.tsv')

### deseq2
subdir = join(root, 'output', 'deseq2')
brca_cll_um_deseq2_size_factors = join(subdir, 'brca_cll_um_deseq2_size_factors.tsv')
brca_cll_um_deseq2_results = join(subdir, 'brca_cll_um_results.csv')
brca_cll_um_deseq2_sig_genes = join(subdir, 'brca_cll_um_sig_genes.tsv')
cll_deseq2_size_factors = join(subdir, 'brca_cll_um_deseq2_size_factors.tsv')
cll_deseq2_results = join(subdir, 'cll_results.csv')

### dexseq
subdir = join(root, 'output', 'dexseq')
brca_dexseq_results = join(subdir, 'brca_dexseq_results.tsv')
cll_dexseq_results = join(subdir, 'cll_dexseq_results.tsv')
um_dexseq_results = join(subdir, 'um_dexseq_results.tsv')
brca_cll_um_dexseq_results = join(subdir, 'brca_cll_um_dexseq_results.tsv')
brca_cll_luad_lusc_um_dexseq_results = join(subdir, 'brca_cll_luad_lusc_um_dexseq_results.tsv')
brca_dexseq_size_factors = join(subdir, 'brca_size_factors.tsv')
cll_dexseq_size_factors = join(subdir, 'cll_size_factors.tsv')
um_dexseq_size_factors = join(subdir, 'um_size_factors.tsv')
brca_cll_um_dexseq_size_factors = join(subdir, 'brca_cll_um_size_factors.tsv')
brca_cll_luad_lusc_um_dexseq_size_factors = join(subdir, 'brca_cll_luad_lusc_um_size_factors.tsv')
brca_cll_um_psi = join(subdir, 'brca_cll_um_psi.tsv')
cll_psi = join(subdir, 'cll_psi.tsv')
brca_psi = join(subdir, 'brca_psi.tsv')

### branch_point_analysis
subdir = join(root, 'output', 'branch_point_analysis')
proximal_jxns = join(subdir, 'proximal_jxns.tsv')
not_proximal_jxns = join(subdir, 'not_proximal_jxns.tsv')
distal_jxns = join(subdir, 'distal_jxns.tsv')
annot_jxns = join(subdir, 'annot_jxns.tsv')
control_jxns = join(subdir, 'control_jxns.tsv')

proximal_to_annot = join(subdir, 'proximal_to_annot.tsv')

proximal_intron_seq = join(subdir, 'proximal_intron_seq.fa')
not_proximal_intron_seq = join(subdir, 'not_proximal_intron_seq.fa')
distal_intron_seq = join(subdir, 'distal_intron_seq.fa')
annot_intron_seq = join(subdir, 'annot_intron_seq.fa')
control_intron_seq = join(subdir, 'control_intron_seq.fa')

proximal_all_bp = join(subdir, 'proximal_all_bp.tsv')
not_proximal_all_bp = join(subdir, 'not_proximal_all_bp.tsv')
distal_all_bp = join(subdir, 'distal_all_bp.tsv')
annot_all_bp = join(subdir, 'annot_all_bp.tsv')
control_all_bp = join(subdir, 'control_all_bp.tsv')

proximal_single_bp = join(subdir, 'proximal_single_bp.tsv')
not_proximal_single_bp = join(subdir, 'not_proximal_single_bp.tsv')
distal_single_bp = join(subdir, 'distal_single_bp.tsv')
annot_single_bp = join(subdir, 'annot_single_bp.tsv')
control_single_bp = join(subdir, 'control_single_bp.tsv')

proximal_single_bp_second = join(subdir, 'proximal_single_bp_second.tsv')
annot_single_bp_second = join(subdir, 'annot_single_bp_second.tsv')

control_ag_dists = join(subdir, 'control_ag_dists.txt')

### susceptible_introns
subdir = join(root, 'output', 'susceptible_introns')
not_sig_intron_seq = join(subdir, 'introns.fa')
not_sig_all_bp = join(subdir, 'bps.tsv')

### psi_analysis
subdir = join(root, 'output', 'psi_analysis')
psi5 = join(subdir, 'psi5.tsv')
psi3 = join(subdir, 'psi3.tsv')

## Other stuff
figshare_article_id = '1120663'
figshare_manifest = join(root, 'manifest.tsv')
subfigure_label_fontsize = 10
dexseq_p_cutoff = 0.1
deseq2_p_cutoff = 0.1

### Clinical cutoffs for CLL
#### ROR1 expression above this values is ROR1+
ror1_cutoff = 0.8 
#### ZAP-70 expression above this value is considered ZAP-70+
zap70_cutoff = 0.2 
#### IGHV homology above this value is considered unmutated
ighv_cutoff = 0.98 

def make_color_panel(df):
    """Map categorical values to colors"""
    import brewer2mpl
    set1 = brewer2mpl.get_map('Set1','Qualitative',9)
    dark2 = brewer2mpl.get_map('Dark2','Qualitative',8)
    out = {}
    if 'condition' in df.columns:
        d = {'MUT' : set1.mpl_colors[0], 'WT' : set1.mpl_colors[1]}
        out['condition']  = pd.DataFrame([ d[x] for x in df.condition ],
                                         index=df.index)
    
    if 'disease_abbr' in df.columns:
        d = {'BRCA' : dark2.mpl_colors[0], 'CLL' : dark2.mpl_colors[2],
             'LUAD' : dark2.mpl_colors[1], 'LUSC' : dark2.mpl_colors[3],
             'UM' : dark2.mpl_colors[-2]}
        out['disease_abbr'] = pd.DataFrame([ d[x] for x in df.disease_abbr ],
                                           index=df.index)
    
    if 'HEAT 5-9' in df.columns:
        d = {True:dark2.mpl_colors[-3], False:(1,1,1)}
        out['HEAT 5-9'] = pd.DataFrame([ d[x] for x in df['HEAT 5-9']],
                                       index=df.index)

    if 'IGHV' in df.columns:
        d = {'mutated':set1.mpl_colors[2], 'unmutated':set1.mpl_colors[3]}
        out['IGHV'] = pd.DataFrame([ d[x] for x in df['IGHV']],
                                       index=df.index)

    if 'ZAP70' in df.columns:
        d = {'positive':set1.mpl_colors[4], 'negative':set1.mpl_colors[6]}
        out['ZAP70'] = pd.DataFrame([ d[x] for x in df['ZAP70']],
                                       index=df.index)

    return pd.Panel(out)

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass

def _comma_func(x, pos):
    """
    Formatter function takes tick label and tick position.
    """
    s = '{:0,d}'.format(int(x))
    return s

# Use: ax.yaxis.set_major_formatter(ds.comma_format)
comma_format = tkr.FuncFormatter(_comma_func)

def _string_func(x, pos):
    """
    Formatter function takes tick label and tick position.
    """
    return str(x)

# Use: ax.yaxis.set_major_formatter(ds.string_format)
string_format = tkr.FuncFormatter(_string_func)

## Functions used throughout project
# These are functions that are used in more than one notebook.

def clean_axis(ax):
    "Remove spines and ticks from axis"
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)

def predict_branch_points(intron_fasta):
    lines = subprocess.check_output([os.path.join(root, 'software', 
                                                  'svm-bpfinder', 
                                                  'svm_bpfinder.py'),
                                     intron_fasta, 'Hsap', '50'])
    lines = [ x.split('\t') for x in lines.strip().split('\n') ]
    return pd.DataFrame(lines[1:],
                        columns=lines[0]).convert_objects(convert_numeric=True)

def make_uniq_bp_results(all_bp):
    assert all_bp.ss_dist.dtype == int
    df = all_bp.sort(['seq_id', 'bp_scr'], 
                     ascending=False).drop_duplicates('seq_id')
    df.index = list(df.seq_id)
    return df

def get_annotated_jxn(row):
    """
    Define the downstream annotated junction for a 
    junction with a novel acceptor using a row
    from the results table
    """
    if row['strand'] == '+':        
        return '{}:{}-{}:{}'.format(
            row['chrom'], row['start'],
            row['end'] + int(row['downstream_acceptor_dist']), row['strand']
        )
    if row['strand'] == '-':
        return '{}:{}-{}:{}'.format(
            row['chrom'], 
            row['start'] - int(row['downstream_acceptor_dist']), row['end'],
            row['strand']
        )

def psi_df(results, counts):
    df = results[(results.padjust < dexseq_p_cutoff) &
                 (results.downstream_acceptor_dist <= 30) &
                 (results.downstream_acceptor_dist >= 10) &
                 (results['log2fold(MUT/WT)'] > 0)]

    annot_jxns = pd.Series(
        results.ix[df.index].apply(lambda x: get_annotated_jxn(x), axis=1))
    psi = (counts.ix[annot_jxns.index].values / 
           (counts.ix[annot_jxns.index].values + 
            counts.ix[annot_jxns.values].values))
    psi = pd.DataFrame(psi, index=annot_jxns.index,
                       columns=counts.columns)
    psi = psi.dropna(how='all')
    psi = psi.replace(np.nan, 0)
    return psi
