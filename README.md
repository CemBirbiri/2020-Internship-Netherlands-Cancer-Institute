# Internship-Netherlands-Cancer-Institute

This repository involves the code of my 2020 summer internship at Netherlands Cancer Institute.
The project is about analysing the ribosome profiling data of skin cancer cells and apply Machine Learning algorithms to classifiy disorderedness levels.

Ribosome profiling is a deep-sequencing-based technique where the detailed analysis 
of the translation can be observed in vivo. In this work, two datasets of ribosome profiling data
especially their corresponding disorederedness levels were used to classify bump and not-bump regions. 
Bump regions are regions where there is a significant chance in disorderedness level probabilities. 
Firstly, bump regions and not-bump regions were selected as arrays of length 34. Then SVM and Random Forest Classifiers 
were used to classify bump and not-bump regions in the 34 dimensional space. 
