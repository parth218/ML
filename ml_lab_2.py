# -*- coding: utf-8 -*-
"""ML_LAB_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GmqMK5B6gnh_gHJHltiUo4Uuai0rhq8Y

# **MACHINE LEARNING LAB - 2**

# **Problem Statement : Assignment on Exploratory data analysis**

# Assignment on Exploratory data analysis

Download Haberman Cancer Survival dataset from Kaggle. You may have to create a Kaggle account to donwload data. (https://www.kaggle.com/gilsousa/habermans-survival-data-set) or you can also run the below cell and load the data directly.
"""

import warnings
import numpy as np
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('haberman.csv')
df.head()

"""### 1.1 Analyze high level statistics of the dataset: number of points, numer of   features, number of classes, data-points per class.
- You have to write all of your observations in Markdown cell with proper formatting.
- Do not write your observations as comments in code cells.

"""

df.info()

df.describe()

# pie chart
plt.pie(df['status'].value_counts(), labels=df['status'].value_counts().index, autopct='%1.1f%%')

"""### 1.2 - Explain the objective of the problem.
(The objective for a problem can be defined as a brief explanation of problem that you are trying to solve using the given dataset)

*   The objective of this assignment is to preform exploratory data on analysis Hoberman Cancer Survival dataset obtained from Kaggle. The main aim is to preform univariate as well as bivariate analysis on the feature set to identify the bed features which can used for training different classification models.

### 1.3 Perform Univariate analysis - Plot PDF, CDF, Boxplot.
- Plot the required charts to understand which feature are important for classification.
- Make sure that you add titles, legends and labels for each and every plots.
- Do write observations/inference for each plot.
"""

import seaborn as sns

sns.set_style("whitegrid")
sns.pairplot(df, hue="status", palette="RdGy")
plt.show()

sns.heatmap(df.corr(), annot=True)

sns.FacetGrid(df, hue="status", height=10, size=5) \
   .map(sns.distplot, "age") \
   .add_legend()

plt.show()

sns.FacetGrid(df, hue="status", height=10, size=5) \
   .map(sns.distplot, "year") \
   .add_legend()
plt.show()

sns.FacetGrid(df, hue="status", height=10, size=5) \
   .map(sns.distplot, "nodes") \
   .add_legend()
plt.show()

counts, bin_edges = np.histogram(df['age'], bins=10, density = True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.show()

counts, bin_edges = np.histogram(df['year'], bins=10, density = True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.show()

counts, bin_edges = np.histogram(df['nodes'], bins=10, density = True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

plt.show()

fig, axes= plt.subplots(1,3, figsize=(15,5))
for idx, feature in enumerate(list(df.columns)[:-1]):
     sns.boxplot(data=df, x='status', y= feature, ax= axes[idx])

"""### 1.4 Perform Bivariate analysis - Plot 2D Scatter plots and Pair plots
- Plot the required Scatter plots and Pair plots of different features to see which combination of features are useful for clasification task
- Make sure that you add titles, legends and labels for each and every plots.
- Do write observations/inference for each  plot.

"""

status_1 = df[df['status'] == 1]
status_2 = df[df['status'] == 2]

plt.scatter(status_1['age'], status_1['year'], color='red', label='status = 1')
plt.scatter(status_2['age'], status_2['year'], color='green', label='status = 2')
plt.xlabel('age')
plt.ylabel('year')
plt.legend()
plt.title("age -> year")
plt.show()

"""* We cannot use age -> year for classification of status"""

plt.scatter(status_1['age'], status_1['nodes'], color='red', label='status = 1')
plt.scatter(status_2['age'], status_2['nodes'], color='green', label='status = 2')
plt.xlabel('age')
plt.ylabel('nodes')
plt.legend()
plt.title("age -> nodes")
plt.show()

"""* We cannot use age -> nodes for classification of status"""

plt.scatter(status_1['nodes'], status_1['year'], color='red', label='status = 1')
plt.scatter(status_2['nodes'], status_2['year'], color='green', label='status = 2')
plt.xlabel('nodes')
plt.ylabel('year')
plt.legend()
plt.title("nodes -> year")
plt.show()

"""* We cannot use nodes->year for classification of status

### 1.5 Summarize your final conclusions of the Exploration
- You can desrcibe the key features that are important for the Classification task.
- Try to quantify your results i.e. while writing observations include numbers,percentages, fractions etc.
- Write a brief of your exploratory analysis in 3-5 points
-After performing the EDA on the dataset, we can conclude that none of the features aremore important than the others. Hence all of the features will be considered equal.

Exploratory Data Analysis:


*  There are 306 data points in the dataset.

*   There are 3 features in the dataset namely: Age, Op_Year, axil_nodes.
*   The output class is Surv_status which has two class labels 1 which depicts that patient survived 5 years or longer and 2 which depicts the patient died within 5 year 
* There are 255 data samples belonging to class 1 and 81 samples belonging to class Thus we can say that the datasks is imbalanced. 
*  Pie chart of the class label shows that 74% of the patient survived 5 years or longer whereas 26% of the patient died within 5 year.
*   After plotting the scatter plot for all the three features, we can conclude that there is overlapping between both the class label. Thus none of the feature can be linearly separated.

*  After plotting the PDF (Probability Distribution Function) for all the three features, we can conclude that there is overlapping between both the class label.

*  As we can observe from the 2D scatter plot and pair plot, that none of the feature pairs are linearly separable. Thus, we cannot give preference to any feature pair.
"""