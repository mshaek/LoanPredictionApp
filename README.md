# LoanPredictionApp
# Loan Repayment Challenge
## Mahfuzur Rahman Shaek
### Approx time spent: 30 hours

Machine learning models are commonly used for screening loan applications and continuous assessment even after the loan approval. MoneyLion being a fintech company, utilizes loan related data to draw insight which can help the organization offer better products and services to the appropriate customers. Machine learning helped to automate loan approval process and credit risk assessment which saved time and money, ultimately led to faster and better loan process as well as reduced risks and losses.

Google Colab has been used to explore and model the date using python libraries.Data Analysis and creating visualization can reveal some critical insights from the data. Some univariate and bivariate analysis have been done here to find the underlying relationship between the variables.

The 'Loan' dataset has been filtered for funded entries only. As those data points where a customer was not approved for loan or customer withdrawn the loan application before or after loan has not been considered. Therefore, not necessary to assess the credit risks for those customers who withdrew their application/ got rejected. A 'target' variable has been created from 'loan status' with categories similar to 'likely to default' or 'paid off'. Moneylion would target the customer who will pay off the loan and reduce the number of customer who would likely to default. This two categories makes it a binary classification problem. Four well-known modeling techniques are used to build the best model. These are Logistic Regression, Random Forest, XGBoost and a Neural Network. The best model is identified using evaluation metrics.

Customers who are likely to default are considered as positive class. So the false negative (model predicts customer will pay off but in actual customer would default) is costly to the business. Hence, FN has to be minised and true negative has to maximised. Also there will be an opportunity loss if model identified a good customer as potential defaulter(false positive). So some optimisation has to be done to decide the threshold value.

In this experiment, XGBoost model has better perfomance in terms of accuracy an AUC score.

Just for the illustration, a smaller model with handful features has been used to create an "Loan Prediction App". Accuracy is very low but this just for demo how the the end product may look like. Ovioulsly, a complete model will have more predictors and with better performance than the demo showed in this project.

This document has been organised as follows- uploading and initial preprocessing of all three data files. After exploring and visualisation, some important features have been selected for modeling. Then 4 modelling techniques were used to build model and their performances has been compared.


