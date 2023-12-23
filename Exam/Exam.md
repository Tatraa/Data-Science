Data exploration
==================

### 1. Explain what are the numerical and categorical variables.

__Numerical Variables__:
Numerical variables, also known as quantitative or continuous variables, take on numerical values and can be measured. These values represent quantities that can be subjected to mathematical operations such as addition, subtraction, multiplication, and division. Numerical variables can be further categorized into two types:

- Discrete Variables: These variables take on distinct, separate values. For example, the number of students in a class or the count of cars in a parking lot are discrete numerical variables.

- Continuous Variables: These variables can take any value within a range and often involve measurements. Examples include height, weight, temperature, and income.

Numerical variables are typically analyzed using descriptive statistics (mean, median, standard deviation) and inferential statistics (regression analysis, t-tests).

__Categorical Variables__:
Categorical variables, also known as qualitative or nominal variables, represent categories or groups. Unlike numerical variables, categorical variables don't have a natural order or ranking. They are divided into two main types:

- Nominal Variables: These variables represent categories with no inherent order or ranking. Examples include gender, ethnicity, and eye color.

- Ordinal Variables: These variables have categories with a meaningful order or ranking, but the intervals between the categories may not be consistent. Examples include education level (e.g., high school, college, graduate) or customer satisfaction ratings (e.g., low, medium, high).

Categorical variables are often summarized using frequencies and proportions. Chi-square tests and logistic regression are common statistical methods used for analyzing categorical data.

In summary, numerical variables involve measurable quantities and can be either discrete or continuous, while categorical variables represent different categories or groups and can be either nominal or ordinal. Understanding the nature of variables is crucial for selecting appropriate statistical methods and drawing meaningful conclusions from data analysis.

### 2. Explain what is the difference between experimental studies and observations What it is a confounding variable. When we can draw conclusion about correlations and when about causation?

Experimental Studies:

- __Experimental studies__ involve the manipulation of one or more independent variables to observe their effect on a dependent variable. Participants are randomly assigned to different groups, including a control group, to control for potential confounding variables.
Control: Researchers have more control over experimental conditions, allowing them to establish cause-and-effect relationships more convincingly.
Randomization: Random assignment helps distribute potential confounding variables equally among groups, reducing the likelihood of bias.
Observational Studies:

- __Observational studies__, on the other hand, involve observing and measuring variables without intervention. Researchers don't manipulate variables or control the study environment.
Control: There is less control over variables, and researchers rely on statistical methods to control for confounding factors.
Types: Observational studies can be cross-sectional (data collected at a single point in time), longitudinal (data collected over time), or retrospective (looking at past data).
Confounding Variable:
A confounding variable is an extraneous variable that correlates with both the independent variable and the dependent variable, making it difficult to determine the true cause-and-effect relationship between them. Confounding variables can introduce bias and lead to incorrect conclusions. Experimental studies often use randomization to minimize the impact of confounding variables, while observational studies use statistical techniques like matching or stratification to control for them.

__Correlation vs. Causation__:

- Correlation: Correlation indicates a statistical association between two variables. If two variables are correlated, it means they tend to vary together, but it doesn't imply causation. Correlation does not prove that changes in one variable cause changes in another.

- Causation: Causation implies a cause-and-effect relationship between two variables. Establishing causation requires evidence from experimental studies where variables are manipulated, and other potential influences are controlled. Randomization helps control for confounding variables, enhancing the ability to draw causal conclusions.

In summary, experimental studies involve manipulation and randomization, providing a stronger basis for establishing causation. Observational studies rely on observation without intervention, making it more challenging to claim causation due to potential confounding variables. Correlation does not imply causation, and caution should be exercised when interpreting relationships between variables in observational settings.

### 3. What is the difference between census and the sampling? What are the sampling methods?  What are the possible sources of the sampling bias.

Census:

Definition: A census is a data collection method that aims to gather information from every individual or element in a population. It involves studying the entire population.
Scope: Censuses are comprehensive and provide a complete set of data for analysis.
Applicability: Censuses are often used when the population size is small, manageable, or when it is feasible to collect data from every unit.
Sampling:

Definition: Sampling is a data collection method that involves selecting a subset (sample) of individuals or elements from a larger population and using the information from the sample to make inferences about the entire population.
Scope: Sampling is more practical when studying large populations where collecting data from every unit is time-consuming or costly.
Applicability: Sampling is widely used in various fields, including market research, social sciences, and medical research.
Sampling Methods:

Simple Random Sampling: Every individual in the population has an equal chance of being selected, and each selection is independent of the others.

Stratified Sampling: The population is divided into subgroups (strata) based on certain characteristics, and then random samples are taken from each stratum.

Systematic Sampling: Individuals are selected at regular intervals from a list after a random starting point is chosen.

Cluster Sampling: The population is divided into clusters, and then a random sample of clusters is selected. All individuals within the chosen clusters are included in the sample.

Convenience Sampling: Researchers select individuals who are readily available and convenient to study. This method may introduce bias, as it doesn't ensure a representative sample.

Possible Sources of Sampling Bias:

Selection Bias: Occurs when the method used to select the sample results in a non-representative group. For example, using volunteers may introduce bias if volunteers differ systematically from non-volunteers.

Non-Response Bias: Results from the failure to obtain responses from some individuals in the sample. If those who respond differ systematically from those who do not respond, it can introduce bias.

Undercoverage Bias: Occurs when some members of the population are less likely to be included in the sample. This can happen if certain groups are excluded or not adequately represented.

Sampling Frame Bias: Arises when the list or database used to create the sample does not accurately represent the population. If some individuals are missing from the sampling frame, it can lead to bias.

Survivorship Bias: Happens when the sample includes only those individuals or elements that have survived a selection process, leading to an incomplete or biased view of the population.

It's essential to be aware of these potential sources of bias and take steps to minimize them when designing and conducting sampling studies. Proper sampling techniques and randomization can help reduce bias and enhance the generalizability of findings.

### 4. How we define point estimate of sample statistics: measures of center and spread.  What does it mean "robust statistics". Which definitions have this features.

In statistics, point estimates are single values that are used to approximate or "estimate" population parameters based on sample data. Two fundamental types of point estimates are measures of center and measures of spread.

Measures of Center:

Mean (Arithmetic Average): The mean is the sum of all values in a dataset divided by the number of observations. It is a common point estimate of the center of a distribution.
Median: The median is the middle value when the data is ordered. It is less sensitive to extreme values than the mean and is a robust measure of central tendency.
Measures of Spread:

Standard Deviation: The standard deviation measures the average distance of each data point from the mean. It provides information about the spread or variability of the data.
Interquartile Range (IQR): The IQR is the range between the first quartile (25th percentile) and the third quartile (75th percentile). It is a robust measure of spread, especially in the presence of outliers.
Robust Statistics:

Robust statistics refer to statistical methods and measures that are not unduly influenced by outliers or extreme values in the data. In the context of measures of center, the median is considered a robust statistic because it is less affected by extreme values compared to the mean. Similarly, the interquartile range (IQR) is a robust measure of spread because it is based on quartiles and is not heavily influenced by outliers.

Robust Measures:

Median: As mentioned earlier, the median is less sensitive to outliers than the mean, making it robust in the presence of extreme values.

Interquartile Range (IQR): Since the IQR is based on quartiles (which are less affected by extreme values), it is considered a robust measure of spread.

Non-Robust Measures:

Mean: The mean is sensitive to extreme values, and a single outlier can significantly affect its value.

Standard Deviation: The standard deviation is influenced by extreme values, making it less robust when dealing with datasets containing outliers.

When dealing with datasets that may contain outliers or are not normally distributed, using robust statistics can provide more reliable and stable estimates of central tendency and spread. They are particularly useful when the data distribution is skewed or has heavy tails.

### 5. What is the box plot. Could you draw example and explain meaning of its content. How we deduce that distributions has a tail, outlayers, etc.

A box plot, also known as a box-and-whisker plot, is a graphical representation of the distribution of a dataset. It provides a visual summary of the central tendency, spread, and skewness of the data. The plot consists of a rectangular "box" and two "whiskers" extending from either end of the box.

Let me describe the components of a box plot and then provide an example:

Box Plot Components:

Box: The box represents the interquartile range (IQR), which is the range between the first quartile (Q1) and the third quartile (Q3). The box spans the middle 50% of the data. The line inside the box represents the median.

Whiskers: The whiskers extend from the box to the minimum and maximum values within a certain range. The range is often determined by a multiplier (e.g., 1.5 times the IQR). Points beyond the whiskers are considered potential outliers.

Outliers: Individual data points beyond the whiskers are considered potential outliers. They may be indicative of extreme values in the dataset.

Example Box Plot:

Let's consider an example box plot:

      
           
The box represents the interquartile range (IQR) between the first quartile (Q1) and the third quartile (Q3).
The line inside the box represents the median of the data.
The whiskers extend from the box to the minimum and maximum values within a certain range.
Points beyond the whiskers are considered potential outliers.
Interpreting a Box Plot:

Skewness: If the median is not centered in the box, the distribution may be skewed.

Tails: The length of the whiskers can give an indication of the spread of the data. Longer whiskers suggest a larger spread.

Outliers: Individual points beyond the whiskers are potential outliers. Outliers may indicate extreme values or data points that deviate significantly from the overall pattern of the data.

By examining the components of a box plot, you can gain insights into the central tendency, spread, and presence of outliers in a dataset. Box plots are particularly useful for comparing the distribution of different groups or variables.


Regression
==================

1. Draw the flow-chart diagram for making predictions using regression
   as ML algorithm.
   Explain briefly each box on the flow-chart: ML model, ML algorithm,
   Quality metric, Feature extraction.

2. Write down formula for simple linear regression model.
   How one can interpret coefficients.
   Write formula for defining cost function using RSS estimator.

3. Write down sequence of iterative gradient descent algorithm finding
   minimum of the cost function for simple linear regression.
   When do we stop iteration, how do we choose step-size.

4. How do we access performance? Explain what is the "training error",
   "validation error", "generalization error", "test error".
   What does it mean "cross-validation"?
   Draw illustrative plot how they typically behave with regression
   model complexity.

5. Explain what are the sources of errors on the prediction:
   noise, bias, variance.
   Draw simple illustration explaining it.
   What does it mean bias-variance trade-off.

6. What does it mean "over-fitting"?
   Explain how we can mitigate it adding extra term to the
   cost function:  "regge regression"  or "lasso regression".
   Write formula of the respective cost functions.
   Show illustrative plot how the coefficients w will behave in each case.

7. Explain procedure for selecting features for regression with
   the greedy algorithm.

8. What does it mean "non-parametric regression".
   Explain concept of: (1-NN) regression, (k-NN) regression,
   weighted regression, kernel regression.

 
Classification
==================

1. Explain model of logistic regression classifier.
   Write down formula for linear score and logistic link function.
   How it is extended in case of multi-classification problem.

2. We measure performance of the classifier based on:
   "classification error",  "classification accuracy", "confusion matrix".
   Could you explain what does it mean?
   What is the problem of "class majority".

3. Write formula for quality metric in case of logistic classifier:
   likelihood function.
   The best classifier is found using MLE (maximum likelihood estimation)
   method and gradient ascent.
   Could you write down and explain final formula of that algorithm.
   How do we choose step size.

4. Classification with decision trees. How one defines classification
   of the final leafs.
   How one measure quality of the predictions: error and accuracy. 
   Explain simple greedy algorithm to find the best decision tree.
   How one is measuring performance.

5. Greedy decision tree learning: what are the steps for building tree.
   Stopping conditions for the splitting in the decision tree model.
   What is the sign of over-fitting in decision trees, how one mitigate
   this effect: early stopping or pruning.
   Could you explain what does it mean?

6. What are strategies for handling missing data in case of decision trees.
 
7. Idea of ensemble classifiers and boosting. Could you explain the concept
   of weighted weak classifiers and weighted data.
   Could you write down formula for final mode predictions.

8. AdaBoost algorithm, formulas, learning process.


 
Clustering&Retrieval
=====================

1. Explain TF-IDF representation of documents.
   What are the metrics which are most commonly used to search for
   k-NN documents.

2. What are the KD-trees. How to build and query KD-tree.
   What is the complexity of querying and how it compares with complexity
   of other queries: 1-NN, k-NN.

3. Explain LSH method (locality sensitive hashing).
   Is it competitive to KD-tree method?

4. Describe steps of k-means clustering algorithm.
   How we measure its quality? Could you comment on its convergence

5. Explain probabilistic approach for clustering.
   The soft assignment can be optimised with MLE approach
   (maximum likelihood estimator).
   Can you explain what does it mean, give some formulas?

6. Explain what is the model for "bag-of-words" for clustering documents.

7. LDA method (Latent Dirichlet allocation). Can you explain the concept?

8. Hierarchical clustering. Explain algorithm, illustrate with dendrogram. 