# DonorsChoose

An Experiment with DonorsChoose projects data
==============================================

Kaggle recently opened up a competition to help DonorChoose with targeted marketing. Since I am relatively new to the ML libraries, I decided to make up a project of my own. The goal of the project is to ascertain whether there is a correlation between the category the project belongs to, the kind of resources they ask for and similar other parameters and the total donation these projects accumulate.

Part1:
-----
I am using the Projects.csv and Donations.csv files for this experiment and are available at:https://www.kaggle.com/donorschoose/datasets .To run the experiments, execute files in the order step1.py -> step2.py -> step3.py.

I am modelling the regression problem where the independent variables are ('Project Cost', 'Project Subject Category Tree', 'Project Grade Level Category', 'Project Resource Category') and the variable to predict is the fraction of the total cost that is funded. Note that this variable is bounded between 0 and 1. For this reason, I am using logistic regression with multiple classes as the predictor. All the possible values that the dependent variable can take can divided in 10 buckets, whcih form the classes.

Part2: (in /Code and /Graphs)
-----

In the second part, I extend the same idea to a larger set of attributes; specifically, using (Project Cost,Project Subject Category Tree,Project Grade Level Category,Project Resource Category,Total Donation,School Metro Type,School Percentage Free Lunch,School State).

Indeed this allowed me to extract some useful prediction measure. Using logistic regression (along the same lines as in Part 1), I could show a 76% prediction accuracy of whether a given project would collect at least 25% of its project cost or not. More interestingly, the more sophisticated methods like lightgbm and adaboost perform much worse.

Just for insight, I have also plotted some graphs. These can be found in Graphs folder.

Conclusion:
-----------

The classification score obtained with just 2 buckets is sligtly above 50% i.e. with just these parameters *and nothing else* one can predict slightly better than random guessing whether the project donations will cross the 50% mark or not. This is rather expected since the only information we used was *some project parameters*. We do not consider the project essay for example, which might hold significant clues as to *how important* the project is for students. Nevertheless, I believe this experiment shows that the project parameters used here are not entirely irrelevant in their impact on the actual donations received.

An interesting side-observation of this experiment is that there is a noticeable spike in the number of projects that are funded close to 50% (See ProjCostsCovered.png). I am not sure what the reason for that is. Also, there are a substantial number of projects (36615) that were over-funded. It's a pity that the systems of DonorChoose allow for over-funding when there are so many others which are hardly funded.
