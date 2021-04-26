# Project 2 Pattern Discovery and Building Predictive Models

Datasets and Problem Domain
For this project, we would like to use the mobile price classification dataset as the source of data. The target of this project is to predict whether the price of a mobile phone is high or not. A copy of the necessary files is  here

Project 2 aims to produce clean, reduced or transformed data for pattern discovery and predicative analysis. In this project, we will assess the data cleaning and predictive model building skills. You can use either Weka or other data analytic toolsets (e.g., R or Python) familiar to you.

Datasets and Problem Domain
For this project, we would like to use the mobile price classification dataset as the source of data. The target of this project is to predict whether the price of a mobile phone is high or not. A copy of the necessary files is  here

## Your tasks
1. Data cleaning and analysis
a. Read through the table and the table column descriptions. Understand the meaning of each column in the table.
b. Distinguish the type of each attribute (e.g., nominal/categorical, numerical). You may need to discretise some attributes, when completing Task 2, 3 or 4.
c. Determine whether an attribute is relevant to your target variable. You may remove some attributes if they are not helpful for Task 2, 3, or 4. You might create separate data files for Task 2, 3 and 4.
d. Identify inconsistent data and take actions using the knowledge you have learnt in this unit.
Note: You may use different data processing procedures, when working on different tasks to get better results.

2. Association rule mining
Select a subset of the attributes (or all the attributes) to mine interesting patterns. To rank the degree of interesting of the rules extracted, use support, confidence and lift.
Explain the top k rules (according to lift or confidence) that have the "price_category” on the right-hand-side, where k >= 1.
Explain the meaning of the k rules in plain English.
Given the rules, what recommendation will you give to a company willing to design a high price mobile phone (e.g., should the mobile phone equipped with bluetooth)?

3. Classification
Use the "price_category" as the target variable and train two classifiers based on different machine learning algorithms (e.g. classifier 1 based on a decision tree; classifier 2 based on SVMs).
Evaluate the classifiers based on some evaluation metrics (e.g., accuracy). You may use 10-fold cross-validation for the evaluation.

4. Clustering
Run a clustering algorithm of your choice and explain how the results can be interpreted with respect to the target variable.

5. Data reduction
Perform numerosity reduction and perform attribute reduction.
Train the two classifiers in Task 3 on the reduced data.
Answer the question: "Does data reduction improve the quality of the classifiers"?

6. Attribute selection
Select the top-10 most important attributes manually based on your understanding of the problem; select the top-10 most important attributes based on Information Gain.
Which attribute selection method is better and why?

## Files to submit
A zip file that contains:

- A report in PDF containing the six tasks listed above. If you work in team, only one submission is needed and the contribution of each team member should be clearly mentioned. Clearly indicate the name and student number of yourself and the team member.
- All the codes (e.g., python, SQL script) and/or screenshots (for Excel, or other data processing software) of data cleaning and process procedures.
- Intermediate and final result files for all data processing procedures.