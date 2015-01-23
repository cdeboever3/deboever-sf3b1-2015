import ds2014 as ds
from matplotlib.patches import Polygon
from matplotlib.transforms import Bbox
from numpy import arange, log2
import pandas as pd
# import scipy.spatial.distance as dist
# import scipy.cluster.hierarchy as sch

def get_sig_log_dists(res):
    """Get distance to novel acceptors for plotting for significant junctions"""
    df = res[res.novel_acceptor]
    t = log2(df.ix[((df.padjust < ds.dexseq_p_cutoff) & 
                    (df['log2fold(WT/MUT)'] < 0)),
                    'downstream_acceptor_dist'].dropna())
    t2 = log2(df.ix[((df.padjust < ds.dexseq_p_cutoff) &
                     (df['log2fold(WT/MUT)'] < 0)),
                     'upstream_acceptor_dist'].dropna())
    s = set(t.index) & set(t2.index)
    t2 = t2.drop(s)
    mut_dists = pd.concat([-1 * t, t2])
    t = log2(df.ix[((df.padjust < ds.dexseq_p_cutoff) &
                    (df['log2fold(WT/MUT)'] > 0)),
                    'downstream_acceptor_dist'].dropna())
    t2 = log2(df.ix[((df.padjust < ds.dexseq_p_cutoff) &
                     (df['log2fold(WT/MUT)'] > 0)),
                     'upstream_acceptor_dist'].dropna())
    s = set(t.index) & set(t2.index)
    t2 = t2.drop(s)
    wt_dists = pd.concat([-1 * t, t2])
    return mut_dists, wt_dists

def get_not_sig_log_dists(res):
    """Get distance to novel acceptors for plotting for non-significant
    junctions"""
    df = res[res.novel_acceptor]
    t = log2(df.ix[((df.padjust > ds.dexseq_p_cutoff) & 
                    (df['log2fold(WT/MUT)'] < 0)),
                    'downstream_acceptor_dist'].dropna())
    t2 = log2(df.ix[((df.padjust > ds.dexseq_p_cutoff) &
                     (df['log2fold(WT/MUT)'] < 0)),
                     'upstream_acceptor_dist'].dropna())
    s = set(t.index) & set(t2.index)
    t2 = t2.drop(s)
    mut_dists = pd.concat([-1 * t, t2])
    t = log2(df.ix[((df.padjust > ds.dexseq_p_cutoff) &
                    (df['log2fold(WT/MUT)'] > 0)),
                    'downstream_acceptor_dist'].dropna())
    t2 = log2(df.ix[((df.padjust > ds.dexseq_p_cutoff) &
                     (df['log2fold(WT/MUT)'] > 0)),
                     'upstream_acceptor_dist'].dropna())
    s = set(t.index) & set(t2.index)
    t2 = t2.drop(s)
    wt_dists = pd.concat([-1 * t, t2])
    return mut_dists, wt_dists

def plot_hist(res, ax, mut_color, wt_color, 
              letter_label=None, significant=True,
              mut=True, wt=True, legend_loc='upper left',
              ylabel=True):
    """
    Plot distance from cryptic acceptor to canonical acceptor
    
    significant : If True, use significant junctions. If False, use 
                  non-significant genes.
    """
    if significant:
        mut_dists, wt_dists = get_sig_log_dists(res)
    else:
        mut_dists, wt_dists = get_not_sig_log_dists(res)
    if mut_dists.shape[0] > 0 and mut:
        ax.hist(mut_dists, bins=arange(-20, 21.25, 0.25),
                alpha=0.5, label='MUT$\uparrow$',
                histtype='stepfilled', linewidth=0,
                fc=mut_color, zorder=5)
    if wt_dists.shape[0] > 0 and wt:
        ax.hist(wt_dists, bins=arange(-20, 21.25, 0.25),
                alpha=0.5, label='WT$\uparrow$',
                histtype='stepfilled', linewidth=0,
                fc=wt_color, zorder=5)
    if mut and wt:
        print('{:,} 3\'SSs in histogram'.format(mut_dists.shape[0] + wt_dists.shape[0]))
    elif mut:
        print('{:,} mut 3\'SSs in histogram'.format(mut_dists.shape[0]))
    elif wt:
        print('{:,} wt 3\'SSs in histogram'.format(wt_dists.shape[0]))
    x = ax.set_xlabel('$\log_2$ distance (bp) from associated canonical 3\'SS')
    if ylabel:
        ax.set_ylabel('Number novel 3\'SSs')
    else:
        ax.set_ylabel('Number\nnovel 3\'SSs')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    for l in ax.get_xticklines() + ax.get_yticklines(): 
        l.set_markersize(0)
    lgd = ax.legend(loc=legend_loc, frameon=False)
    ax.xaxis.set_major_formatter(ds.comma_format)
    ax.yaxis.set_major_formatter(ds.comma_format)
    
    if letter_label:
        offset = 0.1 * (ax.get_xlim()[1] - ax.get_xlim()[0])
        t = ax.text(ax.get_xlim()[0] - offset, 
                    ax.get_ylim()[1], 
                    letter_label, 
                    size=ds.subfigure_label_fontsize)
    return ax

def plot_polygon(ax, fig):
    ymin, ymax = ax.get_ylim()
    xy = [[-1 * log2(50), 0],
          [5, ymax * 0.35],
          [20, ymax * 0.35],
          [0, 0]]
    poly = Polygon(xy, facecolor='#E6E6E6',
               edgecolor='none', zorder=1)
    ax.add_patch(poly)
    bb_data = Bbox.from_bounds(5, ymax * 0.35, 15, ymax * 0.55)
    disp_coords = ax.transData.transform(bb_data)
    fig_coords = fig.transFigure.inverted().transform(disp_coords)
    ax2 = fig.add_axes(Bbox(fig_coords), zorder=5)
    return ax, ax2

def plot_little_hist(res, ax, mut_color, wt_color, halve_yticks=False):
    df = res[res.novel_acceptor]
    t = -1 * df.ix[((df.padjust < ds.dexseq_p_cutoff) & 
                    (df['log2fold(WT/MUT)'] < 0)),
                    'downstream_acceptor_dist'].dropna()
    ax.hist(t[(t <= 0) & (t >= -50)],
            bins=range(-50, 1), alpha=0.5, 
            histtype='stepfilled', linewidth=0,
            fc=mut_color)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    for l in ax.get_xticklines() + ax.get_yticklines(): 
        l.set_markersize(0)
    if halve_yticks:
        ax.set_yticks(ax.get_yticks()[0::2])
    ax.xaxis.set_major_formatter(ds.comma_format)
    ax.yaxis.set_major_formatter(ds.comma_format)
