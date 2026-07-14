#!/usr/bin/env python
# coding: utf-8

# In[2]:


#clean dataset import and preview
import pandas as pd
dataset=pd.read_csv(r"C:\Users\USER\Desktop\first ds project\clean_liver.csv")
dataset.head
dataset.info


# In[3]:


#heat map to show correlation ,multicollinearity,drop columns with multicollinearity
numerical_var=dataset[['Age(years)','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']]
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(numerical_var.corr(),annot=True,cmap='coolwarm')
plt.show()


# In[11]:


get_ipython().system('pip install statsmodels')


# In[4]:


#confirm multicollinearity using variance_inflation_factor
import statsmodels
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif=pd.DataFrame()
vif["Variable"]=numerical_var.columns
vif["VIF"]=[variance_inflation_factor(numerical_var.values,i)
            for i in range(numerical_var.shape[1])]
print(vif)


# In[5]:


#age,albumin,prothrombin and Stage have high VIF which are all expected to rise with advancing liver diesease
#start logistic regression
# encode outcome with label encoder
target= dataset.OUTCOME
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
target_e=le.fit_transform(target)




# In[6]:


#encode norminal variables/predictors using get_dummies
predictor=dataset[['N_Days','Drug','Age(years)','Sex','Ascites','Hepatomegaly','Spiders','Edema','Bilirubin','Cholesterol','Albumin','Copper','Alk_Phos','SGOT','Tryglicerides','Platelets','Prothrombin','Stage']]
Predictors=pd.get_dummies(predictor,columns=["Drug","Sex","Ascites","Hepatomegaly","Spiders","Edema"],drop_first=True)


# In[7]:


#split data into training and testing sets
from sklearn.model_selection import train_test_split
P_train,P_test,T_train,T_test=train_test_split(Predictors,target_e,test_size=0.2,random_state=16)


# In[8]:


#scale predictor and target
from sklearn.preprocessing import StandardScaler
scalerr=StandardScaler()
Predictors_s=scalerr.fit_transform(P_train)
target_s= scalerr.transform(P_test)



# In[1]:


#Logistic regression
from sklearn.linear_model import LogisticRegression
loreg=LogisticRegression(random_state=16)
loreg.fit(P_train,T_train)
T_pred=loreg.predict(P_test)


# In[11]:


#model evaluation with the confusion matrix
from sklearn import metrics
conf_m=metrics.confusion_matrix(T_test,T_pred)
print(conf_m)


# In[12]:


#calculate performnce metrics( classification report)
from sklearn.metrics import classification_report
print(classification_report(T_test,T_pred))



# In[12]:


#roc curve and auc
from sklearn.metrics import roc_curve,roc_auc_score
T_prob=loreg.predict_proba(P_test)[:,1]
auc=roc_auc_score(T_test,T_prob)
print("ROC-AUC:",auc)

 


# In[13]:


fpr,tpr,thresholds=roc_curve(T_test,T_prob)
plt.figure(figsize=(6,6))
plt.plot(fpr,tpr,label=f"AUC={auc:.3f}")
plt.plot([0,1],[0,1],linestyle='--')
plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("ROC Curve")
plt.legend()
plt.show()


# In[13]:


#testing the model
logrege = LogisticRegression(max_iter=5000)
logrege.fit(P_train, T_train)
#predict if a patient will live or die
T_prede = logrege.predict(P_test)
#predict if a patient will die
T_proba = logrege.predict_proba(P_test)[:, 1]
#testing with a new patient's details
new_patient = [[100, 1,65,0,1,1,1,0,8.4,300,3.5,150,800,100,90,190,10.2,3]]
new_patient_scaled = scalerr.transform(new_patient)
prediction = logrege.predict(new_patient_scaled)
print(prediction)


# In[14]:


#confirming the outcome=death
print(le.classes_)


# In[31]:


for col in Predictors.columns:
    if Predictors[col].dtype == "bool":
        Predictors[col] = Predictors[col].astype(int)
print(Predictors.dtypes)


# In[32]:


#FINDING THE STRONGEST PREDICTORS OF DEATH IN PATIENTS WITH LIVER CIRRHOSIS
import statsmodels.api as sm
X = sm.add_constant(Predictors)
logit_model = sm.Logit(target_e, X)
result = logit_model.fit()

print(result.summary())


# In[33]:


# age(years),alk_phos and SGOT had p_values less than 0.05,ignore  N_days because it was follow up time
#odds ratios
import numpy as np
import pandas as pd

or_table = pd.DataFrame({
    "Odds Ratio": np.exp(result.params),
    "Lower 95% CI": np.exp(result.conf_int()[0]),
    "Upper 95% CI": np.exp(result.conf_int()[1]),
    "P-value": result.pvalues
})

print(or_table)


# In[ ]:




