# DonorsChoose

An Experiment with DonorsChoose projects data
==============================================

Kaggle recently opened up a competition to help DonorChoose with targeted marketing. Since I am relatively new to the ML libraries, I decided to make up a project of my own. The goal of the project is to ascertain whether there is a correlation between the category the project belongs to, the kind of resources they ask for and similar other parameters and the total donation these projects accumulate.

I am using the Projects.csv and Donations.csv files for this experiment and are available at:https://www.kaggle.com/donorschoose/datasets .To run the experiments, execute files in the order step1.py -> step2.py -> step3.py.

I am modelling the regression problem where the independent variables are ('Project Cost', 'Project Subject Category Tree', 'Project Grade Level Category', 'Project Resource Category') and the variable to predict is the fraction of the total cost that is funded. Note that this variable is bounded between 0 and 1. For this reason, I am using logistic regression with multiple classes as the predictor. All the possible values that the dependent variable can take can divided in 10 buckets, whcih form the classes.

An interesting side-observation of this experiment is that there is a noticeable spike in the number of projects that are funded close to 50% (See ProjCostsCovered.png). I am not sure what the reason for that is. Also, there are a substantial number of projects (36615) that were over-funded. It's a pity that the systems of DonorChoose allow for over-funding when there are so many others which are hardly funded.
