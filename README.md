# Template-computo-quarto

[![build output](https://github.com/computorg/template-computo-quarto/workflows/build/badge.svg)](https://computorg.github.io/template-computo-quarto/)

Documentation and sample of a [Quarto-based](https://quarto.org) submission for the Computo journal (_requires that Quarto is installed on your computer_).

Shows how to automatically setup and build the HTML and PDF outputs, ready to submit to our peer-review platform.

## Process overview

Submissions to Computo require both scientific content (typically equations, codes and figures) and a proof that this content is reproducible. This is achieved via [Quarto](https://quarto.org), which can be used on its own as a notebook system, but also to handle the standard notebook formats like ipynb or Rmarkdown. 

A Computo submission is thus a git(hub) repository like this one typically containing 

- the source of the notebook (a markdown file with metadata + a BibTeX + some statics files typically in `figs/`)
- configuration files for the binder environment to build the final notebook files in HTML (`environment.yml`). 

## Step-by-step procedure

### Step 0: setup a github repository

This can be simply achieved by using this repository as a template, via the "use this template" button on the top of this page.

**Note**: _You can rename the files at your convenience, but we suggest you to keep the name of the config files unchanged, unless you know what you are doing._

### Step 1. write your contribution 

Write your notebook as usual, as demonstrated in the `template-computo-quarto.qmd` sample. More advanced featrues are examplfied [in this page](https://computo.sfds.asso.fr/computo-quarto-extension/) or in our [remake fo the t-SNE paper](https://computo.sfds.asso.fr/published-paper-tsne/)?

**Note**: _Make sure that you are able to build your manuscript as a regular notebook on your system before proceeding to the next step._

The final rendering can be obtained on your local machine by adding the Computo extension for quarto as follows

```bash
quarto add computorg/computo-quarto-extension
```

### Step 2: configure your environement

The file `environment.yml` tells how to setup the machine used to build your notebook with a conda environment. It must be configured to have all the dependencies required to run you notebook (R/Python/Julia packages/feedstocks and system dependencies).

The default uses conda-forge and includes a couple of popular Python and R packages, since quarto supports both 'knitr' and 'jupyter' to coompile your notebook:

``` yaml
name: computorbuild
channels:
  - conda-forge
dependencies:
  - jupyter
  - matplotlib
  - numpy
  - r-base=4.1.1
  - r-knitr
  - r-plotly
  - r-tidyverse
  - r-reticulate
```

The available feedstocks (Python modules and R packages) for conda-forge are listed here: [https://conda-forge.org/feedstock-outputs/index.html](https://conda-forge.org/feedstock-outputs/index.html).

### Step 3: proof reproducibility

It is now time to put everything together and check that your work is indeed reproducible! 

To this end, you need to rely on a github action, whose default is found here: [.github/workflows/build.yml](https://github.com/computorg/template-computo-quarto/blob/main/.github/workflows/build.yml)

This action will

- Check out repository for Github action on a Ubuntu machine
- Set up the Python and R dependencies specified in `environment.yml` with Micromambda
- Render your qmd file to HTML and to PDF
- Deploy your HTML (https://computorg.github.io/template-computo-quarto/) and PDF (https://computorg.github.io/template-computo-quarto/content.pdf) on a github page on the gh-page branch

_It is all pre-setup for you, so you hopefully don't need to modify, except if you change the name of your notebook: you must then set up the  'quarto_file' variable appropriately_

### Step 4. submit

Once step 3 is successful, you should end up with an HTML version published as a gh-page and a PDF version named `content.pdf` at the root of the gh-page repository. This PDF version can be submitted to the [Computo submission platform](https://computo.scholasticahq.com/):

<div id="scholastica-submission-button" style="margin-top: 10px; margin-bottom: 10px;"><a href="https://computo.scholasticahq.com/for-authors" style="outline: none; border: none;"><img style="outline: none; border: none;" src="https://s3.amazonaws.com/docs.scholastica/law-review-submission-button/submit_via_scholastica.png" alt="Submit to Computo"></a></div>

