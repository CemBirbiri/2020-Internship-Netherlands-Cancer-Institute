# Internship-Netherlands-Cancer-Institute

This repository involves the report and code of my summer 2020 internship at The Netherlands Cancer Institute. I completed this internship remotely due to the Covid-19 pandemic, under the supervision of [Prof Reuven Agami in the Oncogenomics group](https://www.nki.nl/research/research-groups/reuven-agami/).
The project is about analyzing the ribosome profiling data of melanoma cancer cells and applying machine learning algorithms to classify disorderedness levels.

Ribosome profiling is a deep-sequencing-based technique where the detailed analysis 
of the translation can be observed in vivo. In this work, two datasets of ribosome profiling data
especially their corresponding disorederedness levels were used to classify bump and not-bump regions. The quality control was made using [bowtie2](https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml), [tophat](https://ccb.jhu.edu/software/tophat/index.shtml) and [samtools](http://www.htslib.org/).

Bump regions are regions where there is a significant chance of disorderedness level probabilities. 
Firstly, bump regions and not-bump regions were selected as arrays of length 34. Then SVM and Random Forest Classifiers 
were used to classify bump and not-bump regions in the 34-dimensional space. The corresponding Python implementations and project report can be found in this repository.
