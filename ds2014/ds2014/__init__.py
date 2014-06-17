import os

import matplotlib.colors as colors
import matplotlib.ticker as tkr
import pandas as pd

# File locations
# Rather than specifying paths all over, I'll just put the paths to commonly
# used files and directories here and use the package to open them. 
x = os.getcwd()
root = os.path.join(x.split('deboever-sf3b1-2014')[0], 'deboever-sf3b1-2014')

## data
subdir = 'data'
metadata = os.path.join(root, subdir, 'metadata.tsv')
cosmic_sf3b1 = os.path.join(root, subdir, 'cosmic_sf3b1.tsv')
sf3b1_mut_info = os.path.join(root, subdir, 'sf3b1_mut_info.tsv')
expressdir = os.path.join(root, subdir, 'express')
sjoutdir = os.path.join(root, subdir, 'sjout')
logfinaldir = os.path.join(root, subdir, 'logfinal')

## ext_data
subdir = 'ext_data'
gencode_gtf = os.path.join(root, subdir, 'gencode',
                           'gencode.v14.annotation.gtf')
gencode_transcripts = os.path.join(root, subdir, 'gencode',
                                   'gencode.v14.pc_transcripts.fa')
gencode_translations = os.path.join(root, subdir, 'gencode',
                                   'gencode.v14.pc_translations.fa')

### gencode_sjout_express_processing
subdir = os.path.join('output', 'gencode_sjout_express_processing')
gene_info = os.path.join(root, subdir, 'gene_info.tsv')
transcript_eff_counts = os.path.join(root, subdir, 'transcript_eff_counts.tsv')
gene_eff_counts = os.path.join(root, subdir, 'gene_eff_counts.tsv')
junction_info = os.path.join(root, subdir, 'junction_info.tsv')
transcripts_genes = os.path.join(root, subdir, 'transcripts_genes.tsv')
star_logs = os.path.join(root, subdir, 'star_logs.tsv')
um_sj_counts = os.path.join(root, subdir, 'um_sj_counts.tsv')
um_sj_annot = os.path.join(root, subdir, 'um_sj_annot.tsv')
um_sj_stats = os.path.join(root, subdir, 'um_sj_stats.tsv')
cll_sj_counts = os.path.join(root, subdir, 'cll_sj_counts.tsv')
cll_sj_annot = os.path.join(root, subdir, 'cll_sj_annot.tsv')
cll_sj_stats = os.path.join(root, subdir, 'cll_sj_stats.tsv')
brca_sj_counts = os.path.join(root, subdir, 'brca_sj_counts.tsv')
brca_sj_annot = os.path.join(root, subdir, 'brca_sj_annot.tsv')
brca_sj_stats = os.path.join(root, subdir, 'brca_sj_stats.tsv')
brca_cll_um_sj_counts = os.path.join(root, subdir, 'brca_cll_um_sj_counts.tsv')
brca_cll_um_sj_annot = os.path.join(root, subdir, 'brca_cll_um_sj_annot.tsv')
brca_cll_um_sj_stats = os.path.join(root, subdir, 'brca_cll_um_sj_stats.tsv')
brca_cll_luad_lusc_um_sj_counts = os.path.join(root, subdir, 
                                               'brca_cll_luad_lusc_um_sj_counts.tsv')
brca_cll_luad_lusc_um_sj_annot = os.path.join(root, subdir, 
                                              'brca_cll_luad_lusc_um_sj_annot.tsv')
brca_cll_luad_lusc_um_sj_stats = os.path.join(root, subdir, 
                                              'brca_cll_luad_lusc_um_sj_stats.tsv')

### dexseq
subdir = os.path.join('output', 'dexseq')
brca_dexseq_results = os.path.join(root, subdir, 'brca_dexseq_results.tsv')
cll_dexseq_results = os.path.join(root, subdir, 'cll_dexseq_results.tsv')
um_dexseq_results = os.path.join(root, subdir, 'um_dexseq_results.tsv')
brca_cll_um_dexseq_results = os.path.join(root, subdir,
                                          'brca_cll_um_dexseq_results.tsv')
brca_cll_luad_lusc_um_dexseq_results = os.path.join(
    root, subdir, 'brca_cll_luad_lusc_um_dexseq_results.tsv')

brca_size_factors = os.path.join(root, subdir, 'brca_size_factors.tsv')
cll_size_factors = os.path.join(root, subdir, 'cll_size_factors.tsv')
um_size_factors = os.path.join(root, subdir, 'um_size_factors.tsv')
brca_cll_um_size_factors = os.path.join(root, subdir,
                                        'brca_cll_um_size_factors.tsv')
brca_cll_luad_lusc_um_size_factors = os.path.join(
    root, subdir, 'brca_cll_luad_lusc_um_size_factors.tsv')

## Other stuff
dexseq_p_cutoff = 0.1

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
        d = {'MUT' : set1.mpl_colors[1], 'WT' : set1.mpl_colors[0]}
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
        True

    if 'ZAP-70' in df.columns:
        True

    return pd.Panel(out)

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass

def _func(x, pos):
    """Formatter function takes tick label and tick position"""
    s = '{:0,d}'.format(int(x))
    return s

comma_format = tkr.FuncFormatter(_func)

def clean_axis(ax):
    "Remove spines and ticks from axis"
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
