#!/usr/bin/env python
# coding: utf-8

# # Import necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load the dataset

# In[2]:


dataset_path = r'C:\data\Covid Data.csv'
df = pd.read_csv(dataset_path)


# # Summary statistics

# In[3]:


summary_stats = df.describe()
print('Summary Statistics:')
print(summary_stats)


# # Infographics visualisation

# In[4]:


fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Bar plot for Patient Types
sns.countplot(x='PATIENT_TYPE', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Patient Types')
axes[0, 0].set_xlabel('Patient Type')
axes[0, 0].set_ylabel('Count')

# Plot 2: Pie chart for Gender distribution
gender_distribution = df['SEX'].value_counts()
axes[0, 1].pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Gender Distribution of Patients')

# Plot 3: Box plot for Age distribution
sns.boxplot(x='SEX', y='AGE', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Age Distribution by Gender')
axes[1, 0].set_xlabel('Gender')
axes[1, 0].set_ylabel('Age')

# Plot 4: Distribution of Ages
sns.histplot(df['AGE'], bins=20, kde=True, ax=axes[1, 1])
axes[1, 1].set_title('Distribution of Ages')
axes[1, 1].set_xlabel('Age')
axes[1, 1].set_ylabel('Frequency')

fig.suptitle('COVID-19 Infographics - Analysis of Patient Data', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show


# In[ ]:




