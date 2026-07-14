#Predicting Mortality in Patients with Liver Cirrhosis Using Logistic Regression
###Introduction
Liver cirrhosis is a chronic progressive disease associated with significant morbidity and mortality worldwide. Early identification of patients at high risk of death is essential for timely intervention, improved clinical decision-making, and optimal allocation of healthcare resources.
This project applies supervised machine learning and statistical modelling techniques to identify factors associated with mortality among patients diagnosed with liver cirrhosis. A logistic regression model was developed to predict mortality and evaluate the contribution of clinical and laboratory variables to patient outcomes.

###Objective
The objectives of this project were to:
-	Predict mortality among patients with liver cirrhosis using logistic regression.
-	Identify independent predictors associated with mortality.
-	Evaluate the predictive performance of the model using standard classification metrics.
-	Demonstrate an end-to-end healthcare data science workflow from data preprocessing to model interpretation.

###Skills Demonstrated
Throughout this project, the following data science and analytical skills were applied:
-	Data cleaning and preprocessing using Excel
-	Handling missing values
-	Exploratory data analysis (EDA)
-	Feature engineering
-	Encoding categorical variables using Label Encoding and get_dummies
-	Multicollinearity assessment using Variance Inflation Factor (VIF)
-	Feature selection
-	Train-test splitting
-	Feature scaling using StandardScaler
-	Logistic Regression modelling using Scikit-learn
-	Statistical logistic regression using Statsmodels
-	Model evaluation using: Confusion Matrix, Accuracy, Precision, Recall,F1-score, ROC Curve, Area Under the Curve (AUC)
-	Interpretation of regression coefficients and Odds Ratios
-	Clinical interpretation of predictive variables

###Data Sourcing
The dataset used in this project was obtained from the UCI Machine Learning repository and contains 294 patients’ data after data cleaning including: patient age, sex, drug allocation, serum bilirubin, cholesterol, albumin, copper, alkaline phosphatase, SGOT, triglycerides, platelet count, prothrombin time, disease stage, presence of ascites, hepatomegaly, spiders, edema, patient outcome (mortality status)
For this analysis, patients with censored outcomes were excluded to allow the development of a binary classification model for mortality prediction.

###Data Transformation and Modelling
The following preprocessing pipeline was implemented:
-	Removed records with censored outcomes.
-	Selected variables relevant to mortality prediction.
-	Checked for missing values and replaced them with the column average
-	Encoded categorical variables using Label Encoding and get_dummies where appropriate.
-	Assessed multicollinearity among predictors using Variance Inflation Factor (VIF).
-	Split the dataset into training and testing subsets.
-	Standardized numerical variables using StandardScaler.
-	Developed a Logistic Regression model using Scikit-learn for predictive modelling.
-	Evaluated model performance using classification metrics and ROC-AUC.
-	Built a statistical logistic regression model using Statsmodels to estimate coefficients, Odds Ratios, confidence intervals, and p-values for predictor interpretation.

###Model Performance Report
The logistic regression model demonstrated satisfactory performance in predicting mortality among patients with liver cirrhosis. For patients who survived throughout the follow up duration, the model achieved a precision of 0.76, indicating that 76% of patients predicted to belong to this class were correctly classified. The model also attained a recall of 0.79, meaning it correctly identified 79% of all patients that remained alive throughout the follow up process, with an F1-score of 0.78, reflecting a good balance between precision and recall.
For patients that died during the follow up process, the model achieved a precision of 0.72, indicating that 72% of patients predicted to belong to this class were correctly classified. The recall was 0.69, showing that the model correctly identified 69% of all who died . The resulting F1-score of 0.71 suggests a reasonably balanced performance in predicting this outcome.
The ROC-AUC of 0.79  indicates that the model has good discriminatory ability and is suitable for identifying patients at increased risk of the outcome.
Key Findings
Odds Ratios were calculated to quantify the strength of association between each predictor and mortality.
Variables with p-values greater than 0.05 were not considered statistically significant independent predictors in the adjusted model.
The multivariable logistic regression analysis identified age, alkaline phosphatase (Alk_Phos), SGOT, and prothrombin time as statistically significant independent predictors of mortality (p < 0.05). Specifically, each additional year of age was associated with a 3.6% increase in the odds of death (AOR = 1.04, 95% CI: 1.00–1.07, p = 0.046), while a one-unit increase in prothrombin time more than doubled the odds of mortality (AOR = 2.16, 95% CI: 1.41–3.30, p < 0.001). Higher alkaline phosphatase (AOR = 1.0003, p = 0.001) and SGOT levels (AOR = 1.01, p = 0.038) were also significantly associated with increased odds of death.
Other variables, including bilirubin, cholesterol, albumin, copper, triglycerides, platelet count, disease stage, sex, drug allocation, hepatomegaly, spiders, and edema, were not statistically significant predictors of mortality in the adjusted model (p > 0.05). 

