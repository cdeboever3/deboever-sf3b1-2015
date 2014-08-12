deboever-sf3b1-2014
===================

This repository is designed to allow for the replication of [XXX paper]
starting *after* some of the time intensive steps such as read-mapping,
expression estimation, etc.  Information on the time intensive steps is
available in the methods section of the paper.

This git repository holds IPython notebooks and code needed to replicate the
study.  Additional data are available in this Figshare
[fileset](http://dx.doi.org/10.6084/m9.figshare.1120663) and must be downloaded
before attempting to replicate the study. After cloning this Github repository,
you can use the `figshare_download` notebook to download the data from
Figshare.

If you have any trouble replicating the results, please let me know using
Github's issues. If you are having trouble installing dependencies, try the
help resources for those software.

### Overview

Here are the steps that you'll need to follow for inspecting the code and 
replicating the study:

* clone this repository from Github
* install dependencies
* use `figshare_download` notebook to download data from Figshare
* use `ext_data` notebook to download data from external sources
* run desired notebooks

### Cloning from Github

You can clone this repository using the button on the side of the page. It is
important that you don't change the name of the repository (e.g.
deboever-sf3b1-2014).

### Dependencies

There are a few non-Python dependencies but these are usually only used in one
notebook. I'll point those out in the respective notebooks.

#### Python

A working IPython notebook environment is needed along with some of the common
scientific Python packages that you likely already have as part of a working
IPython notebook environment. I recommend using 
[Anaconda Python](https://store.continuum.io/cshop/anaconda/) since it includes
most of the needed packages. You will need to use the `pylab` flag when running 
the notebooks. Besides the default Anaconda packages, you will need

* pybedtools
* [cdpybio](https://Github.com/cdeboever3/cdpybio)

You can download cdpybio from its [Github
repo](https://Github.com/cdeboever3/cdpybio) and install using `python setup.py
install`. 

You will also need to install the project specific Python package ds2014 from
this repository. From the `deboever-sf3b1-2014` directory, you can change into
`ds2014` and install using `python setup.py install` or `python setup.py
develop` if you think you may want to make changes to the ds2014 package and
have these changes instantly propagated.

### Downloading data from Figshare and external sources

After cloning the repository and installing the dependencies, you should be
able to just run the `figshare_download` and `ext_data` notebooks to download
the necessary data.

### Running notebooks

The IPython notebooks for this project are somewhat ordered in how they should
be run because some notebooks rely on the output of other notebooks. However,
all of the intermediate files are downloaded from Figshare so you should be
able to run any notebook initially. Note that some notebooks will not actually
recreate their output files if the files already exists:

	if not os.path.exists([some output file]):
		[do analysis]
	else:
		[read output file that already exists]

You can delete (or better, rename or move) output files to ensure they are
recreated when you run a given notebook.

### Directory structure

##### data  

Downloaded from Figshare. Contains primary data files (i.e. those that aren't
created by any of the code here). You shouldn't delete or alter these.

##### ds2014

This directory contains a Python package specific to this project. See the
Dependencies section of this README for installation instructions.

##### ext_data

This directory holds data downloaded externally that I trust will still be
available in the future. These data are downloaded using the `ext_data`
notebook.  There may be some other notebooks that store data in here too but I
don't think so.

##### notebooks  

IPython notebooks tracked by git. Use these to rerun different analyses.

##### output  

Output from IPython notebooks. Contains intermediate files (i.e. files that are
created using the primary data and other external data) as well as images,
table, etc. For figures that require some Illustrator manipulation (currently
Figures 2 and 3), I try to copy the final figure into the output folder as
well.

##### software

This directory contains non-Python software. Most of these software are only 
used in one notebook so the details are contained within those respective
notebooks.

### Numbers from paper

The notebook `numbers_from_paper.ipynb` contains commands that print most of
numbers/statistics in the paper. Numbers in the figure legends are printed out
in the figure notebooks however (although they may be duplicated in
`number_from_paper.ipynb`).

### Figures

Each figure has its own notebook (e.g. `figure01.ipynb` or `sfigure01.ipynb`).
These notebooks create the entire figure in go except for a couple cases where
some parts of the figure have to be inserted manually. The things to be
inserted manually are either created by the notebook and saved in its output
folder or they are available in the `data` directory from Figshare.

### Terminology

In the manuscript, I refer to 3' splice sites only as 3' splice sites or
3'SSs. However, in the code and notebooks for this project, I sometimes refer
to them as acceptors. Similarly, I refer to 5' splice sites as donors in the
code and notebooks in some cases. I generally try to "junction" to refer to a
gap spanned in the RNA-seq data and "splice site" to refer to an annotated or
cryptic splice site.

In the manuscript, I refer to 3'SSs or other features annotated in Gencode as
"canonical." However, I may refer to these as "annotated" (or "annot" for
short) in the code and notebooks at various points. I also refer to cryptic
3'SSs as "novel" splice sites in some places.
